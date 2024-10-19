import random # library for randomness
# Sets
suits = set()
print ("suites is of Type", type(suits), " having length", len(suits)) # O/P suites is of Type <class 'set'>  having length 0
print(dir(suits))
help(suits.add)
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
print ("suites is of Type", type(suits), " having length", len(suits))

faces = list()
print ("suites is of Type", type(faces), " having length", len(faces)) # O/P suites is of Type <class 'list'>  having length 0
print(dir(faces))
help(faces.append)
faces = ["Jack", "Queen", "King", "Ace"]
print ("faces is of Type", type(faces), " having length", len(faces)) # tuple

numbered = tuple()
print ("numbered is of Type", type(numbered), " having length", len(numbered)) # O/P suites is of Type <class 'tuple'>  having length 0
print(dir(numbered))
help(numbered.count)
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("numbered is of Type", type(numbered), " having length", len(numbered))  # O/P tuple: numbered_duplicated is of Type <class 'list'>  having length 9

numbered_duplicated = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10 ]
numberedSet = set(numbered_duplicated) # numbered set take unique value from list containing duplicate values
print ("numbered_duplicated is of Type", type(numbered_duplicated), " having length", len(numbered_duplicated)) # O/P tuple: numbered_duplicated is of Type <class 'list'>  having length 14
print ("numberedSet is of Type", type(numberedSet), " having length", len(numberedSet)) # length reduced to 9 , set takes unique values


# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT BIF: BuiltIn Function
# ~~~~~~~~~~~~~~~~~~
# set()/ set(data): creates a variable of  type set
# list() / list(data): creates a variable of  type list
# tuple() / tuple(data): creates a variable of  type data
# type(variable):  identifies type of variable
# len(variable)) : return length of variable
# dir(variable): list attribute of Type of variable
# help(BIF) returns details of  BIF


