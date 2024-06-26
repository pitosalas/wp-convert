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
    if drop["excerpt"] != "":
        content += f"""\n\n* **Web site excerpt:** {drop['excerpt']}\n"""
    return content


def fix_drop_tags(tags):
    if isinstance(tags, list):
        return tags
    ret_tag = re.split(", | |,", tags)
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
        with open("data/wp_tags.json") as json_file:
            self.tags = json.load(json_file)

    def retrieve_drops_from_file(self):
        with open("data/drops.json") as json_file:
            self.drops = json.load(json_file)

    def retrieve_api_drops_from_file(self):
        with open("data/api_drops.json") as json_file:
            self.drops = json.load(json_file)

    def retrieve_wp_posts_from_file(self):
        with open("data/wp_posts.json") as json_file:
            self.wp_posts = json.load(json_file)

    def retrieve_wp_pages_from_file(self):
        with open("data/wp_pages.json") as json_file:
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
                print(f"blogbuild_v2: Failed to copy {file_path}. Reason: {e}")
        print(f"""blogbuild_v2Total: {count} files copied""")

    def incorporate_original_pages(self):
        self.copy_all_files(ORIGINAL_PAGES_DIRECTORY, PAGES_DIRECTORY)

    def incorporate_original_posts(self):
        self.copy_all_files(ORIGINAL_POSTS_DIRECTORY, POSTS_DIRECTORY)

    def generate_wp_posts(self):
        count = 0
        for post in self.wp_posts:
            content = self.text_maker.handle(post["content"]["rendered"])
            title = post["title"]["rendered"]
            date = datetime.strptime(
                post["date"], "%Y-%m-%dT%H:%M:%S"
            ).strftime("%Y-%m-%d")
            if self.drops.get(title) is not None:
                print(
                    f"""blogbuild_v2: Skipping {title} because it is a drop"""
                )
                continue
            tags = self.tags_to_markdown(post["tags"])
            self.save_individual_post(title, content, date, tags, None, None, "")
            count += 1
        print(f"""blogbuild_v2: Total: {count} wp Posts Generated""")

    def generate_wp_pages(self):
        count = 0
        for post in self.wp_pages:
            content = self.text_maker.handle(post["content"]["rendered"])
            title = post["title"]["rendered"]
            date = datetime.strptime(
                post["date"], "%Y-%m-%dT%H:%M:%S"
            ).strftime("%Y-%m-%d")
            self.save_individual_page(title, content, date, None, None)
            count += 1
        print(f"""blogbuild_v2: Total: {count} wp Pages Generated""")

    def generate_drop_posts(self):
        """Generates drop posts based on the drops stored in the object. This method iterates over the drops stored in the object and generates drop posts
        by extracting the necessary information such as title, content, date, URL, cover,
        and tags. It then saves each individual drop post using the `save_individual_post`method.

        """
        count = 0
        for index, (drop_title, drop) in enumerate(self.drops.items()):
            title = drop_title
            content = self.fix_drop_content(drop)
            exerpt = drop["excerpt"]

            date = self.fix_drop_date(drop["created"])
            url = drop["url"]
            cover = drop["cover"]
            rawtags = self.fix_drop_tags(drop["tags"])
            if rawtags not in ["", "None", [""], []]:
                tags_str = """\ntags:"""
                for tag in rawtags:
                    if re.match(r"^\d+$", tag):
                        tag = "N" + tag
                        print(f"""blogbuild_v2: numerical {tag}""")
                    if re.match(r".*[,+.=:!'].*", tag) is not None:
                        print(f"""blogbuild_v2: invalid tag: {tag}""")
                        tag = "FOOBAR"
                    tags_str += f"""\n    - {tag}"""
            else:
                tags_str = ""
            self.save_individual_post(
                title, content, date, tags_str, url, cover, exerpt
            )
            count += 1
        print(f"""blogbuild_v2: total: {count} Drop Posts Generated""")

    def fix_drop_content(self, drop):
        """The fix_drop_content function takes a drop dictionary as input and
        extracts the 'note' field from it.

        If the 'excerpt' field is not empty, it appends it to the content with a
        formatted string. It then returns the content.

        """
        content = f"""{drop['note']}"""
        return content

    def fix_drop_tags(self, tags):
        """The fix_drop_tags function takes a parameter tags and checks if it is a
        list. If it is already a list, it returns it as is. If it is not a list, it splits the string using commas and spaces as delimiters and returns the resulting list. Additionally, if the split list is different from the
        original tags, it prints a message indicating the change.
        """
        if isinstance(tags, list):
            return tags
        ret_tag = re.split(", | |,", tags)
        if ret_tag != tags:
            print(f"""blogbuild_v2: {tags} -> {ret_tag}""")
        return ret_tag

    def fix_drop_date(self, date_string):
        """The fix_drop_date function takes a date string as input and converts
        it."""
        parsed_date = datetime.fromisoformat(date_string.rstrip("Z"))
        parsed_date.replace(tzinfo=None)
        return parsed_date.strftime("%Y-%m-%d")

    def tags_to_markdown(self, tags):
        """Given list of tag IDs as input and converts them into a markdown-
        formatted string.  It retrieves the corresponding tag text from a dictionary and appends it
        to the markdown string. If a tag fID does not have a corresponding tag
        text, it uses the string "none" instead. The function then returns the
        markdown string containing the tags.
        """
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

    def save_individual_post(self, title, content, date, tags, url, cover, excerpt) -> None:
        if cover is not None:
            cover_markdown = f"""<img class="cover" src="{cover}">\n"""
            cover_text = f"""\ncover: "{cover}" """
        else:
            cover_markdown = ""
            cover_text = ""
        url_text = "" if url is None else f"""\nurl: "{url}" """
        url_text += "" if url is None else f"""\nlink: "{url}" """
        title = html.unescape(title)
        title = title.replace('"', '\\"')
        file_path = os.path.join(
            POSTS_DIRECTORY,
            self.sanitize_filename(date, title),
        )
        link_markdown = "" if url is None else f"""**Link: [{title}]({url}):** "{excerpt}" """
        with open(file_path, "w", encoding="utf-8") as file:
            markdown = f"""---
title: "{title}"
author: Pito Salas{url_text}{cover_text}
date: {date}{tags}
---
{cover_markdown}
{link_markdown}

{content}
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
        file_path = os.path.join(
            PAGES_DIRECTORY, f"{title.replace(' ', '-')}.md"
        )
        with open(file_path, "w", encoding="utf-8") as file:
            markdown = f"""---
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
        filename = re.sub(
            r'[\\/*?:"<>|]', "-", filename
        )  # Replace forbidden characters with dash
        filename = re.sub(
            r"\s+", "", filename.strip()
        )  # Replace spaces or consecutive spaces with dash
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
                    print(
                        f"blogbuild_v2: Failed to delete {file_path}. Reason: {e}"
                    )
        else:
            # Create the directory if it doesn't exist
            os.makedirs(dir_path)

    def run(self) -> None:
        """
        Executes the main functionality of the blog builder.

        This method performs a series of steps to build a blog. It creates or empties the necessary directories,
        retrieves data from files, generates posts and pages, and incorporates original pages and posts.

        Returns:
            None
        """
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


# Main program
if __name__ == "__main__":
    print("blogbuild_v2: start")
    blog_build = BlogBuild()
    blog_build.run()
    print("blogbuild_v2: done")
