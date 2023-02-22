
### Blackjack with recursive functions and scoring

# setup and functions

import random

def player_draw(p_hand, dk):

    """Player draws 1 random card from deck"""
    card = random.randint(0, 12)

    p_hand.append(dk[card])

def dealer_draw(d_hand, dk):

    """Dealer draws 1 random card from deck"""

    card = random.randint(0, 12)
    d_hand.append(dk[card])

# def who_wins(d_total, p_total, dealer_score, player_score):         ### couldn't get the score to update through local variables
#
#     """Compares whose hand is greater, and adds 1 to score"""       ### so not in use
#
#     difference = d_total - p_total
#
#     if difference > 0:
#         print(f"The dealer wins with a total of {d_total} against your {p_total}")
#         dealer_score += 1
#
#     elif difference < 0:
#         print(f"You beat the dealer with a total of {p_total} against their {d_total}")
#         player_score += 1
#
#     else:
#         print(f"Tie game! the dealer has {d_total} and you have {p_total}")

def cont_play(dealer_score, player_score):

    """Triggers the recursive function of the main blackjack function,
        also prints out the updated score after every round"""

    again = input("Play another round? 'Y' or 'N': ").upper()
    print(f"the current score for this session is: dealer = {dealer_score}, player = {player_score}\n")

    if again == "Y":
        black_jack(dealer_score, player_score)

    else:
        print("Thank you for playing")
        return

### Main recursive function

def black_jack(dealer_score, player_score):

    """Parent function containing logic statements and auxiliary function calls"""

    dealer_hand = []                                                                                                    # Empty list for dealer's hand
    player_hand = []                                                                                                    # Empty list for player's hand
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]                                                                 # Simplified deck of cards



    # initial draw
    for i in range(2):                                                                                                  # Both players draw 2 cards
        player_draw(player_hand, deck)
        dealer_draw(dealer_hand, deck)

    player_hand_total = sum(player_hand)                                                                                # Total of player's hand
    dealer_hand_total = sum(dealer_hand)                                                                                # Total of dealer's hand
    print(f"your starting hand is {player_hand} with a total of {player_hand_total}\n")                                   # Print statement showing the players hand


    dealer_bust = False                                                                                                 # Boolean for while loops
    game_over = False                                                                                                   # Boolean for while loops

    while not game_over:                                                                                                # 1st while loop to cycle through decision tree

        choice_1 = input("Would you like to stick or twist? 'S' or 'T': ").upper()                                      # Input for 'stick' or 'twist' decision

        if choice_1 == "T":                                                                                             # If player 'twist', player draws care and calculates new total
            player_draw(player_hand, deck)
            player_hand_total = sum(player_hand)

            if player_hand_total > 21:                                                                                  # If player is bust, print the hand and total, add 1 to dealer score

                print(f"your hand is {player_hand} with a total of {player_hand_total}")
                print(f"Round over, you are bust!")
                dealer_score += 1

                cont_play(dealer_score, player_score  )                                                                 # call the continue_play function, passing the updated score
                break

            else:
                print(f"your hand is {player_hand} with a total of {player_hand_total}")                                # If player not bust then, print the hand and total

        if choice_1 == "S":                                                                                             # If player 'stick', logic tree moves into dealers while loop

            while not dealer_bust and not game_over:                                                                    # Boolean check to ensure no run away loops

                if dealer_hand_total < 17:                                                                              # If dealer has total under 17, then has to draw new card

                    dealer_draw(dealer_hand, deck)
                    dealer_hand_total = sum(dealer_hand)                                                                # New dealer hand total calculated

                    if dealer_hand_total > 21:                                                                          # If dealer total over 21 then bust

                        print(f"The dealer is bust with a total of {dealer_hand_total} against your {player_hand_total}, you win")
                        dealer_bust = True
                        game_over = True                                                                                # Booleans flip to true to stop further loop
                        player_score += 1                                                                               # Player's score + 1
                        cont_play(dealer_score, player_score)                                                           # Call the continue_play function to check for new round and update scores


                    elif 21 >= dealer_hand_total >= 17:                                                                 # If dealer's hand totals between 21 and 17 then forced 'stick'

                        difference = dealer_hand_total - player_hand_total

                        if difference > 0:
                            print(f"The dealer wins with a total of {dealer_hand_total} against your {player_hand_total}")
                            dealer_score += 1

                        elif difference < 0:
                            print(f"You beat the dealer with a total of {player_hand_total} against their {dealer_hand_total}")
                            player_score += 1

                        else:
                            print(f"Tie game! the dealer has {dealer_hand_total} and you have {player_hand_total}")

                        game_over = True                                                                                # Flip boolean to true to stop further loops
                        cont_play(dealer_score, player_score)                                                           # Call the continue_play function to check for new round and update scores


                if 21 >= dealer_hand_total >= 17:                                                                       # same logic as above but outside the < 17 logic branch

                    difference = dealer_hand_total - player_hand_total

                    if difference > 0:
                        print(f"The dealer wins with a total of {dealer_hand_total} against your {player_hand_total}")
                        dealer_score += 1

                    elif difference < 0:
                        print(
                            f"You beat the dealer with a total of {player_hand_total} against their {dealer_hand_total}")
                        player_score += 1

                    else:
                        print(f"Tie game! the dealer has {dealer_hand_total} and you have {player_hand_total}")

                    game_over = True
                    cont_play(dealer_score, player_score)


                elif dealer_hand_total > 21:                                                                            # If dealer over 21 and bust

                    print(f"The dealer has bust with {dealer_hand_total}, You win")                                     # Print 'dealer hand and bust'
                    game_over = True                                                                                    # Flip the booleans to stop loops
                    dealer_bust = True
                    player_score += 1                                                                                   # Add 1 to player score
                    cont_play(dealer_score, player_score)                                                               # Call continue_play function



black_jack(dealer_score = 0, player_score = 0)                                                                          # Call parent function with scores = 0