import unittest
import random
from blackjack.deck import Deck
from typing import List 

class Tests(unittest.TestCase):
    d = Deck()
    
    def test_deal(self):
        self.assertIsNotNone(self.d.deal())

    def test_shuffle(self):
        shuffledDeck = Deck()
        shuffledDeck.shuffle()
        self.assertNotEqual(self.d.deal(), shuffledDeck.deal())

if __name__ == '__main__':
    unittest.main(verbosity=2)