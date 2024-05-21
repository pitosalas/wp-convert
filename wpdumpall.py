import json
import requests

MAX_API_PAGES = 10000
MAP = {
 "media":
    {
        "url": "http://lit.cfv.mybluehost.me/wp-json/wp/v2/media",
        "file": "data/wp_scan_media.json",
    },
        "posts":
    {
        "url": "http://lit.cfv.mybluehost.me/wp-json/wp/v2/posts",
        "file": "data/wp_scan_posts.json",
    },
        "pages":
    {
        "url": "http://lit.cfv.mybluehost.me/wp-json/wp/v2/pages",
        "file": "data/wp_scan_pages.json",
    },
        "categories":
        {
            "url": "http://lit.cfv.mybluehost.me/wp-json/wp/v2/categories",
            "file": "data/wp_scan_taxonomies.json",
        },
                    "tags":
        {
            "url": "http://lit.cfv.mybluehost.me/wp-json/wp/v2/tags",
            "file": "data/wp_scan_taxonomies.json",
        }

}

 
class WPGlobalDump:
    def __init__(self):
        self.results = {
            "posts": [],
            "pages": []
        }

    def gen_url(self, kind:str):
        return MAP[kind]["url"]
    
    def retrieve(self, kind: str):
        url = self.gen_url(kind)
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari'
        }
        current_page = 1
        total_pages = 50
        should_continue = True
        while should_continue and current_page < total_pages and current_page < MAX_API_PAGES:
            params = { "per_page": 100, "page": current_page }
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                break
            total_pages = int(response.headers['X-WP-TotalPages'])
            self.process_results(kind, response, self.process_a_result)
            print(f"Retrieved {len(self.results[kind])} {kind} so far")
            current_page += 1
        return requests.get(url, headers=headers)

    def process_results(self, kind, response, action):
        # Parse JSON response
        results = response.json()
        for result in results:
            self.results[kind].append(action(kind, result))

    def process_a_result(self, kind, result: dict) -> dict:
        if (kind == "posts"):
            result = self.drop_unneeded_keys(result)
        return(result)

    def drop_unneeded_keys(self, post):
        post.pop('sticky', None)
        post.pop('template', None)
        post.pop('meta', None)
        post.pop('jetpack_sharing_enabled', None)
        post.pop('jetpack_featured_media_url', None)
        post.pop('_links', None)
        return post

    def save_results(self, kind):
        with open(f'data/dump_{kind}_results.json', 'w') as outfile:
            json.dump(self.results[kind], outfile)

    def run(self):
        for kind in MAP.keys():
            try:
                self.results[kind] = []
                self.retrieve(kind)
                self.save_results(kind)
            except KeyError:
                print(f"Failed to retrieve {kind}")  
            self.save_results(kind)

# Main program
if __name__ == "__main__":
    global_dump = WPGlobalDump()
    global_dump.run()
    print("done")




                    


