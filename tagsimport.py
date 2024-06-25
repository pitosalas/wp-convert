# Tagsimport is a script that retrieves tags from a wordpress site and saves them
# as a json file. The tags are cleaned up by removing special characters, changing
# spaces to dashes and more.

import json
import requests
import re

MAX_TAG_API_PAGES = 1000000
TAG_EXCLUDE_WORDS = ["yes", "on", "off", "no", "none", "true", "false"]
TAG_EXCLUDE_CHARACTERS = r"[,+.=:!']"
OUTPUT_FILE = "data/wp_tags.json"

def clean_tag(tag):
    """delete special characeters, change space to dash, detect excluded
    words and add "tag-" prefix.
    """
    outtag = re.sub(TAG_EXCLUDE_CHARACTERS, "", tag)
    if " " in outtag:
        outtag = re.sub("\\s", "-", outtag)
    for word in TAG_EXCLUDE_WORDS:
        outtag = outtag.replace(word, word+"-tag")
    outtag = handle_weird_special_cases(outtag)
    return outtag

def handle_weird_special_cases(s):
    if s == "007":
        return "Bond-007"
    elif s == "1969":
        return "year-1969"
    else:
        return s

class TagsImport:
    def __init__(self):
        self.tags = {}

    def retrieve_tags(self):
        url = "https://lit.cfv.mybluehost.me/wp-json/wp/v2/tags"
        headers = {"Accept": "application/json", "User-Agent": "Safari"}
        current_page = 1
        total_pages = None
        while current_page != total_pages and current_page < MAX_TAG_API_PAGES:
            params = {"page": current_page}
            response = requests.get(url, headers=headers, params=params)
            total_pages = int(response.headers["X-WP-TotalPages"])
            current_page += 1
            self.process_tags(response, self.process_a_tag)
        return requests.get(url, headers=headers)

    def process_tags(self, response, action):
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            tags = response.json()
            for tag in tags:
                action(tag)
        else:
            print("raindropimport: Failed to retrieve tags. Status code:", response.status_code)

    def process_a_tag(self, tag):
        self.tags[tag["id"]] = clean_tag(tag["name"])


    def save_tags(self):
        # save tags as a json file
        with open(OUTPUT_FILE, "w") as outfile:
            json.dump(self.tags, outfile)

    def run(self):
        self.retrieve_tags()
        self.save_tags()


# Main program
if __name__ == "__main__":
    wp_conv = TagsImport()
    wp_conv.run()
    print("raindropimport: done")
