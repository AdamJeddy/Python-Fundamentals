# importing the file deck.py
# and using its function to create a set of cards
# and printing them

import deck

cards = deck.create_deck()

for card in cards:
    print(card)
