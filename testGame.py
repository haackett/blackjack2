import unittest
import random
from game import Game
from deck import Deck
from card import Card
from player import Player
from typing import List
from hand import Hand

#create one of each card value to test with
two = Card('2', 'Clubs')
three = Card('3', 'Clubs')
four = Card('4', 'Clubs')
five = Card('5', 'Clubs')
six = Card('6', 'Clubs')
seven = Card('7', 'Clubs')
eight = Card('8', 'Clubs')
nine = Card('9', 'Clubs')
ten = Card('10', 'Clubs')
jack = Card('Jack', 'Clubs')
queen = Card('Queen', 'Clubs')
king = Card('King', 'Clubs')
ace = Card('Ace', 'Clubs')


class Tests(unittest.TestCase):

    def test_check_if_busted(self):
            p = Player()
            g = Game([])
            cards = [queen, queen, queen]
            p.hands = [Hand(cards)]
            g.check_if_busted(p)
            self.assertEqual(p.hands[0].busted, True)

    def test_check_for_blackjack(self):
          g = Game([])
          players = [Player()]

          #check for dealer with blackjack and 1 player without blackjack
          players[0].hands.append(Hand([two, three]))        
          dealer = Player(isDealer=True)
          dealer.hands.append(Hand([ace, queen]))

          self.assertEqual(g.check_for_blackjack(players, dealer), [True, False])

          #check for dealer with BJ and 1 player with BJ
          players[0].hands[0] = Hand([ace, queen])
          self.assertEqual(g.check_for_blackjack(players, dealer), [True, True])

          #check for dealer without BJ and 1 player with BJ
          dealer.hands[0] = Hand([two, three])
          self.assertEqual(g.check_for_blackjack(players, dealer), [False, True])

          #check for dealer without BJ and 2 players with BJ
          players.append(Player())
          players[1].hands.append(Hand([ace, queen]))
          self.assertEqual(g.check_for_blackjack(players, dealer), [False, True, True])

          #check for dealer without BJ, 1 player with BJ, and 1 player without
          players[1].hands[0] = Hand([two, three])
          self.assertEqual(g.check_for_blackjack(players, dealer), [False, True, False])

    def test_hit_player(self):
        g = Game(Deck())
        p = Player()
        g.hit_player(p, 0, g.deck)
        self.assertEqual(len(p.hands), 1)

    def test_hit_dealer(self):
        g = Game(Deck())
        dealer = Player()

        #test with hand val < 17, expecting a hit
        dealer.hands.append(Hand([two, two]))
        g.hit_dealer(dealer, g.deck)
        self.assertGreater(len(dealer.hands[0].cards), 2)

        #test with hand val == 17, expecting a stand
        dealer.hands[0] = Hand([queen, seven])
        g.hit_dealer(dealer, g.deck)
        self.assertEqual(len(dealer.hands[0].cards), 2)

        #test with val > 17, expecting a stand
        dealer.hands[0] = Hand([queen, queen])
        g.hit_dealer(dealer, g.deck)
        self.assertEqual(len(dealer.hands[0].cards), 2)

    def test_bust_dealer(self):
        g = Game(Deck())
        dealer = Player()
        dealer.hands.append(Hand([two]))
        g.bust_dealer(dealer)
        self.assertEqual(dealer.hands[0].busted, True)
    
    def test_determine_standing(self):
        g = Game(Deck())
        dealer = Player()
        bustedPlayer,winningPlayer, losingPlayer, pushPlayer, twoHandPlayer = Player(), Player(), Player(), Player(), Player()
        winningPlayer.hands.append(Hand([ace]))
        losingPlayer.hands.append(Hand([nine]))
        pushPlayer.hands.append(Hand([ten]))
        bustedPlayer.hands.append(Hand())
        bustedPlayer.hands[0].busted = True
        #twoHand player has winning hand and losing hand
        twoHandPlayer.hands = [Hand([ace]), Hand([nine])]
        dealer.hands.append(Hand([ten]))

        self.assertEqual(g.determine_standing(dealer, [winningPlayer, winningPlayer, winningPlayer]), [[1], [1], [1]])
        self.assertEqual(g.determine_standing(dealer, [losingPlayer, losingPlayer, losingPlayer]), [[-1], [-1], [-1]])
        self.assertEqual(g.determine_standing(dealer, [bustedPlayer, losingPlayer, winningPlayer]), [[-1], [-1], [1]])
        self.assertEqual(g.determine_standing(dealer, [losingPlayer, winningPlayer, pushPlayer]), [[-1], [1], [0]])
        self.assertEqual(g.determine_standing(dealer, [twoHandPlayer, winningPlayer, pushPlayer]), [[1, -1], [1], [0]])
        
        #test with a busted dealer
        g.bust_dealer(dealer)
        self.assertEqual(g.determine_standing(dealer, [winningPlayer, winningPlayer, winningPlayer]), [[1], [1], [1]])
        self.assertEqual(g.determine_standing(dealer, [losingPlayer, losingPlayer, losingPlayer]), [[1], [1], [1]])
        self.assertEqual(g.determine_standing(dealer, [bustedPlayer, losingPlayer, winningPlayer]), [[-1], [1], [1]])
        self.assertEqual(g.determine_standing(dealer, [losingPlayer, winningPlayer, pushPlayer]), [[1], [1], [1]])
        self.assertEqual(g.determine_standing(dealer, [twoHandPlayer, winningPlayer, pushPlayer]), [[1, 1], [1], [1]])

    def test_reset_player_hands(self):
        g = Game(Deck)
        players = []
        p = Player()
        p.hands.append([ace, ace])
        p2 = Player()
        p2.hands.append([ace, ace])
        p2.hands.append([six, six])
        players.append(p)
        players.append(p2)
        g.reset_player_hands(players)
        self.assertEqual(players[0].hands, [])
        self.assertEqual(players[1].hands, [])
if __name__ == '__main__':
    unittest.main(verbosity=2)