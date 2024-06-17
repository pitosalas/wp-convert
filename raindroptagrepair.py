import os
from raindrop_utils import process_drops, retrieve_top_collection_id, setup_http_headers
from typing import Any, Dict


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
        process_drops(top_id, headers, self.process_drop: Callable[[dict[Any, Any]], Any])

    def process_drop(self, drop: dict[Any, Any]) -> Any:
        tags = self.get_tags_as_str_array(drop)
        tags = self.repair_tags(tags)
        tag_array = self.convert_tag_to_array(tags)
        # convert tags back to tag array
        self.update_drop(drop)
        pass

    def get_tags_as_str_array(self, drop):
        tag_array = []
        return tag_array
    
    def repair_tags(self, tags):
        pass

    def convert_tag_to_array(self, tags):
        pass

    def update_drop(self, drop):
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
