import random # library for randomness
suits = ["Clubs", "Spades", "Hearts", "Diamonds"] # Array of suites
faces = ["Jack", "Queen", "King", "Ace"] # Array of faces
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10] # Array of numbers
def draw(): # function definition draw
    # select randon value from Array of suites and assign it variable the_suit
    the_suit = random.choice(suits)
    # concat / combine arrays faces and numbered
    # select randon value from combined array and assign it to variable the_card
    the_card = random.choice(faces + numbered)
    # return concatinated text with value from the_card variable , of, and alue from the_suit variable
    return the_card, "of", the_suit
print(draw()) # call function draw and print value
# print_draw(2) # RunTime error: Since print_draw function is defined below this statement it cannot find it ,
print("=> print_draw function call results below ")
#  For Loop example
def print_draw(times):
    for i in range(times):
        print(draw())

print_draw(2) # call function draw and print value
print_draw(5) # call function draw and print value
