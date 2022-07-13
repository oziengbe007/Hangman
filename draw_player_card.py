# - Create a function called draw_player_card
# - It should accept a list as a parameter
# - Your function should append a random number between 1 and 11 to the list
# - Return the modified list
# - Your  function will be called anytime the player wants more card
import random 

def draw_player_card(cards):
  """this allows player to draw a random card from a deck of cards in the range of 1 to 11 """
  cards.append(random.randint(1,11))
  return cards