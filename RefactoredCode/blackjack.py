import os
import deck

def hit_stay(player_cards):
    """Allows a user to take as many cards as they want until they go over 21 or choose to stay"""
    while True: # Every loop it should ask if you want a card    
        if calculate_hand_total(player_cards) > 21:
            print("Bust!")
            break

        take_card = input("Would you like another card? (1 = Yes 2 = No): ")

        if take_card == "1": # Only happens if they want a card
            player_cards.append(get_card())
            print(player_cards[-1]['display'])
        elif take_card == "2":
            break

    return player_cards

def dealer_logic(dealer_cards, player_cards):
    """Makes the dealer take a card until it is at or above 17"""
    if calculate_hand_total(player_cards) > 21: # Only takes something if the player did not bust
        return dealer_cards
    
    while calculate_hand_total(dealer_cards) < 17: # Takes a card until the dealer's total is at least 17
        dealer_cards.append(get_card())
        
    return dealer_cards
    
def determine_winner(points, bet, player_total, dealer_total):
    """Determines the winner and returns the new amount of points a player should have"""
    print("Your total:", player_total, "\nDealer total:", dealer_total)
    if player_total > 21:
        return loss(points, bet)
    elif player_total == dealer_total and player_total < 22:
        return tie(points)
    elif player_total > dealer_total and player_total < 22:
        return win(points, bet)
    elif dealer_total > player_total and dealer_total < 22:
        return loss(points, bet)
    elif player_total < 22 and dealer_total > 21:
        return win(points, bet)

def tie(points):
    print("It's a tie!")
    win_loss_record['Ties'] += 1
    return points

def loss(points, bet):
    print("You lose!")
    win_loss_record['Losses'] += 1
    return points - bet

def win(points, bet):
    print("You win!")
    win_loss_record['Wins'] += 1
    return points + bet

def get_bet(points: int) -> int:
    """Gets the amount of points the user wants to bet"""
    bet = 0
    while not valid_bet(bet, points):
        bet = input("You have " + str(points) + " points. How much would you like to bet? ")

    return int(bet)

def valid_bet(bet: str, points: int) -> bool:
    """Returns True if user entered a valid bet otherwise return False"""
    try:
        return int(bet) > 0 and int(bet) <= points
    except ValueError:
        return False

def get_card():
    """Returns a card off the top of the deck"""
    return game_deck.pop()

def calculate_hand_total(hand):
    """Gets the total value of a hand"""
    numAces = len([card for card in hand if card["type"] == "Ace"])
    handTotal = sum([x["value"] for x in hand])

    # If the total is greater than 21 and there are still aces
    # Then subtract 10 from the total and take away one ace
    while handTotal > 21 and numAces:
        handTotal -= 10
        numAces -= 1

    return handTotal

# Global variables
points = 1000
win_loss_record = {'Wins':0, 'Losses':0, 'Ties':0}

if __name__ == "__main__":
    # Play a new game until the user quits or they run out of points
    while True:
        # Create the deck and get the players bet
        game_deck = deck.shuffle_deck(deck.make_deck())
        bet = get_bet(points)

        player_cards = [get_card(), get_card()]
        dealer_cards = [get_card(), get_card()]

        # Display cards
        print("Your cards: " + "\n".join([card['display'] for card in player_cards]))
        print("Dealers cards: " + "\n".join([card['display'] for card in dealer_cards]))

        # Have the player and the dealer take cards until they're done
        player_cards = hit_stay(player_cards)
        dealer_cards = dealer_logic(dealer_cards, player_cards)
        points = determine_winner(points, bet, calculate_hand_total(player_cards), calculate_hand_total(dealer_cards))

        # If the user runs out of points it should end the game
        if not points:
            print("You ran out of points!")
            break

        # If the user chooses not to play again break
        play_again = input("Would you like to play again? (1 = Yes | 2 = No) ")
        if play_again == "2":
            break
        os.system('clear')

    print(f"Wins: {win_loss_record['Wins']}")
    print(f"Losses: {win_loss_record['Losses']}")
    print(f"Ties: {win_loss_record["Ties"]}")
    print(f"Points: {points}")