import requests
from bs4 import BeautifulSoup

def count_posts_with_title(url, title):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the specified title
        posts = soup.find_all('a', class_='article')
        matching_posts = [post for post in posts if post.get_text(strip=True) == title]

        # Return the count of matching posts
        return len(matching_posts)
    
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return 0

# URL of the Joonggonara page
joonggonara_url = "https://cafe.naver.com/joonggonara"

# Title to search for
search_title = "tcr"

# Get the count of posts with the specified title
post_count = count_posts_with_title(joonggonara_url, search_title)

# Display the result
print(f'The number of posts with the title "{search_title}" on Joonggonara is: {post_count}')
