import json
from blogbuild_v2 import fix_drop_date, fix_drop_tags
import requests
import re
import os

MASTO_URL_FILE = "data/masto_url_list.json"

class MastoPost:

    def __init__(self):
        self.sec_token = os.getenv("MASTO_TOKEN")
        self.masto_urls : list[str] = []
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari',
            'Authorization': self.sec_token        
        }

    def retrieve_api_drops_from_file(self) -> None:
        with open('data/api_drops.json') as json_file:
            self.drops = json.load(json_file)

    def load_masto_url_file(self) -> None:
        if not os.path.exists(MASTO_URL_FILE):
            with open(MASTO_URL_FILE, "w") as json_file:
                json.dump({}, json_file)
                self.masto_urls = []
        with open(MASTO_URL_FILE) as json_file:
            loaded_file = json.load(json_file)
            self.masto_urls = loaded_file.get("urls", [])
            
    def save_masto_url_file(self):
        with open(MASTO_URL_FILE, "w") as json_file:
            urls_dict = {"urls" : self.masto_urls}
            json.dump(urls_dict, json_file, indent=4)

    def fix_drop_content(self, drop):
        content = f"""{drop['note']}"""
        return content

    def write_api_drops_to_masto(self):
        count = 0
        for index, (drop_title, drop) in enumerate(self.drops.items()):
            if count > 1:
                count += 1
            title = drop_title
            content = self.fix_drop_content(drop)
            date = fix_drop_date(drop['created'])
            url = drop['url']
            tags_str: str = ""
            cover = drop['cover']
            rawtags = fix_drop_tags(drop['tags'])
            if rawtags not in ['', 'None', [''], []]:
                tags_str = """"""
                for tag in rawtags:
                    tags_str += f"""#{tag} """
            else:
                tags_str = ""
            self.create_masto_post(title, content, date, tags_str, url, cover)
            count += 1
        print(f"""Total: {count} Drop Posts Generated""")

    def create_masto_post(self, title, content, date, tags_str, url, cover):
        if url in self.masto_urls:
            return
        rest_url = "https://ruby.social/api/v1/statuses"
        status = f"""{content} {tags_str}: "{title}"({url})"""
        json_data_dict = { "status" : status, "links" : url }
        response = requests.post(rest_url, headers=self.headers, data=json_data_dict)
        if response.status_code == 200:
            self.masto_urls.append(url)

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
