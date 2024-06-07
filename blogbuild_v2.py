import os
import html2text
import json
import html
import re
from datetime import datetime
from pathlib import Path
import shutil

POSTS_DIRECTORY = "docs/posts"
PAGES_DIRECTORY = "docs/pages"
ORIGINAL_PAGES_DIRECTORY = "data/original_pages"
ORIGINAL_POSTS_DIRECTORY = "data/original_posts"

def fix_drop_content(drop):
    content = f"""{drop['note']}"""
    if drop['excerpt'] != "":
        content += f"""\n\n* **Web site excerpt:** {drop['excerpt']}\n"""
    return content

def fix_drop_tags(tags):
    if isinstance(tags, list):
        return tags
    ret_tag = re.split(', | |,', tags)
    if ret_tag != tags:
        print(f"""blogbuild_v2 fixed {tags} -> {ret_tag}""")
    return ret_tag

def fix_drop_date(date_string):
    parsed_date = datetime.fromisoformat(date_string.rstrip("Z"))
    parsed_date.replace(tzinfo=None)
    return parsed_date.strftime("%Y-%m-%d")        


class BlogBuild:
    def __init__(self):
        self.text_maker = html2text.HTML2Text()
        self.text_maker.protect_links = True
        directory = Path(POSTS_DIRECTORY)
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir()  
        
    def retrieve_tags_from_file(self):
        with open('data/wp_tags.json') as json_file:
            self.tags = json.load(json_file)
    
    def retrieve_drops_from_file(self):
        with open('data/drops.json') as json_file:
            self.drops = json.load(json_file)
    
    def retrieve_api_drops_from_file(self):
        with open('data/api_drops.json') as json_file:
            self.drops = json.load(json_file)
    
    def retrieve_wp_posts_from_file(self):
        with open('data/wp_posts.json') as json_file:
            self.wp_posts = json.load(json_file)

    def retrieve_wp_pages_from_file(self):
        with open('data/wp_pages.json') as json_file:
            self.wp_pages = json.load(json_file)

    def copy_all_files(self, source, destination):
        count = 0
        for filename in os.listdir(source):
            file_path = os.path.join(source, filename)
            try:
                if os.path.isfile(file_path):
                    shutil.copy(file_path, destination)
                count += 1
            except Exception as e:
                print(f'blogbuild_v2: Failed to copy {file_path}. Reason: {e}')
        print(f"""blogbuild_v2Total: {count} files copied""")

    def run(self):
        self.create_or_empty_directory(POSTS_DIRECTORY)
        self.create_or_empty_directory(PAGES_DIRECTORY)
        self.retrieve_api_drops_from_file()
        self.retrieve_tags_from_file()
        self.retrieve_wp_posts_from_file()
        self.retrieve_wp_pages_from_file()
        self.generate_drop_posts()
        self.generate_wp_posts()
        self.generate_wp_pages()
        self.incorporate_original_pages()
        self.incorporate_original_posts()

    def incorporate_original_pages(self):   
        self.copy_all_files(ORIGINAL_PAGES_DIRECTORY, PAGES_DIRECTORY)
    
    def incorporate_original_posts(self):
        self.copy_all_files(ORIGINAL_POSTS_DIRECTORY, POSTS_DIRECTORY)


    def generate_wp_posts(self):
        count = 0
        for post in self.wp_posts:
            content = self.text_maker.handle(post['content']['rendered'])
            title = post['title']['rendered']
            date = datetime.strptime(post['date'], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
            if self.drops.get(title) is not None:
                # print(f"""Skipping {title} because it is a drop""")
                continue
            tags = self.generate_tags_string(post['tags'])
            self.save_individual_post(title, content, date, tags, None, None)
            # print(f"Adding Post {title}")
            count += 1
        print(f"""blogbuild_v2: Total: {count} wp Posts Generated""")

    def generate_wp_pages(self):
        count = 0
        for post in self.wp_pages:
            content = self.text_maker.handle(post['content']['rendered'])
            title = post['title']['rendered']
            date = datetime.strptime(post['date'], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
            self.save_individual_page(title, content, date, None, None)
            count += 1
        print(f"""blogbuild_v2: Total: {count} wp Pages Generated""")

    
    def generate_drop_posts(self):
        count = 0
        for index, (drop_title, drop) in enumerate(self.drops.items()):
            title = drop_title
            content = self.fix_drop_content(drop)
            date = self.fix_drop_date(drop['created'])
            url = drop['url']
            cover = drop['cover']
            rawtags = self.fix_drop_tags(drop['tags'])
            if rawtags not in ['', 'None', [''], []]:
                tags_str = """\ntags:"""
                for tag in rawtags:
                    if re.match(r"^\d+$", tag):
                        tag = "N" + tag
                        print(f"""blogbuild_v2: numerical {tag}""")
                    if re.match(r".*[,+.=:!'].*", tag) is not None:
                        print(f"""blogbuild_v2: invalid: {tag}""")
                        tag = "FOOBAR"
                    tags_str += f"""\n    - {tag}"""
            else:
                tags_str = ""
            self.save_individual_post(title, content, date, tags_str, url, cover)
            count += 1
        print(f"""blogbuild_v2: total: {count} Drop Posts Generated""")

    def fix_drop_content(self, drop):
        content = f"""{drop['note']}"""
        if drop['excerpt'] != "":
            content += f"""\n\n* **Web site excerpt:** {drop['excerpt']}\n"""
        return content
    
    def fix_drop_tags(self, tags):
        if isinstance(tags, list):
            return tags
        ret_tag = re.split(', | |,', tags)
        if ret_tag != tags:
            print(f"""blogbuild_v2: {tags} -> {ret_tag}""")
        return ret_tag

    def fix_drop_date(self, date_string):
        parsed_date = datetime.fromisoformat(date_string.rstrip("Z"))
        parsed_date.replace(tzinfo=None)
        return parsed_date.strftime("%Y-%m-%d")        

    def generate_tags_string(self, tags):
        tags_string = ""
        for tag_id in tags:
            tag_id = str(tag_id)
            tag_text = self.tags.get(tag_id)
            if tag_text is None:
                tag_text = "none"
            tag_text = "none" if tag_text is None else tag_text
            if isinstance(tag_text, int):
                tag_text = str(tag_text)
            tags_string += f"\n    - {tag_text}"
        if tags_string != "":
            tags_string = f"\ntags:{tags_string}"
        return tags_string
    
    def save_individual_post(self, title, content, date, tags, url, cover):
        if cover is not None:
            cover_markdown = f"""<img class="cover" src={cover}>\n"""
            cover_text = f"""\ncover: "{cover}" """
        else:
            cover_markdown = ""
            cover_text = ""
        url_text = "" if url is None else f"""\nurl: "{url}" """
        url_text += "" if url is None else f"""\nlink: "{url}" """
        title = html.unescape(title)
        title = title.replace('"', '\\"')        
        file_path = os.path.join(POSTS_DIRECTORY, self.sanitize_filename(date, title))
        with open(file_path, 'w', encoding='utf-8') as file:
            markdown =f"""---
title: "{title}"
author: Pito Salas{url_text}{cover_text}
date: {date}{tags}
---
{cover_markdown}
{content}
* **Link to site:** **[{title}]({url})**
"""
            file.write(markdown)

    def save_individual_page(self, title, content, date, url, cover):
        if cover is not None:
            cover_markdown = f"""<img src={cover} width="500">\n"""
            cover_text = f"""\ncover: "{cover}" """
        else:
            cover_markdown = ""
            cover_text = ""
        url_text = "" if url is None else f"""\nurl: "{url}" """
        title = html.unescape(title)
        title = title.replace('"', '\\"')        
        file_path = os.path.join(PAGES_DIRECTORY, f"{title.replace(' ', '-')}.md")
        with open(file_path, 'w', encoding='utf-8') as file:
            markdown =f"""---
title: "{title}"
author: Pito Salas{url_text}{cover_text}
date: {date}
---
{cover_markdown}
{content}
---
[{title}]({url})
"""
            file.write(markdown)
 
    def sanitize_filename(self, date, title):
        filename = f"{date}-{title.replace(' ', '-')}.md"
        filename = re.sub(r'[\\/*?:"<>|]', "_", filename)  # Replace forbidden characters with underscore
        filename = re.sub(r'\s+', '', filename.strip())   # Replace spaces or consecutive spaces with dash
        return filename[:255]

    def create_or_empty_directory(self, dir_path):
        # Check if the directory exists
        if os.path.exists(dir_path):
            # Empty the directory
            for filename in os.listdir(dir_path):
                file_path = os.path.join(dir_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'blogbuild_v2: Failed to delete {file_path}. Reason: {e}')
        else:
            # Create the directory if it doesn't exist
            os.makedirs(dir_path)

# Main program
if __name__ == "__main__":
    print("blogbuild_v2: start")
    blog_build = BlogBuild()
    blog_build.run()
    print("blogbuild_v2: done")


