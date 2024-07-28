from news_fetcher import get_trending_news_headlines
from web_scraper import scrape_article_content
from summarizer import summarize_text
import spacy

def main():
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    trending_headlines = get_trending_news_headlines()

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

if __name__ == "__main__":
    main()
