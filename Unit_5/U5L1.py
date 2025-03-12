import random

#Card class to create an object of a card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class to create an object of a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return "No cards left in the deck."

# Example usage:
deck = Deck()
deck.shuffle()

#draw 5 cards from the deck
print("Drawing 5 cards:")
for i in range(5):
    print(deck.drawCard())
