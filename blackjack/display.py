from typing import List
from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player import Player
from blackjack.hand import Hand
from blackjack.betting import is_bet_valid

class Display:
    
    def display_busted(self, player: Player, players: List[Player]) -> None:
        #TODO implement this method for multiple hands per player
        if player.isDealer:
            print("The dealer has busted!")
        else:
            print("Player %s has busted!" % (players.index(player)))

    def display_blackjacks(self, blackjacks: List[bool]) -> None:
        # Dealer is index 0, players are index 1 : n 
        if blackjacks[0]:
            print("The dealer has blackjack.")
        for i in range(1, len(blackjacks)):
            if blackjacks[i]:
                print("Player %s has blackjack." % (i - 1))

    def display_hand(self, hand: Hand, playerID) -> None:
            print("Player %s's hand is: " % (playerID))
            for card in hand.cards:
                print("%s of %s" % (card.value, card.suit))

    def display_winning_players(self, winners: List[List[int]]) -> None:
        #TODO include amount of money player won in this print statement
        for playerIndex, player in enumerate(winners):
            for handIndex, hand in enumerate(player):
                if hand == 1:
                    print("Player %s hand %s wins!" % (playerIndex, handIndex))
                elif hand == 0:
                    print("Player %s hand %s pushes." % (playerIndex, handIndex))
                if hand == -1:
                    print("Player %s hand %s loses." % (playerIndex, handIndex))
                    
    def display_dealer_hand(self, dealer: Player, hidden=True) -> None:
        print("The dealer hand is: ")
        if hidden:
            print("%s of %s" % (dealer.hands[0].cards[0].value, dealer.hands[0].cards[0].suit))
        else:
            for card in dealer.hands[0].cards:
                print("%s of %s" % (card.value, card.suit))

    def get_input(self, prompt) -> None:
        return input(prompt)

    def prompt_player(self, playerID: int, splittable=False) -> str:
        if splittable:
            choice = self.get_input("Player " + str(playerID) + ", would you like to hit ('h'), stand ('s'), or split ('p')").lower()
            while choice not in ['h','s', 'p', 'hit','stand', 'split']:
                choice = input("Please enter 'h' or 's' or 'p'")
            if choice in ['h','hit']:
                return 'h'
            elif choice in ['s','stand']:
                return 's'
            elif choice in ['p', 'split']:
                return 'p'
        else:
            choice = self.get_input("Player " + str(playerID) + ", would you like to hit ('h') or stand ('s')").lower()
            while choice not in ['h','s','hit','stand']:
                choice = input("Please enter 'h' or 's'")
            if choice in ['h','hit']:
                return 'h'
            elif choice in ['s','stand']:
                return 's'

    def prompt_player_for_bet(self, player : Player, players : List[Player]) -> float:
            bet = self.get_input("Player " + str(players.index(player)) + ", what would you like to bet?")
            try:
                if is_bet_valid(player, float(bet)):
                    return bet
                else: 
                    print("Please enter a bet less than or equal to " + str(player.stack))
                    return -1
            except ValueError:
                print("Please enter a number.")
                return -1
                
    def display_stacks(self, players) -> None:
        for playerIndex, player in enumerate(players):
            print("Player " + str(playerIndex) + "'s stack: $" + str(player.stack))

    def display_changing_shoe(self) -> None:
        print("Last deck reached. Getting new shoe...")

