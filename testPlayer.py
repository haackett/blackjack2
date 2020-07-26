import unittest
from player import Player
from card import Card
from hand import Hand

class Tests(unittest.TestCase):
    p = Player()

    def test_bust_hand(self):
        self.p.hands.append(Hand())
        self.p.hands[0].cards = [Card('a','b'), Card('c', 'd')]
        #check the player has a hand at index 0
        self.assertIsNotNone(self.p.hands[0])
        self.p.bust_hand(0)
        #check that the player's hands are now empty
        self.assertEqual(self.p.hands[0].busted, True)

    def test_hit(self):
        self.p.hands = []
        card = Card('a', 'b')

        #check hand containing card
        self.p.hit(card, 0)
        self.assertEqual(self.p.hands[0].cards, [card])

        #check hand containing two cards
        self.p.hit(card,0)
        self.assertEqual(self.p.hands[0].cards, [card, card])

        #check player with 2 hands
        self.p.hit(card, 1)
        self.assertEqual(self.p.hands[0].cards, [card,card])
        self.assertEqual(self.p.hands[1].cards, [card])

if __name__ == '__main__':
    unittest.main(verbosity=2)