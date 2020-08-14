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

    def test_bet(self):
        p = Player()
        p.stack = 100
        bet(p, 5)
        self.assertEqual(p.bet, 5)
        self.assertEqual(p.stack, 95)
    
    def clear_bet(self):
        p = Player()
        p.bet = 5
        clear_bet(p)
        self.assertEqual(p.bet, 0)
        
    def test_pay_blackjack(self):
        players = [Player(), Player()]
        players[0].bet = 5
        players[1].bet = 5
        blackjacks = [True, True, False]
        pay_blackjack(blackjacks, players)
        self.assertEqual(players[0].stack, 5)
        self.assertEqual(players[1].stack, 0)
        blackjacks = [False, False, True]
        pay_blackjack(blackjacks, players)
        self.assertEqual(players[0].stack, 5)
        self.assertEqual(players[1].stack, 12.5)

    def pay_players(self):
        players = [Player(), Player()]
        players[0].bet, players[1].bet = 5, 5
        playerStandings = [[1], [0]]
        pay_players(playerStandings, players)
        self.assertEqual(players[0].stack, 10)
        self.assertEqual(players[1].stack, 5)
        playerStandings = [[-1], [-1]]
        self.assertEqual(players[0].stack, 10)
        self.assertEqual(players[1].stack, 5)

    def test_get_stacks(self):
        players = [Player(), Player()]
        players[0].stack = 5
        players[1].stack = 10
        self.assertEqual(get_stacks(players), [5, 10])

if __name__ == '__main__':
    unittest.main(verbosity=2)