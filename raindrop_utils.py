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

def update_drop(headers, drop, updated_tags):
    id = drop["_id"]
    url = f"https://api.raindrop.io/rest/v1/raindrop/{id}"
    params = { 'tags': updated_tags}
    response = requests.put(url, headers=headers, json=params)
    if response.status_code != 200:
        raise RuntimeError(f"update drop failed with {response.status_code}")
        

def process_drops(top_id, headers, process_drop: Callable[[dict[Any, Any]], bool], max_drop):
    url = f"https://api.raindrop.io/rest/v1/raindrops/{top_id}"
    page = 0
    drops = 0
    status = True
    while (drops < max_drop) and status:
        print(f"Processing page {page}, drops {drops}, status {status}")
        params = { 'page': page }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200 or len(response.json()["items"]) == 0:
            print(f"""Breaking loop because: {response.status_code}""")
            break
        sleep(2)
        page += 1
        for drop in response.json()['items']:
            drops += 1
            status = process_drop(drop)
