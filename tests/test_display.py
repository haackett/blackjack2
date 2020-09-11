from blackjack.display import Display
from typing import List
from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player import Player
from io import StringIO
from blackjack.hand import Hand
import unittest
from unittest.mock import patch
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
        hand = Hand(cards=[Card('Ace','Spades'),Card('2','Clubs')])
        self.d.display_hand(hand, 0)
        self.assertEqual(capturedOutput.getvalue(), "Player 0's hand is: \nAce of Spades\n2 of Clubs\n")
        capturedOutput.close()

    def test_display_winning_players(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.d.display_winning_players([[0],[1]])
        self.d.display_winning_players([[0],[-1,1]])
        self.assertEqual(capturedOutput.getvalue(), "Player 0 hand 0 pushes.\nPlayer 1 hand 0 wins!\nPlayer 0 hand 0 pushes.\nPlayer 1 hand 0 loses.\nPlayer 1 hand 1 wins!\n")
        capturedOutput.close()

    def test_display_dealer_hand(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        dealer = Player(isDealer=True)
        dealer.hands.append(Hand(cards=[Card("2","Spades"), Card("8","Spades")]))
        self.d.display_dealer_hand(dealer)
        self.d.display_dealer_hand(dealer, hidden=False)
        self.assertEqual(capturedOutput.getvalue(), "The dealer hand is: \n2 of Spades\nThe dealer hand is: \n2 of Spades\n8 of Spades\n")
        capturedOutput.close()
    
    @patch('blackjack.display.Display.get_input', return_value='h')
    def test_choice_hit(self, return_value):
        self.assertEqual(self.d.prompt_player(0), 'h')

    @patch('blackjack.display.Display.get_input', return_value='s')
    def test_choice_stay(self, return_value):
        self.assertEqual(self.d.prompt_player(0), 's')

    @patch('blackjack.display.Display.get_input', return_value = 5)
    def test_valid_bet(self,return_value):
        p = Player()
        p.stack = 5
        players = [p]
        self.assertEqual(self.d.prompt_player_for_bet(p, players), 5)
    
    @patch('blackjack.display.Display.get_input', return_value = 5)
    def test_invalid_bet_amount(self, return_value):
        p = Player()
        p.stack = 0
        players = [p]
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.d.prompt_player_for_bet(p, players)
        self.assertEqual(capturedOutput.getvalue(), "Please enter a bet less than or equal to 0\n")

    def test_display_changing_shoe(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.d.display_changing_shoe()
        self.assertEqual(capturedOutput.getvalue(), 'Last deck reached. Getting new shoe...\n')
    
if __name__ == "__main__":
    unittest.main(verbosity=2)




