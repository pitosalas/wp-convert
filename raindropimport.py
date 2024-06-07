import csv
import json
from tagsimport import clean_tag

class RaindropImport:
    def __init__(self):
        self.drops = {}

    def retrieve_drops(self):
        with open('data/Library.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row['title']
                # Removing the name key-value pair as it's already used as a dictionary key
                del row['title']
                self.drops[key] = row

    def save_drops(self):
        with open('data/drops.json', 'w') as json_file:
            json.dump(self.drops, json_file)

    def clean_drops(self):
        for key in self.drops:
            self.drops[key]['tags'] = clean_tag(self.drops[key]['tags'])
                
    def run(self):
        self.retrieve_drops()
        self.clean_drops()
        self.save_drops()

# Main program
if __name__ == "__main__":
    wp_conv = RaindropImport()
    wp_conv.run()
    print("raindropimport: done")

                    


