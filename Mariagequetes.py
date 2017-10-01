import urllib
from BeautifulSoup import BeautifulSoup


topic_url = 'http://quotes.yourdictionary.com/theme/marriage/'
topic_html = urllib.urlopen(topic_url).read()
topic_soup = BeautifulSoup(topic_html)


quotes = topic_soup.findAll('p',limit=5, attrs={'class': 'quoteContent'})



import random

five_quotes = random.sample(quotes, 5)
for quote in five_quotes:
        print(quote.text + "\n")

