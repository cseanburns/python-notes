#!/usr/bin/env python3

# example basic web scraping

import requests
from bs4 import BeautifulSoup

#URL = "https://example.com/"
# from filesystem
with open("/var/www/") as home:
    soup = BeautifulSoup(home, "html.parser")

# span element with class="title"
book_titles = soup.find_all("span", class_="title")
print(book_titles)

# span element with class="title"
for title in soup.find_all('span', class_='title'):
    print(f'You read the book: {title.string}.')

# span element with class="author"
for author in soup.find_all('span', class_='author'):
    print(f'You read the following author: {author.string}.')
