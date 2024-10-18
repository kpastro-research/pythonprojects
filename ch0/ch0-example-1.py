import random # library for randomness
# LIST : items grouped in square brackets seperated by ,
suits = ["Clubs", "Spades", "Hearts", "Diamonds"] # Array of suites (Python LIST)
faces = ["Jack", "Queen", "King", "Ace"] # Array of faces
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10] # Array of numbers
def draw(): # function definition draw
    # select randon value from Array of suites and assign it variable the_suit
    the_suit = random.choice(suits)
    # concat / combine arrays faces and numbered
    # select randon value from combined array and assign it to variable the_card
    the_card = random.choice(faces + numbered)
    # return concatenated text with value from the_card variable , of, and value from the_suit variable
    # TUPLE - items grouped in parentheses seperated by ,
    return the_card, "of", the_suit
print(draw()) # call function draw and print value
# print_draw(2) # RunTime error: Since print_draw function is defined below this statement it cannot find it ,
print("=> print_draw function call results below ")
#  For Loop example
def print_draw(times):
 for i in range(times):# In build function
    print(draw())

print_draw(2) # call function draw and print value
print_draw(5) # call function draw and print value

# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT
# ~~~~~~~~~~~~~~~~~~
# Python is interpreter , goes line by line in sequence
#  library to be used must be imported at the start of the script
# LIST : items grouped in "square brackets" seperated by ,
# TUPLE - items grouped in "parentheses" seperated by ,
# Function must be defined above the statement where it is called.
# BIF: Built In Function
# BIF example used random, range
# function definition starts with def function bname(parameters if any) : <= end with colon
# code in function  is indented , i.e cannot start exactly below def
# code in for loop is also indented , i.e cannot start exactly below for

