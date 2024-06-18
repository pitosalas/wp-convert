import os
from raindrop_utils import process_drops, retrieve_top_collection_id, setup_raindrop_header
from typing import Any, Dict

class DropTagRepair:
    def process_drop(self, drop): 
        tags_array = self.get_tags_as_str_array(drop)
        tags_repaired = self.repair_tags(tags_array)
        self.update_drop_tags(drop, tags_repaired)
        pass

    def get_tags_as_str_array(self, drop):
        tag_array = drop['tags']
        return tag_array
    
    def repair_tags(self, tags):
        pass

    def convert_tag_to_array(self, tags):
        pass

    def update_drop_tags(self, drop, tags):
        pass

    def run(self):
        headers = setup_raindrop_header()
        top_id = retrieve_top_collection_id(headers)    
        process_drops(top_id, headers, self.process_drop)

# Main program
if __name__ == "__main__":
    print("raindroptagrepair: start")
    masto = DropTagRepair()
    masto.run()
    print("raindroptagrepair: done")
