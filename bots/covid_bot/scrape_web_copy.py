# import urllib2
from bs4 import BeautifulSoup
import requests
import re
import json
quote_page ="https://www.cdc.gov/coronavirus/2019-ncov/faq.html"
page = requests.get(quote_page)
soup = BeautifulSoup(page.text, 'html.parser')
questions=[]  # a list to store quotes 
from scrape_web import faq_dict_nig
table = soup.findAll('div', attrs = {'class':"card card-accordion"})
# for row in table:
answers= []
questions=[]

for row in table:
    answers_blk = row.findAll('div',attrs ={"class":"card-body"})
    questions_blk = row.findAll('div',attrs={'class':"card-header"})
    for element in answers_blk:
        answer =element.text
        answers.append(answer)
    for element in questions_blk:
        question = element.text
        questions.append(question)
print(len(answers))
print(len(questions))

# dirty = ["\u2019", "\u2019s","\u2019t", '\u00a0', '\u201d', '\n']
# for dirt in dirty: 
#     questions_clean= [re.sub(dirt, ' ', question) for question in questions]
#     answers_clean= [re.sub(dirt, ' ', question) for question in answers]
# questions_clean= [re.sub("\u2019| \u2019s |\u2019t | \u00a0 |\u201d| \n', ' ', question) for question in questions]
# answers_clean= [re.sub(dirt, ' ', question) for question in answers]
faq_dict= dict(zip(questions, answers))
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
faq_combine = Merge(faq_dict, faq_dict_nig) 
# print(len(faq_combine))
with open('faq1.json', 'w') as json_file:
  json.dump(faq_combine, json_file)


  storage_vm_bucket