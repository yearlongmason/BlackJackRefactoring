import os
import deck


def hit_stay(player_hand):
    """
    Parameters: player_total - the total of all the cards for the player. Assumes it's an integer.

    Returns: player_total - Should return the new player total with the new cards

    This should ask if you want to take a card or if you'd like to stay with what you have. If you want to take another card it should deal another card to you, and add it to the list of cards you've taken. If you want to stay the function should do nothing
    """
    while True: # Every loop it should ask if you want a card    
        if getHandTotal(player_hand) > 21:
            print("Bust!")
            break

        take_card = input("Would you like another card? (1 = Yes 2 = No): ")

        if take_card == "1": #Only happens if they want a card
            new_card = get_card()
            player_hand.append(new_card)
            print(new_card['display'])

            # Ace logic
            if getHandTotal(player_hand) > 21:
                for i in range(len(player_hand)): #In case of a bust it should check for aces worth 11 and change them to 1
                    if player_hand[i]['value'] == 11:
                        player_hand[i]['value'] = 1
            continue
        break

    return getHandTotal(player_hand)


def dealer_logic(dealer_cards):
    """
    parameters: dealer_total - the total of all the cards for the dealer. Assumes it's an integer.

    returns: dealer_total - Should return the new dealer total with the new cards.

    This should make the dealer take a card until it is at or above 17
    """
    if player_total > 21: #Only takes something if the player did not bust
        return getHandTotal(dealer_cards)
    
    while getHandTotal(dealer_cards) < 17: #Takes a card until the dealers total is at least 17
        new_card = get_card()
        dealer_cards.append(new_card)

        # Ace logic
        if getHandTotal(dealer_cards) > 21:
            for i in range(len(dealer_cards)): #If the dealer busts it should check to see if they have aces that can be lowered to 1
                if dealer_cards[i]['value'] == 11:
                    dealer_cards[i]['value'] = 1
        
    return getHandTotal(dealer_cards)

    
def determine_winner(points, bet, player_total, dealer_total):
    """
    Parameters: points - The amount of points a player has (integer)
                bet - The amount the player chooses to bet

    Returns: points - the amount of points they have based on whether they won, lost, or tied

    Should just compare dealer and player scores to determine who won that round and then return the amount of points they have after that round
    """
    result = 0
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
    """
    This function should just ask the user how much they would like to bet of however many points they have
    """
    bet = 0
    while not validBet(bet, points):
        bet = input("You have " + str(points) + " points. How much would you like to bet? ")

    return int(bet)

def validBet(bet: str, points: int) -> bool:
    try:
        return int(bet) > 0 and int(bet) <= points
    except ValueError:
        return False

def get_card():
    """
    Parameters: None

    Returns: Card - a dictionary containing information about the card that was drawn

    This funcion should just pick a random card from the deck of cards and remove that card from the deck
    """
    return game_deck.pop()

def getHandTotal(hand):
    return sum([x["value"] for x in hand])

# Global variables
points = 1000
win_loss_record = {'Wins':0, 'Losses':0, 'Ties':0}

if __name__ == "__main__":
    while True: #Should just replay the game as long as the user chooses to do so
        game_deck = deck.shuffle_deck(deck.make_deck())
        bet = get_bet(points)
        player_cards = [get_card(), get_card()]
        dealer_cards = [get_card(), get_card()] #Stores cards in a list mainly in case there's a conflict with aces
        dealer_total = getHandTotal(dealer_cards)
        player_total = getHandTotal(player_cards)
        print("Your cards: " + "\n".join([card['display'] for card in player_cards]))
        print("Dealers cards: " + "\n".join([card['display'] for card in dealer_cards]))

        player_total = hit_stay(player_cards)
        dealer_total = dealer_logic(dealer_cards)
        points = determine_winner(points, bet, player_total, dealer_total)

        if points == 0: #If the user runs out of points it should end the game
            print("You ran out of points!")
            break
        play_again = input("Would you like to play again? (1 = Yes | 2 = No) ")
        if play_again == "2":
            break
        os.system('clear')

    print("Wins: " + str(win_loss_record['Wins']) + "\nLosses: " + str(win_loss_record['Losses']) + "\nTies: " + str(win_loss_record['Ties']) + "\nPoints: " + str(points))