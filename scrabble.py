letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key : value for key, value in zip(letters, points)}

# print("brownie_points")
new_dict={" ":0}
letters_to_points.update(new_dict)
# print(letters_to_points)
# print(letters_to_points["A"])
def score_word(word):
  point_total=0
  for letter in word:
    if letter in letters_to_points:
      point_total+=letters_to_points[letter]
    else:
      point_total+=0
    # print(point_total)
  return point_total
    
brownie_points = score_word("BROWNIE")
print(brownie_points)



player_to_words= {"player1":['BLUE', 'TENNIS', 'EXIT'],"wordNerd":['EARTH', 'EYES', 'MACHINE'],"Lexi Con":['ERASER', 'BELLY', 'HUSKY'],"Prof Reader":['ZAP', 'COMA', 'PERIOD']}

player_to_points={}
for player, words in player_to_words.items():
  player_point=0
  for word in words:
    player_point = score_word(word)
  player_to_points[player]=player_point
print(player_to_points)

def play_word():
  player = input("Player name:\n>")
  word = input("Word to play:\n>")
  return {player, word}
play_word()