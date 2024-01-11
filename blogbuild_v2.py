import os
import html2text
import json
import html
import re
from datetime import datetime
from pathlib import Path
import shutil

POSTS_DIRECTORY = "docs/posts"
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
    
    def retrieve_wp_posts_from_file(self):
        with open('data/wp_posts.json') as json_file:
            self.wp_posts = json.load(json_file)

    
    def run(self):
        self.retrieve_drops_from_file()
        self.retrieve_tags_from_file()
        self.retrieve_wp_posts_from_file()
        self.generate_drop_posts()
        self.generate_wp_posts()
        # self.generate_original_posts()

    def generate_original_posts(self):
        pass

    def generate_wp_posts(self):
        count = 0
        for post in self.wp_posts:
            content = self.text_maker.handle(post['content']['rendered'])
            title = post['title']['rendered']
            date = post['date']
            if self.drops.get(title) is not None:
                print(f"""Skipping {title} because it is a drop""")
                continue
            tags = self.generate_tags_string(post['tags'])
            self.save_individual_post(title, content, date, tags, None, None)
            count += 1
        print(f"""Total: {count} wp Posts Generated""")

    
    def generate_drop_posts(self):
        count = 0
        for index, (drop_title, drop) in enumerate(self.drops.items()):
            title = drop_title
            content = self.fix_drop_content(drop)
            date = self.fix_drop_date(drop['created'])
            url = drop['url']
            cover = drop['cover']
            rawtags = self.fix_drop_tags(drop['tags'])
            if rawtags not in ['', 'None', ['']]:
                tags_str = """\ntags:"""
                for tag in rawtags:
                    if re.match(r"^\d+$", tag):
                        tag = "N" + tag
                        print(f"""*** {tag} ***""")
                    if re.match(r".*[,+.=:!'].*", tag) is not None:
                        print(f"""***** {tag}""")
                        tag = "FOOBAR"
                    tags_str += f"""\n    - {tag}"""
            else:
                tags_str = ""
            self.save_individual_post(title, content, date, tags_str, url, cover)
            count += 1
        print(f"""Total: {count} Drop Posts Generated""")

    def fix_drop_content(self, drop):
        content = f"""{drop['note']}"""
        if drop['excerpt'] != "":
            content += f"""\n\n(**Web site except:** {drop['excerpt']}) """
        return content
    
    def fix_drop_tags(self, tags):

        ret_tag = re.split(', | |,', tags)
        if ret_tag != tags:
            print(f"""{tags} -> {ret_tag}""")
        return ret_tag

    def fix_drop_date(self, date_string):
        parsed_date = datetime.fromisoformat(date_string.rstrip("Z"))
        parsed_date.replace(tzinfo=None)
        return parsed_date.strftime("%Y-%m-%d %H:%M:%S")        

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
            cover_markdown = f"""<img src={cover} width="500">\n"""
            cover_text = f"""cover: "{cover}" """
        else:
            cover_markdown = ""
            cover_text = ""
        url_text = "" if url is None else f"""url: "{url}" """
        title = html.unescape(title)
        title = title.replace('"', '\\"')        
        filename = f"{date}-{title.replace(' ', '-')}.md"
        file_path = os.path.join(POSTS_DIRECTORY, self.sanitize_filename(filename))
        with open(file_path, 'w', encoding='utf-8') as file:
            markdown =f"""---
title: "{title}"
author: Pito Salas
{url_text}
{cover_text}
date: {date}{tags}
---
{cover_markdown}
{content}
"""
            file.write(markdown)

    def sanitize_filename(self, filename):
        filename = re.sub(r'[\\/*?:"<>|]', "_", filename)  # Replace forbidden characters with underscore
        filename = re.sub(r'\s+', '-', filename.strip())   # Replace spaces or consecutive spaces with dash
        return filename[:255]
            
# Main program
if __name__ == "__main__":
    blog_build = BlogBuild()
    blog_build.run()
    print("done")

                    


