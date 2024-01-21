import json
import requests

MAX_API_PAGES = 10000

class WpImport:
    def __init__(self):
        self.posts = []
        self.pages = []

    def retrieve_posts(self):
        # Endpoint for the WordPress post API, replace with your WordPress site URL
        url = "http://www.salas.com/wp-json/wp/v2/posts"
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari'
        }
        current_page = 1
        total_pages = 10000
        should_continue = True
        while should_continue and current_page < total_pages and current_page < MAX_API_PAGES:
            params = {'page': current_page}
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                break
            total_pages = int(response.headers['X-WP-TotalPages'])
            self.process_posts(response, self.process_a_post)
            current_page += 1
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
            print("Failed to retrieve post. Status code:", response.status_code)
            print(response.text)

    def process_a_post(self, post: dict) -> dict:
        post = self.drop_unneeded_keys(post)
        return(post)


    def retrieve_pages(self):
        # Endpoint for the WordPress post API, replace with your WordPress site URL
        url = "http://www.salas.com/wp-json/wp/v2/pages"
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Safari'
        }
        current_page = 1
        total_pages = 10000
        should_continue = True
        while should_continue and current_page < total_pages and current_page < MAX_API_PAGES:
            params = {'page': current_page}
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                break

            total_pages = int(response.headers['X-WP-TotalPages'])
            self.process_pages(response, self.process_a_page)
            print(f"Retrieved {len(self.posts)} pages so far")
            current_page += 1
        return requests.get(url, headers=headers)

    def process_pages(self, response, action):
    # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json()
            for post in posts:
                self.pages.append(action(post))
        else:
            print("Failed to retrieve page. Status code:", response.status_code)
            print(response.text)

    def process_a_page(self, post: dict) -> dict:
        page = self.drop_unneeded_keys(post)
        return(page)

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

    def save_pages(self):
        # save posts as a json file
        with open('data/wp_pages.json', 'w') as outfile:
            json.dump(self.pages, outfile)

    def run(self):
        self.retrieve_posts()
        self.save_posts()
        self.retrieve_pages()
        self.save_pages()

# Main program
if __name__ == "__main__":
    wp_conv = WpImport()
    wp_conv.run()
    print("done")




                    


