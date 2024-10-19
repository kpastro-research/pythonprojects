import random # library for randomness
def deck_of_cards():
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"] # Array of suites (Python LIST)
    faces = ["Jack", "Queen", "King", "Ace"] # Array of faces
    numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10] # Array of numbers
    deck = set()
    for suit in suits:
        for card in faces + numbered:
            deck.add((card, "of", suit))    # unique tuples added to deck
    return deck

# cards to finds
deck = deck_of_cards();
card1 = ('Queen', 'of', 'Hearts')
card2 = ('Queen', 'of', 'Spades')
card3 = ('Clown')

print("card1 in deck", card1 in deck)
print("card2 in deck", card2 in deck)
print("card3 in deck", card3 in deck)

# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT
# ~~~~~~~~~~~~~~~~~~
#  finding in collection
# Python has two built-in boolean values: True and False.
# in is equivalent to  contains condition check , can be used with if else