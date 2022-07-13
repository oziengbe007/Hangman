# - Create a function called remove_eleven
# - It should accept a list as a parameter
# - Your function should check if the sum of all the numbers in the list is greater than 21 and 11 is in the list
# - If that is true it should remove the 11 in the list and add 1 to  the list
# - Return the modified list
# - Your function will be used to count the ace card as 1 instead of 11


def remove_eleven(list_of_numbers):
  '''the function removes eleven and returns one, if the sum of numbers is greater than 21 and 11 is in the list'''
  if sum(list_of_numbers) > 21 and 11 in list_of_numbers:
    list_of_numbers.remove(11)
    list_of_numbers.append(1)
  return list_of_numbers
