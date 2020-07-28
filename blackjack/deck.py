import random
from card import Card
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Clubs','Diamonds','Hearts','Spades']

class Deck:
    def __init__(self):
        self._cards = [Card(value,suit) for value in values for suit in suits]
      
    def deal(self):
        return self._cards.pop()

    def shuffle(self):
        cards = []
        while (len(self._cards) > 0):
            randIndex = random.randint(0, len(self._cards) - 1)
            cards.append(self._cards[randIndex])
            del self._cards[randIndex]

        self._cards = cards

