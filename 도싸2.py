import requests
from bs4 import BeautifulSoup

# Base URL for Dossa homepage
base_url = "https://www.corearoadbike.com/board/board.php?g_id=recycle02&t_id=Menu01Top6&category=%ED%8C%90%EB%A7%A4&page="

# Function to crawl titles from a specific page
def crawl_titles(page_number):
    url = base_url + str(page_number)
    response = requests.get(url)
    print(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.select('td', attrs={'class':'list_title_B'})
        
        for post in posts:
            title = post.text.strip()
            print(title)
    else:
        print("Failed to retrieve the page.")

# Crawl titles up to page 100
for page_num in range(1, 10):
    print(f"Page {page_num}:")
    crawl_titles(page_num)
    print("\n")