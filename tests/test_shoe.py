import unittest
import random
from blackjack.shoe import Shoe
from typing import List 

class Tests(unittest.TestCase):
    
    def test_init(self):
        s = Shoe(1)
        self.assertEqual(len(s._cards), 52)

    def test_deal(self):
        s = Shoe(1)
        self.assertIsNotNone(s.deal())

    def test_get_num_cards_remaining(self):
        s = Shoe(1)
        self.assertEqual(s.get_num_cards_remaining(), 52)

    #TODO : a test to make sure the decks have shuffled invidiually
    # Maybe test the distance between cards of the same value and suit?

if __name__ == '__main__':
    unittest.main(verbosity=2)