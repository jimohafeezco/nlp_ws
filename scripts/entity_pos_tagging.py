from nltk import pos_tag
user_message = ["i", "ordered", "two", "t-shirts", "this", "past", "weekend", "when","will", "my", "package", "be", "shipped"]

#define `tagged_user_message` here
import re
tagged_user_message = pos_tag(user_message)
# print(tagged_user_message)
# a=re.findall('^NN', tagged_user_message[3][1])
# print(a)
def extract_nouns(tagged_message):
  message_nouns = list()
  #write your code here
  for word in tagged_user_message:
    pattern = re.findall('^NN', word[1])
    # print(pattern)
    if "NN" in pattern:
      message_nouns.append(word[0])  
  return message_nouns

user_message_nouns=extract_nouns(tagged_user_message)
print(user_message_nouns)
# #define `user_message_nouns` here