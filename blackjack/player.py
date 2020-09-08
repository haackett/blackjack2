from blackjack.hand import Hand

class Player:
    def __init__(self, isDealer= False):
        self.hands = []
        self.isDealer = isDealer
        self.stack = 0
        self.bet = 0

    def bust_hand(self, handIndex=0):
        self.hands[handIndex].busted = True

    def add_hand(self, cards):
        self.hands.append(Hand(self.bet, cards=cards))
        self.stack = self.stack - self.bet

    def hit(self, card, handIndex=0):
        try:  
            self.hands[handIndex].add_card(card)
        except:
            self.hands.append(Hand(self.bet,cards=[card]))
    
    def split(self, handIndex):
        self.add_hand([self.hands[handIndex].cards[0]])
        del self.hands[handIndex].cards[0]
