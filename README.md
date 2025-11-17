News Headline Scraper

This Python script scrapes top news headlines from BBC News using:

- requests
- BeautifulSoup

## How it works

1. Fetch HTML using a GET request  
2. Parse the page using BeautifulSoup  
3. Look for `<h2>` and `<h3>` tags  
4. Extract headlines  
5. Save all headlines into `headlines.txt`


## Files included
- news_scraper.py → Main script
- headlines.txt → Scraped output


