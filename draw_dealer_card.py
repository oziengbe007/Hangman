# - Create a function called draw_dealer_card
# - It should accept a list as a parameter
# - Your function should keep adding numbers to the list when the sum of all the numbers in the list is less than 17
# - Use the function created by remove_eleven.py to remove 11 from your list and add 1 to it if the total sum is greater than 21
# - Return the modified list
# - Your  function will be used to give the dealer more cards when the player stands

import random
from remove_eleven import remove_eleven

# def draw_dealer_card(dealer_list):
#   '''This function is for randomly selecting cards from the deck of cards for the dealer when the player stands. The returned list will contain the modified list when the sum of the elements in the list is equal to or greater than 17'''
#   while True:
#     modified_list = dealer_list
#     while True:
#       if sum(modified_list) < 17:
#         modified_list.append(random.randint(1, 11))
#         break
#       elif sum(modified_list) > 21 and 11 in modified_list:
#         remove_eleven.remove_eleven(modified_list)
#         break
#     if sum(modified_list) >= 17:
#       break
#   return modified_list

def draw_dealer_card(dealers_list):
  '''
  draws a card continuously for the dealer
  remove 11 if card is greater than 21
  '''
  while sum(dealers_list) < 17:
    dealers_list.append(random.randint(1,11))
    dealers_list = remove_eleven(dealers_list)
  return dealers_list