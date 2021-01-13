# Shuffle Deck of cards

import random

# In the program, we used the product() function in itertools module to create a deck of cards. This function performs the Cartesian product of the two sequences.

from itertools import product


deck = list(product(range(1, 14), ["Spade", "Heart", "Club", "Diamond"]))

random.shuffle(deck)

print(" Your picked card is: ")

for i in range(5):
    print(deck[i][0], "of", deck[i][1])
