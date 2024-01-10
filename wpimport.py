import json
import requests

MAX_API_PAGES = 5

class WpImport:
    def __init__(self):
        self.posts = []

    def retrieve_posts(self):
        # Endpoint for the WordPress post API, replace with your WordPress site URL
        url = "http://www.salas.com/wp-json/wp/v2/posts"
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari'
        }
        current_page = 1
        total_pages = None
        while current_page != total_pages and current_page < MAX_API_PAGES:
            params = {'page': current_page}
            response = requests.get(url, headers=headers, params=params)
            total_pages = int(response.headers['X-WP-TotalPages'])
            current_page += 1
            self.process_posts(response, self.process_a_post)
            print(f"Retrieved {len(self.posts)} posts so far")
        return requests.get(url, headers=headers)

    def process_posts(self, response, action):
    # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json()
            for post in posts:
                self.posts.append(action(post))
        else:
            print("Failed to retrieve posts. Status code:", response.status_code)
            print(response.text)

    def process_a_post(self, post: dict) -> dict:
        post = self.drop_unneeded_keys(post)
        post = self.convert_values(post)
        return(post)
    
    def convert_values(self, post):
        return post
    
    def drop_unneeded_keys(self, post):
        post.pop('sticky', None)
        post.pop('template', None)
        post.pop('meta', None)
        post.pop('jetpack_sharing_enabled', None)
        post.pop('jetpack_featured_media_url', None)
        post.pop('_links', None)
        return post

    def save_posts(self):
        # save posts as a json file
        with open('data/wp_posts.json', 'w') as outfile:
            json.dump(self.posts, outfile)

    def run(self):
        self.retrieve_posts()
        self.save_posts()

# Main program
if __name__ == "__main__":
    wp_conv = WpImport()
    wp_conv.run()
    wp_conv.save_posts()
    print("done")




                    


