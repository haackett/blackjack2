class Player:
    def __init__(self, isDealer= False):
        self.hands = [[]]
        self.isDealer = isDealer

    def bust_hand(self, handIndex=0):
        del self.hands[handIndex]

    def hit(self, card, handIndex=0):
        try:  
            self.hands[handIndex].append(card)
        except:
            self.hands.append([])
            self.hands[handIndex].append(card)
