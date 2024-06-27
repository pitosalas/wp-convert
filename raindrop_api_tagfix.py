import json
from time import sleep
import requests
import os
from raindrop_utils import (
    retrieve_top_collection_id as retrieve_top_collection_id,
)


class RaindropApiImport:
    def __init__(self):
        self.sec_token = os.getenv('RAINDROP_TOKEN')
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari',
            'Authorization': self.sec_token,
        }
        self.drops = {}
        self.topcolid = None

    def retrieve_tags(self, top_id):
        url = f'https://api.raindrop.io/rest/v1/tags/{top_id}'
        while True:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print(f"""Breaking loop because: {response.status_code}""")
                break
            sleep(0.25)
            for tag in response.json()['items']:
                if tag['count'] <= 3:
                    print(tag)
            break

    def retrieve_drops(self, top_id):
        url = f'https://api.raindrop.io/rest/v1/raindrops/{top_id}'
        page = 0
        drops = 0
        while True:
            params = {'page': page}
            response = requests.get(url, headers=self.headers, params=params)
            if (
                response.status_code != 200
                or len(response.json()['items']) == 0
            ):
                print(f"""Breaking loop because: {response.status_code}""")
                break
            sleep(0.25)
            page += 1
            for drop in response.json()['items']:
                drops += 1
                key = drop['title']
                drop['url'] = drop['link']
                # Removing the name key-value pair as it's already used as a dictionary key
                del drop['title']
                self.drops[key] = drop
            print(f"""Page: {page} drop: {drops} retrieved""")

    def save_drops(self):
        with open('data/api_drops.json', 'w') as json_file:
            json.dump(self.drops, json_file)

    def run(self):
        top_id = retrieve_top_collection_id(self.headers)
        # self.retrieve_tags(top_id)
        self.retrieve_drops(top_id)


# Main program
if __name__ == '__main__':
    rain = RaindropApiImport()
    rain.run()
    print('done')
