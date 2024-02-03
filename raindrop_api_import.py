import json
from time import sleep
import requests
import os
class RaindropApiImport:
    def __init__(self):
        self.sec_token = os.getenv("SECURITY_TOKEN")
        print(f"*********** Sec token: {self.sec_token}")
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari',
            'Authorization': SECURITY_TOKEN
            # 'Authorization': 'Bearer 9ca9524b-0342-43a4-b043-d0ab3569640b'
        
        }


        self.drops = {}
        self.topcolid = None

    def retrieve_top_collection_id(self):
        url = "https://api.raindrop.io/rest/v1/collections"
        response = requests.get(url, headers=self.headers)
        resp_json = response.json()['items'][0]
        self.topcolid = resp_json["_id"]


    def retrieve_drops(self):
        url = f"https://api.raindrop.io/rest/v1/raindrops/{self.topcolid}"
        page = 0
        drops = 0
        while True:
            params = { 'page': page }
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code != 200 or len(response.json()["items"]) == 0:
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
        self.retrieve_top_collection_id()
        self.retrieve_drops()
        self.save_drops()

# Main program
if __name__ == "__main__":
    rain = RaindropApiImport()
    rain.run()
    print("done")