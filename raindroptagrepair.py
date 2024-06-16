import os
from raindrop_utils import process_drops, retrieve_top_collection_id, setup_http_headers


class DropTagRepair:
    def __init(self):
        self.sec_token = os.getenv("RAINDROP_TOKEN")
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari',
            'Authorization': self.sec_token        
        }
        self.drops = {}
        self.topcolid = None

    def get_drops(self, top_id, headers):
        process_drops(top_id, headers, self.process_drop: Callable[[dict[any, any]], any])

    def process_drop(self, drop: dict[any, any]) -> any:
        return None
        pass

    def update_drop(self):
        pass

    def run(self):
        headers = setup_http_headers()
        top_id = retrieve_top_collection_id(headers)    
        self.get_drops(top_id, headers)

# Main program
if __name__ == "__main__":
    print("raindroptagrepair: start")
    masto = DropTagRepair()
    masto.run()
    print("raindroptagrepair: done")
