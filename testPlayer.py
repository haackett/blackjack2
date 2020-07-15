import unittest
from temporaryMasterFile import Player
from temporaryMasterFile import Card

class Tests(unittest.TestCase):
    p = Player()

    def test_bust_hand(self):
        self.p.hands[0] = [Card('a','b'), Card('c', 'd')]
        #check the player has a hand at index 0
        self.assertIsNotNone(self.p.hands[0])
        self.p.bust_hand(0)
        #check that the player's hands are now empty
        self.assertEqual(len(self.p.hands), 0)

    def test_hit(self):
        card = Card('a', 'b')

        #check hand containing card
        self.p.hit(card, 0)
        self.assertEqual(self.p.hands[0], [card])

        #check hand containing two cards
        self.p.hit(card,0)
        self.assertEqual(self.p.hands[0], [card, card])

        #check player with 2 hands
        self.p.hit(card, 1)
        self.assertEqual(self.p.hands, [[card,card],[card]])

if __name__ == '__main__':
    unittest.main(verbosity=2)