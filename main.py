KEYWORDS = ['дизайн', 'фото', 'web', 'Анализ']

import requests
from bs4 import BeautifulSoup
from constants import HEADERS

url = 'https://habr.com/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
   hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
   hubs = [hub.text.strip() for hub in hubs]
   for hub in hubs:
      for k in KEYWORDS:
         if k in hub:
             href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
             full_href = f"{url}{href}"
             title = article.find("h2").find("span").text
             data = article.find("time").text
             print(f'{data} - {title} - {full_href}')


