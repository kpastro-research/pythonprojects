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


def draw_card():
    return random.choice(list(deck_of_cards())) # Note: deck_of_cards() is set converted to list

    # return random.choice(deck_of_cards()) # TypeError: 'set' object is not subscriptable

def draw_and_remove():
    deck = list(deck_of_cards())
    card = random.choice(deck)
    deck.remove(card)
    return  card # Note: deck_of_cards() is set converted to list

print(draw_card())
print(draw_and_remove())

# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT # TypeError: 'set' object is not subscriptable
# ~~~~~~~~~~~~~~~~~~
# Since Set Being an unordered collection, sets do not record element position or order of insertion.
# Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.
# random.choice(deck_of_cards()) its converted to list
#  remove()