# Deal a deck of cards

#Solution 1
import random

# Create a list for a standard deck of cards
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []
hand = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')
print(f'There are {len(deck)} cards in the deck.')

# Randomly choose 5 cards to add to a player's hand
print('Dealing ...')

for i in range(5):
    number = random.choice(deck)
    deck.remove(number)
    hand.append(number)
    #print(number)

print(f'There are {len(deck)} cards in the deck.')
print(f'Player has the following cards in their hand:\n{hand}')