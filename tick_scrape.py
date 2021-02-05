# Build a web scraper that takes in stock ticker and displays current price.

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Build a web scraper
# find web scraper library
# Find finance/stock website that allows web scraping
# find search box and enter ticker. Or add ticker to url
# find element that holds price, store in text variable
# have text variable insert into purchasing price


def scrape():

    ticker = 'GME'

    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'

    # store webpage in variable

    html = urlopen(url)

    # convert webpage to soup object

    soup = BeautifulSoup(html, 'html.parser')

    price = soup.find(
        'span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})

    print(price.get_text())

# soup find all  (span)
# soup gettext

# How to find a specific element in
