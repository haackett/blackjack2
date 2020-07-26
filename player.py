from hand import Hand

class Player:
    def __init__(self, isDealer= False):
        self.hands = []
        self.isDealer = isDealer

    def bust_hand(self, handIndex=0):
        self.hands[handIndex].busted = True

    def add_hand(self):
        self.hands.append(Hand())

    def hit(self, card, handIndex=0):
        try:  
            self.hands[handIndex].add_card(card)
        except:
            self.hands.append(Hand(cards=[card]))
