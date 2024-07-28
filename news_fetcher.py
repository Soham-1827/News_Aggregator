import requests
from config import NEWS_API_KEY
import datetime

def get_user_parameters():
    parameters = []

    query = input("What is the query?\n")
    if isinstance(query.lower(), str) and query != "":
        parameters.append(query)

    language = input("What is the language?\n")
    if isinstance(language.lower(), str) and language != "":
        parameters.append(language)

    print("News from this date: ")
    from_date = get_dates()
    if isinstance(from_date, str):
        parameters.append(from_date)

    print("News to this date: ")
    to_date = get_dates()
    if isinstance(to_date, str):
        parameters.append(to_date)

    return parameters
def get_dates():
    year = int(input('Enter a year\n'))
    month = int(input('Enter a month\n'))
    day = int(input('Enter a day\n'))
    date1 = str(datetime.date(year, month, day))
    return date1

def get_trending_news_headlines():
    parameter_list = get_user_parameters()
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': parameter_list[0],
        'language': parameter_list[1].strip(),
        'apiKey': NEWS_API_KEY,
        'from': parameter_list[2],
        'to': parameter_list[3],
        'sortBy': 'popularity',
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch headlines: {response.status_code}, {response.text}")
        return []

    articles = response.json().get('articles', [])
    headlines = [{'title': article['title'], 'url': article['url'], 'publishedAt': article['publishedAt']} for article in articles]
    return headlines