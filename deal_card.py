# - Create a function called deal card
# - It should accept two list as parameter one for the dealer,
# - the other for the player
# - Your function should append a random number between 1 and 11 to the lists
# - Return the modified list
# - Your function will be used to give the first card to both the dealer and the player

import random

def deal_card(dealers_list, players_list):
  """This function is meant to add to dealers and players list a randomly generated between 1 to 11"""
  
  dealers_list.append(random.randint(1,11))
  players_list.append(random.randint(1,11))
  
  return dealers_list, players_list

