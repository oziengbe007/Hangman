# - Create a function called display_winner
# - It should accept two two parameters one for the sum of the player, the other for the sum of the dealer
# - Use the following rules to check for the winner:
    # if sum of player cards is greater than 21 - Player is bursted player lose
    # if sum of dealer cards is greater than 21 - Dealer is bursted player win
    # if sum of player cards and sum of dealer cards = 21 --- Its a Push, tie
    # if sum of dealer cards = 21 - Dealer has a blackjack player lose
    # if sum of player cards = 21 - player has a blackjack player wins
   
# if none of the above has happened then check
    # if sum of player cards is greater than sum of dealer cards - player wins
    # if sum of dealer cards is greater than sum of player cards - player lose
    # if sum of dealer cards is equal to sum of player cards - Its a push, tie
# - Return the output of the comparison
# - Your function will be used to display the winner in the console
def display_winner(player_card, dealer_card):
    '''The function decides the winner, looser, or if its a draw, and then displays result to the console'''
    sum_player = sum(player_card)
    sum_dealer = sum(dealer_card)
    if sum_player == 21 and sum_dealer == 21:
      return 'Its a Push 🤝'
    if sum_player > 21:
        return 'You are busted! - You Loose 😔!'
    if sum_dealer > 21:
        return 'Dealer is busted! - You win 🏆'
    if sum_player == 21:
      return 'You have a blackJack 🏆'
    if sum_dealer == 21:
        return 'Dealer has a blackJack 😔'
    if sum_dealer > sum_player:
        return 'Dealer wins 😔!'
    if sum_dealer < sum_player:
        return 'You win 🏆!'
    if sum_dealer == sum_player:
        return 'Its a push- tie 🤝!'