from random import shuffle

def make_deck():
    """
    Returns: deck - a list of lists which are suits, containing a list of dictionaries which are supposed to represent cards

    Parameters - None

    The purpose of this function is to create a deck using a nested for loop. This function should be called every time a new round is started as a way to replace every card in the deck so it doesn't run out
    """
    deck = []

    for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
        for number in range(1, 14):
            deck.append(make_card(suit, number))

    return deck

def make_card(suit, number):
    if number == 1: # If ace
        return {'type':'Ace', 'value':11, 'display':f'Ace of {suit}'}
    elif number == 11: # If Jack
        return {'type':'Face', 'value':10, 'display':f'Jack of {suit}'}
    elif number == 12: # If queen
        return {'type':'Face', 'value':10, 'display':f'Queen of {suit}'}
    elif number == 13: # If king
        return {'type':'Face', 'value':10, 'display':f'King of {suit}'}
    else:
        return {'type':'number', 'value': number, 'display':f'{number} of {suit}'}

def shuffle_deck(deck):
    shuffled_deck = deck
    shuffle(shuffled_deck)
    return shuffled_deck

if __name__ == "__main__":
    print(make_deck())