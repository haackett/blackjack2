import unittest
import random
from blackjack.betting import *
from blackjack.player import Player
from typing import List 

class Tests(unittest.TestCase):

    def test_buyin(self):
        p = Player()
        buyin(p, 100)
        self.assertEqual(p.stack, 100)

    def test_is_bet_valid(self):
        p = Player()
        p.stack = 0
        self.assertEqual(is_bet_valid(p, 5), False)
        p.stack = 5
        self.assertEqual(is_bet_valid(p, 5), True)
        
    def test_bet(self):
        p = Player()
        p.stack = 100
        bet(p, 5)
        self.assertEqual(p.bet, 5)
        self.assertEqual(p.stack, 95)

    def test_pay(self):
        p = Player()
        pay(p, 100)
        self.assertEqual(p.stack, 100)
    
    def clear_bet(self):
        p = Player()
        p.bet = 5
        clear_bet(p)
        self.assertEqual(p.bet, 0)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)