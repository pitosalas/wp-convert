import os
import requests
import html2text
import re


MAX_API_PAGES = 3

class WPConvert:
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

    def process_a_post(self, post) -> dict:
       result = {"title": post['title']['rendered'], "content": post['content']['rendered'],
                 "date": post['date'].replace('T', ' ').replace('Z', ''), "slug": post['slug']}
       return result

    def run(self):
        response = self.retrieve_posts()
        self.process_posts(response, self.process_a_post)


class BlogGenerator:
    def __init__(self):
        self.text_maker = html2text.HTML2Text()
        self.text_maker.protect_links = True

        pass

    def generate(self, posts):
    # Ensure the '_posts' directory exists
        directory = "links"
        if not os.path.exists(directory):
            os.makedirs(directory)

        for post in posts:
            content = self.text_maker.handle(post['content'])
            filename = f"{post['date']}-{post['title'].replace(' ', '-')}.md"
            file_path = os.path.join(directory, self.sanitize_filename(filename))
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

    def sanitize_filename(self, filename):
        filename = re.sub(r'[\\/*?:"<>|]', "_", filename)  # Replace forbidden characters with underscore
        filename = re.sub(r'\s+', '-', filename.strip())   # Replace spaces or consecutive spaces with dash
        return filename[:255]


            
# Main program
if __name__ == "__main__":
    wp_conv = WPConvert()
    wp_conv.run()
    blog_gen = BlogGenerator()
    blog_gen.generate(wp_conv.posts)
    
    print("done")

                    


