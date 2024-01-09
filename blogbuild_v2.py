import os
import html2text
import json
import html
import re
from datetime import datetime


class BlogBuild:
    def __init__(self):
        self.text_maker = html2text.HTML2Text()
        self.text_maker.protect_links = True
        self.posts_directory = "docs/posts"
        os.makedirs(self.posts_directory, exist_ok=True)

    def retrieve_tags_from_file(self):
        with open('data/tags.json') as json_file:
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
        # self.generate_wp_posts()
        # self.generate_original_posts()

    def generate_original_posts(self):
        pass
re.
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
            self.save_individual_post(title, content, date, tags)
            count += 1
        print(f"""Total: {count} wp Posts Generated""")

    
    def generate_drop_posts(self):
        count = 0
        for index, (drop_title, drop) in enumerate(self.drops.items()):
            title = drop_title
            content = self.fix_drop_content(drop)
            date = self.fix_drop_date(drop['created'])
            rawtags = self.fix_drop_tags(drop['tags'])
            if rawtags not in ['', 'None', ['']]:
                tags_str = f"""\ntags:"""
                for tag in rawtags:
                    tags_str += f"""\n    - {tag}"""
            else:
                tags_str = ""
            self.save_individual_post(title, content, date, tags_str)
            count += 1
        print(f"""Total: {count} Drop Posts Generated""")

    def fix_drop_content(self, drop):
        content = f"""{drop['note']}"""
        if drop['excerpt'] != "":
            content += f"""\n\n(**Web site except:** {drop['excerpt']}) """
        return content
    
    def fix_drop_tags(self, tags):
        return re.split(', | |,', tags)

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
            if type(tag_text) == int:
                tag_text = str(tag_text)
            tags_string += f"\n    - {tag_text}"
        if tags_string != "":
            tags_string = f"\ntags:{tags_string}"
        return tags_string
    
    def save_individual_post(self, title, content, date, tags):
        title = html.unescape(title)
        title = title.replace('"', '\\"')        
        filename = f"{date}-{title.replace(' ', '-')}.md"
        file_path = os.path.join(self.posts_directory, self.sanitize_filename(filename))
        with open(file_path, 'w', encoding='utf-8') as file:
            markdown =f"""---
title: "{title}"
author: Pito Salas
date: {date}{tags}
---
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

                    


