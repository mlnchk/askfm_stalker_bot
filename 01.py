import requests
import json
from bs4 import BeautifulSoup

url = 'https://ask.fm/id69938822/answers/poll'
# url = 'https://ask.fm/AlexandraPolyak/answers/poll'



def get_page(user_url):
    r = requests.get(user_url)
    with open('test.html', 'w') as output_file:
        output_file.write(r.text)


def make_qa_list(page):
    soup = BeautifulSoup(page, 'html.parser')
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


get_page(url)

qa = make_qa_list(open('test.html', 'r'))

tmp = json.load(open('qa.json', 'r'))

j = 0

for i in qa:
    if i != tmp[0]:
        j += 1
    else:
        break

print(j)

if j != 0:
    print('we have changes')
    for i in range(len(qa) - j):
        qa.pop()

    with open('qa.json', 'w', encoding='utf8') as file:
        json.dump(qa, file, ensure_ascii=False, indent=2, sort_keys=True)
else:
    print('no changes')

print('DONE')

