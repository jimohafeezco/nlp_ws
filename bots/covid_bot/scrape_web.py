# import urllib2
from bs4 import BeautifulSoup
import requests
import re
import json
quote_page ="https://covid19.ncdc.gov.ng/faq/"
page = requests.get(quote_page)
soup = BeautifulSoup(page.text, 'html.parser')
questions=[]  # a list to store quotes 
   
table = soup.find('div', attrs = {'class':'accordion'}) 
   
for row in table.findAll(attrs = {'class':'mb-0'}): 
    question = row.text
    # print(content.text)
    questions.append(question)
print(len(questions))
questions_clean= [re.sub("\n", '', question) for question in questions]

answers = []

for row in table.findAll(attrs = {'class':'card-body'}): 
    question = row.text
    # print(content.text)
    answers.append(question)
# print(len(answers))
answers_clean = [re.sub("\n",  '', answer) for answer in answers]
faq_dict_nig= dict(zip(questions_clean, answers_clean))
# print(faq)
# faq = json.dumps(faq_dict)
# print(faq)


with open('faq.json', 'w') as json_file:
  json.dump(faq_dict_nig, json_file)