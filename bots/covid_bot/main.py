import json
from collections import Counter
import spacy
from numpy import argsort, argmax
word2vec = spacy.load('en')

from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity

with open("faq1.json") as json_file:
    faq = json.load(json_file)
questions = list(faq.keys())
exit_commands = ("quit", "goodbye", "exit", "no")

# print(questions)
class ChatBot:
  def make_exist(self, user_message):
    for command in exit_commands:
      if command in user_message:
        print("goodbye")
        return True

  def find_intent_match(self, questions, user_message):
    bow_user_message = Counter(preprocess(user_message))
    processed_questions = [Counter(preprocess(question)) for question in questions]
    # define similarity_list here:
    similarity_list = [compare_overlap(bow_user_message, question) for question in processed_questions]
    # define response_index here:
    response_index= similarity_list.index(max(similarity_list))
    return faq[questions[response_index]]

  def respond(self, user_message):
    best_response= self.find_intent_match(questions, user_message)
    # entity =self.find_entities(user_message)
    # print(best_response)
    return best_response
    
  def chat(self, user_message):

    # user_message = input("Hi, I'm Stratus. Ask me about covid!\n")
    # for command in exit_commands:
    #     if command in user_message:
    #         print("goodbye")
    # while not self.make_exist(user_message):
    answer =self.respond(user_message)
    return answer
# chatbot= ChatBot()
# chatbot.chat()