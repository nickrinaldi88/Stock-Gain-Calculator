# Build a web scraper that takes in stock ticker and displays current price.

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Build a web scraper
# find web scraper library
# Find finance/stock website that allows web scraping
# find search box and enter ticker. Or add ticker to url
# find element that holds price, store in text variable
# have text variable insert into purchasing price

ticker = 'GME'

url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'

# store webpage in variable

html = urlopen(url)

# convert webpage to soup object

soup = BeautifulSoup(html)

print(soup)

# soup find all  (span)
# soup gettext

# How to find a specific element in
