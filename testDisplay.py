from display import Display
from typing import List
from card import Card
from deck import Deck
from player import Player
from io import StringIO
import unittest
import sys

class Tests(unittest.TestCase):
    d = Display()

    def test_display_busted(self):
        p = Player()
        players = [p]
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        #test for player at index 0
        self.d.display_busted(p, players)
        #test for dealer
        p.isDealer = True
        self.d.display_busted(p, players)
        #test different player index
        p.isDealer = False
        self.d.display_busted(p, [None, None, p])

        self.assertEqual(capturedOutput.getvalue(), "Player 0 has busted!\nThe dealer has busted!\nPlayer 2 has busted!\n")
        capturedOutput.close()
       
    def test_display_blackjacks(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.d.display_blackjacks([True, False, False])
        self.d.display_blackjacks([False, True, False])
        self.d.display_blackjacks([True, True, True])
        self.assertEqual(capturedOutput.getvalue(), "The dealer has blackjack.\nPlayer 0 has blackjack.\nThe dealer has blackjack.\nPlayer 0 has blackjack.\nPlayer 1 has blackjack.\n")
        capturedOutput.close()
    
    def test_display_hand(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        hand = [Card('Ace','Spades'),Card('2','Clubs')]
        self.d.display_hand(hand, 0)
        self.assertEqual(capturedOutput.getvalue(), "Player 0's hand is: \nAce of Spades\n2 of Clubs\n")
        capturedOutput.close()

    def test_display_winning_players(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.d.display_winning_players([False, False])
        self.d.display_winning_players([True,True])
        self.assertEqual(capturedOutput.getvalue(), "The house wins.\nPlayer 0 wins!\nPlayer 1 wins!\n")
        capturedOutput.close()


    def test_display_dealer_hand(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        capturedOutput.close()

    def test_prompt_player(self):
        raise NotImplementedError

if __name__ == "__main__":
    unittest.main(verbosity=2)




