import json
import os
import requests
import html2text
import re
from datetime import datetime

MAX_TAG_API_PAGES = 1000000
class TagsImport:
    def __init__(self):
        self.tags = {}

    def retrieve_tags(self):
        url = "http://www.salas.com/wp-json/wp/v2/tags"
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari'
        }
        current_page = 1
        total_pages = None
        while current_page != total_pages and current_page < MAX_TAG_API_PAGES:
            params = {'page': current_page}
            response = requests.get(url, headers=headers, params=params)
            total_pages = int(response.headers['X-WP-TotalPages'])
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
            print("Failed to retrieve tags. Status code:", response.status_code)
            print(response.text)
    
    def process_a_tag(self, tag):
        self.tags[tag['id']] = tag['name']

    def save_tags(self):
        # save tags as a json file
        with open('tags.json', 'w') as outfile:
            json.dump(self.tags, outfile)
            
    def run(self):
        self.retrieve_tags()
        self.save_tags()
# Main program
if __name__ == "__main__":
    wp_conv = TagsImport()
    wp_conv.run()
    print("done")

                    


