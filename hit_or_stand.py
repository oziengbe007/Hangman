# - Create a function called hit_or_stand
# - It should ask a user if they want to hit or stand
# - If the user types anything outside hit or stand,
# - it should ask them again if they want to hit or stand
# - Return the input given by the user
#  -Your function will be used to ask they player if they want to hit or stand


def hit_or_stand():  # hit or stand
    '''A function to ask for Hit or Stand'''
    while True:
        ask = input(
            "\nWould you like to hit or stand? Please enter 'hit' or 'stand': "
        )
        if ask[0].lower() == 'h':
            ask = 'hit'
            break
        elif ask[0].lower() == 's':
            ask = 'stand'
            break
        else:
            print("Sorry! wrong input! Please try again!")
            continue
    return ask
