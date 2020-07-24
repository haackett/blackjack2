class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.busted = False

    def add_card(self, card):
        self.cards.append(card)
