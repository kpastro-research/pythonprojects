import random # library for randomness
suits = ["Clubs", "Spades", "Hearts", "Diamonds"] # Array of suites (Python LIST)
faces = ["Jack", "Queen", "King", "Ace"] # Array of faces
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10] # Array of numbers
deck = set()
for suit in suits:
    for card in faces + numbered:
        deck.add((card, "of", suit))    # unique tuples added to deck

print(len(deck)) # length o decl
for deck in deck:
    print(deck)

