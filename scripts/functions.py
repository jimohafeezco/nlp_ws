# # Define your functions

def coffee_bot():
  print("Welcome to the cafe")
  size =get_size()
  drink_type= get_drink_type()
  cup= cup_type()
  print("Alright, that's a %s %s" %(size, drink_type))
  name = input("May I know your name please: ")
  print("Thanks, %s! Your drink in %will be ready shortly" % (name, cup))
  
  

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>  ')
  if res =="a":
    return "small"
  elif res =="b":
    return "medium"
  elif res =="c":
    return "large"
  else:
    print_message()
    return get_size()
    
# Call coffee_bot()!
# get_size()

def print_message():
  print("""I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.""")
  
def get_drink_type():
  res= input("""What type of drink would you     like? \n [a] Brewed Coffee \n[b] Mocha       \n[c] Latte \n>""")
  if res =="a":
    return "brewed coffee"
  elif res =='b':
    return "mocha"
  elif res =="c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()
    
def order_latte():
  res = input("And what kind of milk for your latte? \n [a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n>")
  if res =="a":
    return "latte"
  elif res =='b':
    return "non-fat"
  elif res =="c":
    return "soy latte"
  else:
    print_message()
    return order_latte()
def cup_type():
  res = input("What type of cup do you want ? \n[a] Plastic \n[b] Reusable cup \n>")
  if res =="a":
    return "Plastic"
  elif res =='b':
    return "reusable"
  else:
    print_message()
    return cup_type()
coffee_bot()
