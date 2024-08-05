from flask import Flask, render_template, request, redirect, url_for
from news_fetcher import get_trending_news_headlines
from web_scraper import scrape_article_content
from summarizer import summarize_text
import spacy

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        language = request.form['language']
        from_date = request.form['from_date']
        to_date = request.form['to_date']

        headlines = get_trending_news_headlines(query, language, from_date, to_date)
        return render_template('index.html', headlines=headlines)

    return render_template('index.html', headlines=None)

@app.route('/summarize/<path:url>', methods=['GET'])
def summarize(url):
    content = scrape_article_content(url)
    if content:
        summary = summarize_text(content, nlp)
        return render_template('summary.html', summary=summary, url=url)
    else:
        return "Failed to fetch the article content."

if __name__ == "__main__":
    app.run(debug=True)
