import requests
from bs4 import BeautifulSoup

def scrape_article_content(article_url):
    response = requests.get(article_url)
    if response.status_code != 200:
        print(f"Failed to fetch article: {response.status_code}, try after 24 hours")
        # Error 401 because for free plan articles have 24 hour delay.
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_content = ' '.join([para.get_text() for para in paragraphs])
    return article_content
