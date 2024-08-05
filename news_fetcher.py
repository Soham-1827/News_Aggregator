import requests
from config import NEWS_API_KEY

def get_trending_news_headlines(query, language, from_date, to_date):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'language': language.strip(),
        'apiKey': NEWS_API_KEY,
        'from': from_date,
        'to': to_date,
        'sortBy': 'popularity',
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch headlines: {response.status_code}, {response.text}")
        return []

    articles = response.json().get('articles', [])
    headlines = [{'title': article['title'], 'url': article['url']} for article in articles]
    return headlines
