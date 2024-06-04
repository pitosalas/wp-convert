import json
from typing import Union
from blogbuild_v2 import fix_drop_date, fix_drop_tags
import requests
import re
import os
from typing import Union
import ext.slugs

MASTO_URL_FILE = "data/masto_url_list.json"
SAFE_MODE = True
MASTO_MAX_POST_PER_RUN = 3

JsonValue = Union[str, dict[str, str]]
class MastoPost:

    def __init__(self):
        self.sec_token: str = os.getenv("MASTO_TOKEN", "")

        if self.sec_token == "":
            raise ValueError("MASTO_TOKEN environment variable is not set")

        self.masto_urls: list[str] = []
        self.headers: dict[str, str] = {
            'Accept': 'application/json',
            'User-Agent': 'Safari',
            'Authorization': self.sec_token        
        }
        self.masto_post_count: int = 0

    def retrieve_api_drops_from_file(self) -> None:
        with open('data/api_drops.json') as json_file:
            self.drops: dict = json.load(json_file)

    def load_masto_url_file(self) -> None:
        if not os.path.exists(MASTO_URL_FILE):
            with open(MASTO_URL_FILE, "w") as json_file:
                json.dump({}, json_file)
                self.masto_urls: list[str] = []
        with open(MASTO_URL_FILE) as json_file:
            loaded_file: dict = json.load(json_file)
            self.masto_urls: list[str] = loaded_file.get("urls", [])
            
    def save_masto_url_file(self):
        if SAFE_MODE:
            return
        with open(MASTO_URL_FILE, "w") as json_file:
            urls_dict = {"urls" : self.masto_urls}
            json.dump(urls_dict, json_file, indent=4)

    def fix_drop_content(self, drop):
        content = f"""{drop['note']}"""
        return content

    def write_api_drops_to_masto(self):
        count = 0
        for index, (drop_title, drop) in enumerate(self.drops.items()):
            # print(f"Processing {count} {drop_title}")
            if count > 10:
                count += 1
                continue
            title = drop_title
            content = self.fix_drop_content(drop)
            date = fix_drop_date(drop['created'])
            url = drop['url']
            tags_str: str = ""
            cover = drop['cover']
            rawtags = fix_drop_tags(drop['tags'])
            if rawtags not in ['', 'None', [''], []]:
                tags_str = ""
                for tag in rawtags:
                    tags_str += f"""#{tag} """
            else:
                tags_str = ""
            self.create_masto_post(title, content, date, tags_str, url, cover)
            count += 1
        print(f"""Total: {count} Drop Posts Generated""")

    def get_slug(self, title: str, date_str: str):
        slug = ext.slugs._make_slug_short(title, "-", kwargs={'short' : True})
        url_with_slug = f"https://www.salas.com/{date_str}/{slug}"
        return url_with_slug
    def create_masto_post(self, title: str, content: str, date: str, tags_str: str, url: str, cover: str) -> None:
        if url in self.masto_urls or self.masto_post_count >= MASTO_MAX_POST_PER_RUN:
            return
        rest_url: str = "https://ruby.social/api/v1/statuses"
        status: str = f"""{content} {tags_str}: "{title}"({url})"""
        url_with_slug = self.get_slug(title, date)
        print(url_with_slug)
        json_data_dict: dict[str, JsonValue] = {"status": status, "links": url_with_slug}
        if SAFE_MODE:
            print(f"fake posting {json_data_dict}")
            self.masto_urls.append(url)
        else:
            response = requests.post(rest_url, headers=self.headers, data=json_data_dict)
            if response.status_code == 200:
                self.masto_urls.append(url)
                self.masto_post_count += 1
                print(f"successful posting {json_data_dict}")


    def run(self):
        self.retrieve_api_drops_from_file()
        self.load_masto_url_file()
        self.write_api_drops_to_masto()
        self.save_masto_url_file()       

# Main program
if __name__ == "__main__":
    masto = MastoPost()
    masto.run()
    print("done")
