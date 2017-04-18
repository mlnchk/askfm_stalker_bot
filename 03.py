import json
import requests
import time
from bs4 import BeautifulSoup

url = 'https://ask.fm/p1026425/answers/poll'

page = requests.get(url).text
# print(page)
soup = BeautifulSoup(page, 'html.parser')

answer = soup.find('a', {'id': 'newItemsReady'})

score = answer['data-poll-url']

print(score)