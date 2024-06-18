from time import sleep
from typing import Any, Dict, Callable
import os

import requests

def setup_raindrop_header():
    sec_token = str(os.getenv("RAINDROP_TOKEN"))
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Safari',
        'Authorization': "Bearer " + sec_token        
    }
    return headers

def retrieve_top_collection_id(headers):
    url = "https://api.raindrop.io/rest/v1/collections"
    response = requests.get(url, headers=headers)
    resp_json = response.json()['items'][0]
    return resp_json["_id"]

def process_drops(top_id, headers, process_drop: Callable[[dict[Any, Any]], Any]):
    url = f"https://api.raindrop.io/rest/v1/raindrops/{top_id}"
    page = 0
    drops = 0
    while True:
        params = { 'page': page }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200 or len(response.json()["items"]) == 0:
            print(f"""Breaking loop because: {response.status_code}""")
            break
        sleep(0.25)
        page += 1
        for drop in response.json()['items']:
            drops += 1
            process_drop(drop)
