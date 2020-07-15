import unittest
from hand import *

""" 
                FIX ME
import sys
sys.path.insert(1, '/Users/Aidan/Desktop/pyworkspace/blackjack/Deck')
from Deck import card
"""

class Tests(unittest.TestCase):
    def test_evaluate_hand(self):
        twoAces = Hand()
        Hand.build(twoAces, [Card('Ace', 'Clubs'), Card('Ace', 'Clubs')] )
        self.assertEqual(Hand.evaluate_hand(twoAces), 13)

if __name__ == '__main__':
    unittest.main(verbosity=2)