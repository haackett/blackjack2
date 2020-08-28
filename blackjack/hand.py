from typing import List
from blackjack.card import Card

valueConversions = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10,
    'Ace' : 11
}

class Hand:
    def __init__(self, cards=[]):
        self.cards = cards
        self.complete = False
        self.busted = False

    def add_card(self, card):
        self.cards.append(card)

    def hand_value(self) -> int:
        """ Returns the integer value of the hand, evaluating aces as 11 whenever optimal."""
        values = []
        for card in self.cards:
            values.append(valueConversions[card.value])
        while (values.count(11) != 0):
            if (self.sum_values(values) > 21):
                values[values.index(11)] = 1
            else: 
                break
        return self.sum_values(values)

    def sum_values(self, values: List[int]) -> int:
        """ Helper method for hand_value. Returns the sum of all values in a List"""
        sum = 0
        for value in values:
            sum = value + sum
        return sum

    def check_splittable(self) -> bool:
        splittable = False
        if len(self.cards) == 2:
            if self.cards[0].value == self.cards[1].value:
                splittable = True
        return splittable
