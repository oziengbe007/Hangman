
# - Create a function that would run the main game
# - Print the black jack logo
# - Deal the first card to dealer
# - Deal the first two cards to the player
# - Remove 11 from the first two cards given to the player
# - Print out the first card of the dealer, first two cards given to the player and the sum of both cards
# - Call your function

from logo import logo
from deal_card import deal_card
from draw_player_card import draw_player_card
from remove_eleven import remove_eleven
from hit_or_stand import hit_or_stand
from display_winner import display_winner
from draw_dealer_card import draw_dealer_card as give_dealer_card

dealers_card = []
players_card = []


# Create a function that would run the main game
def main(dealers_card, players_card, main_logo=logo):
    """
        Main 'Black Jack' game function

        Expects the following arguments:
        - dealers_card (a python list)
        - players_card (a python list)
    """
    # Print the black jack logo
    print(main_logo)

    # Deal the 1st card to the dealer and the player
    dealers_card, players_card = deal_card(dealers_card, players_card)

    # adding another card (i.e. the 2nd) to the player
    players_card = draw_player_card(players_card)

    # Remove 11 from the first two cards given to the player
    players_card = remove_eleven(players_card)

    # Print out the first card of the dealer, first two cards given to the player and the sum of both cards
    print(f"Dealers 1st card: {dealers_card[0]}")
    print(f"Players 1st two cards: {players_card[:2]}")

    # END OF TASK 1

    # TASK 2 - Ekem, Emmanuel, Sam Oladapo
    # - Create a loop that continuosly asks the user if they want to hit or stand
    while True:
        answer = hit_or_stand()
        # - If user choice is 'hit' give the player more cards
        if answer == 'hit':
            players_card = draw_player_card(players_card)
            # - Remove 11 from from players card if the total is greater than 21 and add 1
            players_card = remove_eleven(players_card)
            # - Print the dealers first card, the players card and the sum of the players card
            print(f"Dealer's 1st card: {dealers_card[0]}")
            print(f"Player's Card: {players_card}")
            print(f"Sum of Player's card is: {sum(players_card)}")

# TASK 3 - Elizabeth, Ugochuckwu,Benedict
# - If the user choice is 'stand' give cards to the dealer
        elif answer == 'stand':
            dealers_card = give_dealer_card(dealers_card)
            # - Display all the dealers card and the sum of his cards
            print(f"Dealer's card = {dealers_card} ")
            sum_dealer = sum(dealers_card)
            print(f"Sum of Dealers card is: ", sum_dealer)

            # - Display the players card and the sum of his cards
            print(f"players card is: {players_card}")
            sum_player = sum(players_card)
            print(f'sum of players card is: ', sum_player)
            # - Print out the winner of the game
            print(f"Feedback: {display_winner(players_card, dealers_card)}")

            # TASK 4 -  Daniel
            # - Ask if the user wants to play again
            # - If their reponse startsith 'y' call the function that will start the whole game again
            # - Else break out of the current loop and end the game

            # end_game= input("Do you want to play again: ")
            end_game = input("\nDo you want to play again:").lower().strip()

            if end_game.startswith('y'):
                dealers_card = []
                players_card = []
                main(dealers_card, players_card)
            else:
                print("Bye!")
                break


# call the main function
main(dealers_card, players_card)
