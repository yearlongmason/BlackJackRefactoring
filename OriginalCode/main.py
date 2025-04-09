import random
import os
import json
import create_deck


def hit_stay(player_total):
    """
    Parameters: player_total - the total of all the cards for the player. Assumes it's an integer.

    Returns: player_total - Should return the new player total with the new cards

    This should ask if you want to take a card or if you'd like to stay with what you have. If you want to take another card it should deal another card to you, and add it to the list of cards you've taken. If you want to stay the function should do nothing
    """
    extra_card = 0
    
    while True: #Every loop it should ask if you want a card    

        while True: #Should ask if the player wants a card and check their answer
            try:   
                take_card = int(input("Would you like another card? (1 = Yes 2 = No): "))
            except ValueError:
                print("Must be entered as an integer")
            else:
                break
        while take_card != 1 and take_card != 2:
            while True:
                try:
                    take_card = int(input("Invalid answer, please enter an integer. Would you like another card? (1 = Yes 2 = No): "))
                except ValueError:
                    print("Must be entered as an integer")
                else:
                    break

        if take_card == 1: #Only happens if they want a card
            extra_card = get_card()
            player_cards.append(extra_card)
            player_total += extra_card['value']
            print(extra_card['display'])
            if player_total > 21:
                for i in player_cards: #In case of a bust it should check for aces worth 11 and change them to 1
                    if i['value'] == 11:
                        i['value'] = 1
                        player_total -= 10
            if player_total > 21:
                print("Bust!")
                break
        else: #Breaks if the player doesn't want another card
            break
    return player_total


def dealer_logic(dealer_total):
    """
    parameters: dealer_total - the total of all the cards for the dealer. Assumes it's an integer.

    returns: dealer_total - Should return the new dealer total with the new cards.

    This should make the dealer take a card until it is at or above 17
    """
    if player_total < 22: #Only takes something if the player did not bust
        while dealer_total < 17: #Takes a card until the dealers total is at least 17
            extra_card = get_card()
            dealer_cards.append(extra_card)
            dealer_total += extra_card['value']

            if dealer_total > 21:
                for i in dealer_cards: #If the dealer busts it should check to see if they have aces that can be lowered to 1
                    if i['value'] == 11:
                        i['value'] = 1
                        dealer_total -= 10
    return dealer_total

    
def determine_winner(points, bet):
    """
    Parameters: points - The amount of points a player has (integer)
                bet - The amount the player chooses to bet

    Returns: points - the amount of points they have based on whether they won, lost, or tied

    Should just compare dealer and player scores to determine who won that round and then return the amount of points they have after that round
    """
    result = 0
    print("Your total: " + str(player_total) + "\nDealer total: " + str(dealer_total))
    if player_total > 21:
        result = 0
    elif player_total == dealer_total and player_total < 22:
        result = 2
    elif player_total > dealer_total and player_total < 22:
        result = 1
    elif dealer_total > player_total and dealer_total < 22:
        result = 0
    elif player_total < 22 and dealer_total > 21:
        result = 1
    
    if result == 1:
        print("You win!")
        win_loss_record['Wins'] += 1
        return points + bet
    elif result == 0:
        print("You lose!")
        win_loss_record['Losses'] += 1
        return points - bet
    else:
        print("It's a tie!")
        win_loss_record['Ties'] += 1
        return points


def get_bet():
    """
    Parameters: None

    Returns: The amount the player would like to bet

    This function should just ask the user how much they would like to bet of however many points they have
    """
    while True:
        while True: #Makes sure they're entering an integer
            try:
                bet = int(input("You have " + str(points) + " points. How much would you like to bet? "))
            except ValueError:
                print("Error: Must be entered as an integer")
            else:
                break
        if bet > 0 and bet <= points: #Makes sure the bet
            break
        else:
            print("Error: Enter a number between 1 and " + str(points))
    return bet


def get_card():
    """
    Parameters: None

    Returns: Card - a dictionary containing information about the card that was drawn

    This funcion should just pick a random card from the deck of cards and remove that card from the deck
    """
    suit = random.randint(0, len(deck) - 1)
    number = random.randint(0, len(deck[suit]) - 1)
    card = deck[suit][number]
    del deck[suit][number]
    return card


def get_high_scores():
    """
    Parameters: None

    Returns: high_score_num - a list of the high scores sorted
             high_scores - a dictionary of all of the scores and the names: {points:name}

    This function should get the high scores from the json file they're being stored in and make a duplicate of the json dictionary and make another list of all of the scores sorted so the high scores can be found
    """
    with open('high_scores.json', 'r') as file: #Reads json file and stores it in a dictionary
        high_scores = json.load(file)
    
    high_scores.update({str(points):name})

    with open('high_scores.json', 'w') as file: #Adds the most recent score to the dictionary
        json.dump(high_scores, file)

    high_score_num = list(high_scores.keys()) #Gets a list of keys so that it can be sorted and used for high scores
    high_score_num = list(map(int, high_score_num)) #Casts str list as int
    high_score_num.sort()
    return high_score_num, high_scores


points = 1000
bet = 0
win_loss_record = {'Wins':0, 'Losses':0, 'Ties':0}
replay = True


while replay: #Should just replay the game as long as the user chooses to do so
    bet = get_bet()
    deck = create_deck.make_deck()
    card1 = get_card()
    dealer_card1 = get_card()
    card2 = get_card()
    dealer_card2 = get_card() #Deals player and dealers cards (in order)
    player_cards = [card1, card2]
    dealer_cards = [dealer_card1, dealer_card2] #Stores cards in a list mainly in case there's a conflict with aces
    dealer_total = dealer_card1['value'] + dealer_card2['value']
    player_total = card1['value'] + card2['value'] #Calculates initial totals for both players
    print("Your cards: \n" + card1['display'] + "\n" + card2['display'])
    print("Dealers cards: \n" + dealer_card1['display'] + "\n?")

    player_total = hit_stay(player_total)
    dealer_total = dealer_logic(dealer_total)
    points = determine_winner(points, bet)
    if points == 0: #If the user runs out of points it should end the game
        print("You ran out of points!")
        break
    while True: #Asks the user if they'd like to play again
        play_again = input("Would you like to play again? (1 = Yes 2 = No) ")
        if play_again == "1":
            replay = True
            os.system('clear')
            break
        elif play_again == "2":
            replay = False
            break
        else:
            print("Invalid answer. Please enter as an integer.")

name = input("Enter your name: ")
high_score_num, high_scores = get_high_scores() #Gets the high scores and the names (high_score_num is just a list of the points, high_scores is a dictionary: {points:name})

print("Wins: " + str(win_loss_record['Wins']) + "\nLosses: " + str(win_loss_record['Losses']) + "\nTies: " + str(win_loss_record['Ties']) + "\nPoints: " + str(points))
print("High scores: ")
for i in range(3):
    print(high_scores[str(high_score_num[(-1*(i + 1))])] + ": " + str(high_score_num[(-1*(i + 1))]))