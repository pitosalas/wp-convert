import os
from raindrop_utils import process_drops, retrieve_top_collection_id, setup_http_headers
from typing import Any, Dict


class DropTagRepair:
    def process_drops(self, top_id, headers):
        self.process_drop(top_id, headers, self.process_drop)

    def process_drop(self, headers,top_id, drop): 
        tags = self.get_tags_as_str_array(drop)
        tags = self.repair_tags(tags)
        tag_array = self.convert_tag_to_array(tags)
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
        self.process_drops(top_id, headers)

# Main program
if __name__ == "__main__":
    print("raindroptagrepair: start")
    masto = DropTagRepair()
    masto.run()
    print("raindroptagrepair: done")
