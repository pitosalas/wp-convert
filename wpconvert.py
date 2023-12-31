import os
import requests
import html2text
import re
from datetime import datetime


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

    def generate(self, posts):
    # Ensure the '_posts' directory exists
        self.directory = "links"
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.cp_number = 0
        self.start_aggregate_page()
        for post in posts:
            content = self.text_maker.handle(post['content'])
            title = post['title']
            date = post['date']
            self.add_post_to_aggregate_page(title, content, date)
            self.save_individual_post(title, content, date)

    def start_aggregate_page(self):
        self.cp_count = 0
        self.cp_text = ""
        self.cp_start_date = None
        self.cp_end_date = None

    def add_post_to_aggregate_page(self, title, content, date):
        self.cp_count += 1
        markdown = f"""### {title}\n{content}\n---\n"""
        self.cp_text += markdown
        if self.cp_start_date is None:
            self.cp_start_date = date
        self.cp_end_date = date
        if self.cp_count == 10:
            self.save_aggregate_page()
            self.start_aggregate_page()

    def save_aggregate_page(self):
        self.cp_number += 1
        filename = f"links-{self.cp_number}.md"
        page_text = self.generate_page_title(self.cp_start_date, self.cp_end_date) + "\n\n" + self.cp_text
        file_path = os.path.join(self.directory, self.sanitize_filename(filename))
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(page_text)
        print(f"Saved {self.cp_count} posts to {filename}")

    def generate_page_title(self, end_date, start_date):
        date_format = "%Y-%m-%d %H:%M:%S"
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        return f"## My link blog, from {start.strftime("%b %d")} to {end.strftime("%b %d")}"

    def save_individual_post(self, title, content, date):
        filename = f"{date}-{title.replace(' ', '-')}.md"
        file_path = os.path.join(self.directory, self.sanitize_filename(filename))
        with open(file_path, 'w', encoding='utf-8') as file:
            markdown = f"""### {title}\n{content}"""
            file.write(markdown)

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

                    


