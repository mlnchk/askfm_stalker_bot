import json
import requests
import time
from bs4 import BeautifulSoup


main_url = 'https://ask.fm'

# url = 'https://ask.fm/id69938822/answers/poll'
url = 'https://ask.fm/p1026425/answers/poll'
# url = 'https://ask.fm/p1026425/answers/poll?counter=0'
# url = 'https://ask.fm/id69938822/answers/poll?score=1492197465&counter=0'

# payload = {'score': '1492197465', 'counter': '0'}


r = requests.get(url=url)
print(r)
print(r.text)
text = r.text
# print(text)

with open('test2.html', 'w') as output_file:
    output_file.write(r.text)

page = open('test2.html', 'r')

soup = BeautifulSoup(page, 'html.parser')

answer = soup.find('a', {'id': 'newItemsReady'})
score = answer['data-poll-url']

a = score.rfind('score=')

print(score)

r = requests.get(url=main_url+score)
while r.status_code == 204:
    r = requests.get(url=url, params={'score': int(score[a + 6:])})
    print(r)
    print(r.text)
    time.sleep(30)
