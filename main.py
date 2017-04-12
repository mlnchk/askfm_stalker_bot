import requests
import json
from bs4 import BeautifulSoup

main_url = 'https://ask.fm'
url = 'https://ask.fm/id69938822'

r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)

html_doc = open('test.html', 'r')

soup = BeautifulSoup(html_doc, 'html.parser')

# questions = soup.findAll('div',{'class':'streamItemContent-question'})
# answers = soup.findAll('p',{'class':'streamItemContent-answer'})
#
# all = zip(questions, answers)
#
# qa_list = []

# for each_div, each_p in all:
#     x, y = str(each_div).find('<h2>') + 4, str(each_div).find('</h2>')
#     a, b = str(each_p).find('>') + 1, str(each_p).find('</p>')
    # temp = dict(question=str(each_div)[x:y], answer=str(each_p)[a:b])
    # qa_list.append(temp)
    # print(str(each_div)[x:y])
    # print('\t', str(each_p)[a:b], '\n')

# print(json.dumps(qa_list, sort_keys=False, indent=2, ensure_ascii=False))

answer = soup.findAll('div', {'class': 'streamItem-answer'})
# print(answer[0].find('div', {'class': 'streamItem-answer'}))

for i in range(len(answer)):
    print(answer[i].find('h2').get_text())
    if answer[i].find('p', {'class': 'streamItemContent-answer'}) is not None:
        print('\t', answer[i].find('p', {'class': 'streamItemContent-answer'}).get_text())
    else:
        print('\t no answer')

    if answer[i].find('div', {'class': 'streamItem-visualItem'}) is not None:

        print('\t', main_url + answer[i].find('div', {'class': 'streamItem-visualItem'}).find('a')['href'])
    else:
        print('\t no photo')
    print('\n')
