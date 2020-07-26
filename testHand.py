from hand import Hand
import unittest
from card import Card

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

    def test_add_card(self):
        h = Hand()
        h.add_card(two)
        self.assertEqual(h.cards, [two])

    def test_hand_value(self):
        h = Hand()
        
        #test all non-ace cards in hands of 2
        h.cards = [two,three]
        self.assertEqual(h.hand_value(), 5)
        h.cards = [four,five]
        self.assertEqual(h.hand_value(), 9)
        h.cards = [six,seven]
        self.assertEqual(h.hand_value(), 13)
        h.cards = [eight,nine]
        self.assertEqual(h.hand_value(), 17)
        h.cards = [ten,jack]
        self.assertEqual(h.hand_value(), 20)
        h.cards = [queen,king]
        self.assertEqual(h.hand_value(), 20)
        
        #test a hand with val > 21
        h.cards = [queen,queen,queen]
        self.assertEqual(h.hand_value(), 30)

        #test hands of 3 cards
        h.cards = [two,two,two]
        self.assertEqual(h.hand_value(), 6)
        h.cards = [two,three,four]
        self.assertEqual(h.hand_value(), 9)
        
        #test hands of size 4+ 
        for i in range(4, 100):
            h.cards = []
            h.cards += ([two] * i)
            self.assertEqual(h.hand_value(), 2 * i)
       
        #test hands with one ace
        h.cards = [ace, two]
        self.assertEqual(h.hand_value(), 13)
        h.cards = [ace, queen]
        self.assertEqual(h.hand_value(), 21)

        #test hand with 2+ aces
        h.cards = [ace, ace]
        self.assertEqual(h.hand_value(), 12)
        h.cards = [ace,ace,ace]
        self.assertEqual(h.hand_value(), 13)
        h.cards = [ace,ace,ace,ace]
        self.assertEqual(h.hand_value(), 14)
        h.cards = [queen, queen, queen, ace]
        self.assertEqual(h.hand_value(), 31)
        h.cards = [ace,ace,ace,ace,queen]
        self.assertEqual(h.hand_value(), 14)
        h.cards = [ace,ace,ace,ace,queen,king]
        self.assertEqual(h.hand_value(), 24)



if __name__ == '__main__':
    unittest.main(verbosity=2)