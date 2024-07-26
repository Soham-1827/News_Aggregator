import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import spacy
NEWS_API_KEY = '5db0e65032344d939c46fcf368f66cf4'


def get_trending_news_headlines(api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'apple',
        'language': 'en',
        'apiKey': api_key,
        'from': '2024-07-23',
        'to': '2024-07-23',
        'sortBy': 'popularity',
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch headlines: {response.status_code}, {response.text}")
        return []

    print(f"API Response: {response.json()}")  # Debugging: print the entire response

    articles = response.json().get('articles', [])
    headlines = [{'title': article['title'], 'url': article['url'], 'publishedAt': article['publishedAt']} for article in articles]
    return headlines


def scrape_article_content(article_url):
    response = requests.get(article_url)
    if response.status_code != 200:
        print(f"Failed to fetch article: {response.status_code}, try after 24 hours")
        #Error 401 because for free plan articles have 24 hour delay.
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_content = ' '.join([para.get_text() for para in paragraphs])
    return article_content


def summarize_text(text, nlp, num_sentences=3):
    doc = nlp(text)
    sentences = [sent for sent in doc.sents]
    sentence_scores = {}

    for sent in sentences:
        for word in sent:
            if word.text.lower() not in nlp.Defaults.stop_words and word.is_alpha:
                if sent in sentence_scores:
                    sentence_scores[sent] += 1
                else:
                    sentence_scores[sent] = 1

    # Get the highest scored sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join([str(sent) for sent in summarized_sentences])
    return summary


# Load spaCy model
nlp = spacy.load("en_core_web_sm")
trending_headlines = get_trending_news_headlines(NEWS_API_KEY)

if trending_headlines:
    print("Trending News Headlines:")
    counter = 0
    for headline in trending_headlines:
        print(f"Fetching content for: {headline['title']}")
        print(headline['publishedAt'])
        print(headline['url'] + '\n')
        content = scrape_article_content(headline['url'])
        if content:
            summary = summarize_text(content, nlp)
            print("Summary:")
            for bullet_point in summary.split('.'):
                print(f" - {bullet_point.strip()}.")
            counter += 1
            if counter >= 10:
                break
else:
    print("No trending headlines found.")
