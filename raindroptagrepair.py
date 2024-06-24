import json
import os
from raindrop_utils import *
from typing import Any, Dict

TAGS_PLAN_FILE = "data/tag_rules.json"
MAX_DROP_READ = 20000
MAX_TAG_REPAIR = 250

class DropTagRepair:

    def __init__(self):
        self.tags_repaired_count = 0

    def process_drop(self, drop) -> bool:
        tags_array = self.get_tags_as_str_array(drop)
        tags_repaired = self.repair_tags(tags_array)
        self.update_drop_tags(drop, tags_array, tags_repaired)
        print(f"Repaired count {self.tags_repaired_count}, max tag achieved? {self.tags_repaired_count >= MAX_TAG_REPAIR}")
        return self.tags_repaired_count < MAX_TAG_REPAIR

    def get_tags_as_str_array(self, drop):
        tag_array = drop['tags']
        return tag_array
    
    def repair_tags(self, tags):
        repaired_tags = []
        for index, tag in enumerate(tags):
            if tag not in self.tag_rules:
                self.tag_rules[tag] = None
                repaired_tags.append(tag)
            elif self.tag_rules[tag] == "delete":
                continue
            elif isinstance(self.tag_rules[tag], str):
                repaired_tags.append(self.tag_rules[tag])
            elif isinstance(self.tag_rules[tag], list):
                array_of_words = self.tag_rules[tag]
                repaired_tags.extend(array_of_words)
            else:
                array_of_words = self.multi_word_split(tag)
                repaired_tags.append(array_of_words)

        return self.flat_list(repaired_tags)

    def multi_word_split(self, tag: str) -> list[str]:
        return tag.split(" ")
    
    def read_rules_file(self, filename):
         with open(filename) as json_file:
            self.tag_rules = json.load(json_file)
    
    def save_rules_file(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.tag_rules, json_file)

    def convert_tag_to_array(self, tags):
        pass

    def flat_list(self, input_list):
        flat_list = []
        for item in input_list:
            if isinstance(item, list):
                flat_list.extend(item)
            else:
                flat_list.append(item)
        return flat_list

    def update_drop_tags(self, drop, original_tags, updated_tags):
        if original_tags == updated_tags:
            return
        self.tags_repaired_count += 1
        update_drop(self.headers, drop, updated_tags)
        print(f"Found {drop['title']}: \n    {original_tags} => \n    {updated_tags}")

    def run(self):
        self.headers = setup_raindrop_header()
        top_id = retrieve_top_collection_id(self.headers)
        self.read_rules_file(TAGS_PLAN_FILE)
        process_drops(top_id, self.headers, self.process_drop, MAX_DROP_READ)
        self.save_rules_file(TAGS_PLAN_FILE)

# Main program
if __name__ == "__main__":
    print("raindroptagrepair: start")
    masto = DropTagRepair()
    masto.run()
    print("raindroptagrepair: done")
