import json
from typing import Union
from blogbuild_v2 import fix_drop_date, fix_drop_tags
import requests
import re
import os
from typing import Union
import ext.slugs

MASTO_URL_FILE = "data/masto_url_list.json"
SAFE_MODE = False
MASTO_MAX_POST_PER_RUN = 1

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
            if count > 5:
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
        print(f"""masto_post {count} Drop Posts Processed""")

    def get_salas_url_with_slug(self, title: str, date_str: str):
        slug = ext.slugs._make_slug_short(title, "-", kwargs={'short' : True})
        date_str = date_str.replace("-", "/")
        url_with_slug = f"https://salas.com/{date_str}/{slug}/"
        return url_with_slug
    
    def create_masto_post(self, title: str, content: str, date: str, tags_str: str, url: str, cover: str) -> None:
        if url in self.masto_urls or self.masto_post_count >= MASTO_MAX_POST_PER_RUN:
            print(f"""masto_post: maximum masto statuses reached: {self.masto_post_count}""")
            return
        rest_url: str = "https://ruby.social/api/v1/statuses"
        salas_url_with_slug = self.get_salas_url_with_slug(title, date)
        status: str = f"""{content} {tags_str} {salas_url_with_slug}: from: "{title}"({url})"""
        json_data_dict: dict[str, JsonValue] = {"status": status}
        self.masto_post_count += 1
        if SAFE_MODE:
            print(f"masto_post: fake mode posting {json_data_dict}")
        else:
            response = requests.post(rest_url, headers=self.headers, data=json_data_dict)
            if response.status_code == 200:
                self.masto_urls.append(url)
                print(f"masto_post: successful posting {json_data_dict}")

    def run(self):
        self.retrieve_api_drops_from_file()
        self.load_masto_url_file()
        self.write_api_drops_to_masto()
        self.save_masto_url_file()       

# Main program
if __name__ == "__main__":
    print("masto_post: start")
    masto = MastoPost()
    masto.run()
    print("masto_post: done")
