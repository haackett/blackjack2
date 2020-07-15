import unittest
import random
from temporaryMasterFile import Game
from temporaryMasterFile import Card
from temporaryMasterFile import Player
from typing import List

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


    def test_sum_values(self):
        #create a Game with an empty Deck arg
        g = Game([])
        self.assertEqual(g.sum_values([1]), 1)

        #check communitivity
        temp = [random.randint(0,100) for i in range(100)]
        ints = temp.copy()
        random.shuffle(temp)
        shuffled_ints = temp.copy()
        self.assertEqual(g.sum_values(ints), g.sum_values(shuffled_ints))

        #test associativity
        temp = [2] * random.randint(0,100)
        list_of_twos = temp.copy()
        list_of_ones = [1] * len(temp) * 2
        self.assertEqual(g.sum_values(list_of_twos), g.sum_values(list_of_ones))

        #test the additive identity
        temp = [random.randint(0,100) for i in range(100)]
        ints = temp.copy()
        ints_and_zeros = temp.copy()
        ints_and_zeros += ([0] * len(temp))
        self.assertEqual(g.sum_values(ints), g.sum_values(ints_and_zeros))

    def test_hand_value(self):
        #create a Game with an empty Deck arg
        g = Game([])
        
        #test all non-ace cards in hands of 2
        self.assertEqual(g.hand_value([two,three]), 5)
        self.assertEqual(g.hand_value([four,five]), 9)
        self.assertEqual(g.hand_value([six,seven]), 13)
        self.assertEqual(g.hand_value([eight,nine]), 17)
        self.assertEqual(g.hand_value([ten,jack]), 20)
        self.assertEqual(g.hand_value([queen,king]), 20)
        
        #test a hand with val > 21
        self.assertEqual(g.hand_value([queen,queen,queen]), 30)

        #test hands of 3 cards
        self.assertEqual(g.hand_value([two,two,two]), 6)    
        self.assertEqual(g.hand_value([two,three,four]), 9)
        
        #test hands of size 4+ 
        for i in range(4, 100):
            hand = []
            hand += ([two] * i)
            self.assertEqual(g.hand_value(hand), 2 * i)
       
        #test hands with one ace
        self.assertEqual(g.hand_value([ace, two]), 13)
        self.assertEqual(g.hand_value([ace, queen]), 21)

        #test hand with 2+ aces
        self.assertEqual(g.hand_value([ace, ace]), 12)
        self.assertEqual(g.hand_value([ace,ace,ace]), 13)
        self.assertEqual(g.hand_value([ace,ace,ace,ace]), 14)
        self.assertEqual(g.hand_value([queen, queen, queen, ace]), 31)
        self.assertEqual(g.hand_value([ace,ace,ace,ace,queen]), 14)
        self.assertEqual(g.hand_value([ace,ace,ace,ace,queen,king]), 24)


    def test_check_if_busted(self):
            p = Player()
            players = [p]

            g = Game([])
            cards = [queen, queen, queen]
            p.hands[0] = cards

            g.check_if_busted(p, players)
            
            #test length of p.hands. We expect 0 as check_if_busted should have
            #deleted the only list in p.hands
            self.assertEqual(len(p.hands), 0)

    def test_check_for_blackjack(self):
          g = Game([])
          players = [Player()]

          #check for dealer with blackjack and 1 player without blackjack
          players[0].hands[0] = (two, three)        
          dealer = Player(isDealer=True)
          dealer.hands[0] = ([ace, queen])

          self.assertEqual(g.check_for_blackjack(players, dealer), [True, False])

          #check for dealer with BJ and 1 player with BJ
          players[0].hands[0] = [ace, queen]
          self.assertEqual(g.check_for_blackjack(players, dealer), [True, True])

          #check for dealer without BJ and 1 player with BJ
          dealer.hands[0] = [two, three]
          self.assertEqual(g.check_for_blackjack(players, dealer), [False, True])

          #check for dealer without BJ and 2 players with BJ
          players.append(Player())
          players[1].hands[0] = ([ace, queen])
          self.assertEqual(g.check_for_blackjack(players, dealer), [False, True, True])

          #check for dealer without BJ, 1 player with BJ, and 1 player without
          players[1].hands[0] = [two, three]
          self.assertEqual(g.check_for_blackjack(players, dealer), [False, True, False])

if __name__ == '__main__':
    unittest.main(verbosity=2)