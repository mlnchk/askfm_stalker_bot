import json
import requests
import time
from bs4 import BeautifulSoup

url = 'https://ask.fm/p1026425/answers/poll'

def make_request(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def get_qa(soup):
    answer = soup.findAll('div', {'class': 'streamItem-answer'})
    qa_list = []
    for i in range(len(answer)):
        temp = dict(__question=answer[i].find('h2').get_text())
        if answer[i].find('p', {'class': 'streamItemContent-answer'}) is not None:
            temp['_answer'] = answer[i].find('p', {'class': 'streamItemContent-answer'}).get_text()

        if answer[i].find('div', {'class': 'streamItem-visualItem'}) is not None:
            temp['photo'] = answer[i].find('div', {'class': 'streamItem-visualItem'}).find('a')['data-url']
        qa_list.append(temp)
    return qa_list


def get_score(soup):
    answer = soup.find('a', {'id': 'newItemsReady'})
    score = answer['data-poll-url']
    return score

soup = make_request(url)
qa_dict = get_qa(soup)
print(json.dumps(qa_dict, indent=2))

new_url = 'https://ask.fm' + get_score(soup)

while True:
    new_request = requests.get(new_url)
    print(new_request)
    if new_request.status_code == 200:
        soup = make_request(new_url)
        new_qa_dict = get_qa(soup)
        new_url = 'https://ask.fm' + get_score(soup)
        qa_dict = get_qa(soup)
    time.sleep(30)