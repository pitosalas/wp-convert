import json
import os
import requests
import html2text
import re
from datetime import datetime
import html

MAX_API_PAGES = 1
LINKS_PER_PAGE = 30


class WPImport:
    def __init__(self):
        self.posts = []
        self.tags = {}
        self.drops = {}

    def retrieve_posts(self):
        # Endpoint for the WordPress post API, replace with your WordPress site URL
        url = 'http://www.salas.com/wp-json/wp/v2/posts'
        headers = {'Accept': 'application/json', 'User-Agent': 'Safari'}
        current_page = 1
        total_pages = None
        while current_page != total_pages and current_page < MAX_API_PAGES:
            params = {'page': current_page}
            response = requests.get(url, headers=headers, params=params)
            total_pages = int(response.headers['X-WP-TotalPages'])
            current_page += 1
            self.process_posts(response, self.process_a_post)
            print(f'Retrieved {len(self.posts)} posts so far')
        return requests.get(url, headers=headers)

    def process_posts(self, response, action):
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json()
            for post in posts:
                self.posts.append(action(post))
        else:
            print(
                'Failed to retrieve posts. Status code:', response.status_code
            )
            print(response.text)

    def process_a_post(self, post) -> dict:
        return {
            'title': post['title']['rendered'],
            'content': post['content']['rendered'],
            'date': post['date'].replace('T', ' ').replace('Z', ''),
            'slug': post['slug'],
            'tags': post['tags'],
        }

    def retrieve_tags_from_file(self):
        with open('tags.json') as json_file:
            self.tags = json.load(json_file)

    def retrieve_drops_from_file(self):
        with open('raindrop/drops.json') as json_file:
            self.drops = json.load(json_file)

    def run(self):
        self.retrieve_tags_from_file()
        self.retrieve_drops_from_file()
        self.retrieve_posts()
        print('done')


class BlogGenerator:
    def __init__(self):
        self.text_maker = html2text.HTML2Text()
        self.text_maker.protect_links = True
        self.posts_directory = 'posts'
        os.makedirs(self.posts_directory, exist_ok=True)

        # self.index_directory = "index"
        # os.makedirs(self.index_directory, exist_ok=True)

    def generate(self, posts, tags, drops):
        self.drops = drops
        self.cp_number = 0
        # self.start_index_page()
        self.tags = tags
        for post in posts:
            content = self.text_maker.handle(post['content'])
            title = post['title']
            date = post['date']
            if drops.get(title) is not None:
                print(f"""Skipping {title} because it is a drop""")
                continue
            tags = self.generate_tags_string(post['tags'])
            # self.add_post_to_index_page(title, content, date)
            self.save_individual_post(title, content, date, tags)

    def generate_drop_posts(self):
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
                tags_str = ''
            self.save_individual_post(title, content, date, tags_str)

    def fix_drop_content(self, drop):
        content = f"""{drop['note']}"""
        if drop['excerpt'] != '':
            content += f"""\n\n(**Web site except:** {drop['excerpt']}) """
        return content

    def fix_drop_tags(self, tags):
        return re.split(', | |,', tags)

    def fix_drop_date(self, date_string):
        parsed_date = datetime.fromisoformat(date_string.rstrip('Z'))
        parsed_date.replace(tzinfo=None)
        return parsed_date.strftime('%Y-%m-%d %H:%M:%S')

    def generate_tags_string(self, tags):
        tags_string = ''
        for tag_as_int in tags:
            tag_as_int = str(tag_as_int)
            tag_text = self.tags.get(tag_as_int)
            if tag_text is None:
                tag_text = 'none'
            else:
                print(tag_text)
            tag_text = 'none' if tag_text is None else tag_text
            tags_string += f'\n    - {tag_text}'
        if tags_string != '':
            tags_string = f'\ntags:{tags_string}'
        return tags_string

    def start_index_page(self):
        self.index_count = 0
        self.index_text = ''
        self.cp_start_date = None
        self.index_end_date = None

    def add_post_to_index_page(self, title, content, date):
        self.index_count += 1
        markdown = f"""#### {title}\n{content}\n* **date:** {self.pretty_date(date)}\n* **tags:** TBD\n---\n"""
        self.index_text += markdown
        if self.cp_start_date is None:
            self.cp_start_date = date
        self.index_end_date = date
        if self.index_count >= LINKS_PER_PAGE:
            self.save_index_page()
            self.start_index_page()

    def save_index_page(self):
        self.cp_number += 1
        filename = f'index-{self.cp_number}.md'
        page_text = (
            self.generate_index_page_title(
                self.cp_start_date, self.index_end_date
            )
            + '\n\n'
            + self.index_text
        )
        file_path = os.path.join(
            self.index_directory, self.sanitize_filename(filename)
        )
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(page_text)
        print(f'Saved {self.index_count} posts to {filename}')

    def generate_index_page_title(self, end_date, start_date):
        date_format = '%Y-%m-%d %H:%M:%S'
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        return f"### Links from {start.strftime("%b %d")} to {end.strftime("%b %d")}"

    def pretty_date(self, date):
        date_format = '%Y-%m-%d %H:%M:%S'
        date = datetime.strptime(date, date_format)
        return date.strftime('%b %d, %Y')

    def save_individual_post(self, title, content, date, tags):
        title = html.unescape(title)
        title = title.replace('"', '\\"')
        filename = f"{date}-{title.replace(' ', '-')}.md"
        file_path = os.path.join(
            self.posts_directory, self.sanitize_filename(filename)
        )
        with open(file_path, 'w', encoding='utf-8') as file:
            markdown = f"""---
title: "{title}"
author: Pito Salas
date: {date}{tags}
---
{content}
"""
            file.write(markdown)

    def sanitize_filename(self, filename):
        filename = re.sub(
            r'[\\/*?:"<>|]', '_', filename
        )  # Replace forbidden characters with underscore
        filename = re.sub(
            r'\s+', '-', filename.strip()
        )  # Replace spaces or consecutive spaces with dash
        return filename[:255]


# Main program
if __name__ == '__main__':
    wp_conv = WPImport()
    wp_conv.run()
    blog_gen = BlogGenerator()
    blog_gen.generate(wp_conv.posts, wp_conv.tags, wp_conv.drops)
    blog_gen.generate_drop_posts()

    print('done')
