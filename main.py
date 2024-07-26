import requests
from newsapi import NewsApiClient
import json
from bs4 import BeautifulSoup
from transformers import pipeline

NEWS_API_KEY = '5db0e65032344d939c46fcf368f66cf4'

def get_trending_news_headlines(api_key):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us', 
        'apiKey': api_key,
        'sortBy': 'popularity',
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Failed to fetch headlines: {response.status_code}")
        return []
    
    articles = response.json().get('articles', [])
    headlines = [{'title': article['title'], 'url': article['url']} for article in articles]
    return headlines

def scrape_article_content(article_url):
  #Using beautiful soup to scrape the entire article content.
    response = requests.get(article_url)
    if response.status_code != 200:
        print(f"Failed to fetch article: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    paragraphs = soup.find_all('p')
    article_content = ' '.join([para.get_text() for para in paragraphs])

    return article_content


trending_headlines = get_trending_news_headlines(NEWS_API_KEY)

print("Trending News Headlines:")
counter = 0
for headline in trending_headlines:
  content  = scrape_article_content(headline['url'])
  if content:
    print(content) 
    counter+=1
    if counter>10:
      break