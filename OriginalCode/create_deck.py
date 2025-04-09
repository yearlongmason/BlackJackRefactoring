def make_deck():
    """
    Returns: deck - a list of lists which are suits, containing a list of dictionaries which are supposed to represent cards

    Parameters - None

    The purpose of this function is to create a deck using a nested for loop. This function should be called every time a new round is started as a way to replace every card in the deck so it doesn't run out
    """
    deck = []

    for i in range(4):
        deck.append([]) #Creates a new list for every suit
        for x in range(13):
            if i == 0:
                suit_chosen = "Spades"
            elif i == 1:
                suit_chosen = "Hearts"
            elif i == 2:
                suit_chosen = "Clubs"
            else:
                suit_chosen = "Diamonds"
            
            if x+1 > 1 and x+1 < 11: #These are needed to be able to have aces, jacks, queens, and kings
                deck[i].append({'type':'number', 'value':x+1, 'display':str(x+1)+' of ' + suit_chosen})
            elif x+1 == 1:
                deck[i].append({'type':'Ace', 'value':11, 'display':'Ace of ' + suit_chosen})
            elif x+1 == 11:
                deck[i].append({'type':'Face', 'value':10, 'display':'Jack of ' + suit_chosen})
            elif x+1 == 12:
                deck[i].append({'type':'Face', 'value':10, 'display':'Queen of ' + suit_chosen})
            else:
                deck[i].append({'type':'Face', 'value':10, 'display':'King of ' + suit_chosen})
    return deck