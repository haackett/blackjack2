from blackjack.card import Card
from blackjack.deck import Deck
import random

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Clubs','Diamonds','Hearts','Spades']

class Shoe(Deck):
    def __init__(self, numDecks):
        self._cards = []
        self.build(numDecks)
    
    def build(self, numDecks):
        cards = []
        for _ in range(numDecks):
            cards.extend(self.shuffle([Card(value,suit) for value in values for suit in suits]))
        self._cards = cards

    def shuffle(self, cards):
        cardsIn = cards
        cardsOut = []
        while (len(cardsIn) > 0):
            randIndex = random.randint(0, len(cardsIn) - 1)
            cardsOut.append(cardsIn[randIndex])
            del cardsIn[randIndex]
        return cardsOut

    def get_num_cards_remaining(self) -> int:
        return len(self._cards)

