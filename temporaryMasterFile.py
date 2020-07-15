from typing import List
import random

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Clubs','Diamonds','Hearts','Spades']

valueConversions = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10,
    'Ace' : 11
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
class Deck:
    def __init__(self):
        self._cards = [Card(value,suit) for value in values for suit in suits]
    
    def deal(self):
        return self._cards.pop()

    def shuffle(self):
        cards = []
        while (len(self._cards) > 0):
            randIndex = random.randint(0, len(self._cards) - 1)
            cards.append(self._cards[randIndex])
            del self._cards[randIndex]

        self._cards = cards

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

class Game:
    def __init__(self, deck: Deck) -> None:
        pass

    def hand_value(self, hand: List[Card]) -> int:
        """ Returns the integer value of a hand, evaluating aces as 11 whenever optimal."""

        values = []
        for card in hand:
            values.append(valueConversions[card.value])

        while (values.count(11) != 0):
            if (self.sum_values(values) > 21):
                values[values.index(11)] = 1
            else: 
                break

        return self.sum_values(values)

    def sum_values(self, values: List[int]) -> int:
        """ Helper method for hand_value. Returns the sum of all values in a List"""

        sum = 0
        for value in values:
            sum = value + sum
            
        return sum

    def check_if_busted(self, player: Player, players: List[Player]) -> bool:
        # TODO implement this method for multiple hands per player
            if (self.hand_value(player.hands[0]) > 21):
                self.display_busted(player, players)
                player.bust_hand(0)
                return True
            return False

    def check_for_blackjack(self, players: List[Player], dealer: Player) -> List[bool]:
        blackjacks = []
        if self.hand_value(dealer.hands[0]) == 21:
            blackjacks.append(True)
        else:
            blackjacks.append(False)
        for player in players:
            if self.hand_value(player.hands[0]) == 21:
                blackjacks.append(True)
            else:
                blackjacks.append(False)
        return blackjacks

    


    def hit_player(self, players: List[Player], playerID, deck) -> None:
        # TODO make this method work for multiple hands per player
        players[playerID].hit(deck.deal())
        self.display_hand(players[playerID].hands[0], players[playerID], players)
        if (self.check_if_busted(players[playerID], players)):
            return
        else:
            self.prompt_player(players, playerID, deck)
            


    def hit_dealer(self, dealer: Player, deck: Deck) -> None:
        # Dealer hits until its hand value is >= 17
        while self.hand_value(dealer.hands[0]) < 17:
            dealer.hit(deck.deal())
            self.display_dealer_hand(dealer, hidden=False)
        # If dealer busts, set hand_value to 2 so every player not busted will win
        if (self.hand_value(dealer.hands[0]) > 21):
            dealer.hands[0] = [Card('2','Clubs')]

    
    def determine_winners(self, dealer, players) -> None:
        dealerWins = True
        for player in players:
            try:
                if self.hand_value(player.hands[0]) > self.hand_value(dealer.hands[0]):
                    dealerWins = False
                    self.display_winning_players(player, players)
                    # TODO pay bets with a function here
            except IndexError:
                # IndexError occurs when a player has no hand because they busted
                pass
        if dealerWins:
            self.display_dealer_win()

    def play(self, numPlayers) -> None:
        playing = True
        players = []

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            for i in range(numPlayers):
                players.append(Player())
            
            dealer = Player(isDealer=True)

            for i in range(2):
                for player in players:
                    player.hands[0].append(self.deck.deal())

                dealer.hands[0].append(self.deck.deal())

            for player in players:
                self.display_hand(player.hands[0], player, players)
            self.display_dealer_hand(dealer)

            winner_determined = False

            blackjacks = self.check_for_blackjack(players, dealer)
            self.display_blackjacks(blackjacks)

            if blackjacks[0]:
                winner_determined = True
                

            for i in range(len(blackjacks)):
                if blackjacks[i] and not winner_determined:
                    # TODO pay players[i] their bet with a function
                    del players[i].hands[0]

            while not winner_determined:
                for player in players:
                    self.prompt_player(players, players.index(player), self.deck)
                    

                self.display_dealer_hand(dealer, hidden= False)
                self.hit_dealer(dealer, self.deck)
                self.determine_winners(dealer, players)
                winner_determined = True
            
            playing = False
                
class Display:

    def display_busted(self, player: Player, players: List[Player]) -> None:
        #TODO implement this method for multiple hands per player
        print("Player %s has busted!" % (players.index(player)))

    def display_blackjacks(self, blackjacks: List[bool]) -> None:
        # Dealer is index 0, players are index 1 : n 
        if blackjacks[0]:
            print("The dealer has blackjack.")
        for i in range(1, len(blackjacks)):
            if blackjacks[i]:
                print("Player %s has blackjack." % (i - 1))

    def display_hand(self, hand: List[Card], player, players: List[Player]) -> None:
            print("Player %s's hand is: " % (players.index(player)))
            for card in hand:
                print("%s of %s" % (card.value, card.suit))

    def display_winning_players(self, player, players) -> None:
        #TODO include amount of money player won in this print statement
        print("Player %s wins!" % (players.index(player)))

    def display_dealer_win(self) -> None:
        print("The house wins.")

    def display_dealer_hand(self, dealer: Player, hidden=True) -> None:
        print("The dealer hand is: ")
        if hidden:
            print("%s of %s" % (dealer.hands[0][0].value, dealer.hands[0][0].suit))
        else:
            for card in dealer.hands[0]:
                print("%s of %s" % (card.value, card.suit))

    def prompt_player(self, players: List[Player], playerID: int, deck: Deck) -> None:
        choice = input("Player " + str(playerID) + ", would you like to hit ('h') or stand ('s')").lower()
        while choice not in ['h','s','hit','stand']:
            choice = input("Please enter 'h' or 's'")

        if choice in ['h','hit']:
            self.hit_player(players, playerID, deck)
            
        if choice in ['s','stand']:
            return