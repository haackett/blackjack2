from typing import List
from card import Card
from deck import Deck
from player import Player

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

    def display_hand(self, hand: List[Card], playerID) -> None:
            print("Player %s's hand is: " % (playerID))
            for card in hand:
                print("%s of %s" % (card.value, card.suit))

    def display_winning_players(self, winners: List[bool]) -> None:
        #TODO include amount of money player won in this print statement
        if winners.count(True) == 0:
            print("The house wins.")
        else:
            for player in winners:
                if player:
                    print("Player %s wins!" % (winners.index(player)))

    def display_dealer_hand(self, dealer: Player, hidden=True) -> None:
        print("The dealer hand is: ")
        if hidden:
            print("%s of %s" % (dealer.hands[0][0].value, dealer.hands[0][0].suit))
        else:
            for card in dealer.hands[0]:
                print("%s of %s" % (card.value, card.suit))

    def prompt_player(self, playerID: int) -> str:
        choice = input("Player " + str(playerID) + ", would you like to hit ('h') or stand ('s')").lower()
        while choice not in ['h','s','hit','stand']:
            choice = input("Please enter 'h' or 's'")

        if choice in ['h','hit']:
            return 'h'
        elif choice in ['s','stand']:
            return 's'