from typing import List
from card import Card
from deck import Deck
from player import Player
from display import Display

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

class Game:
    def __init__(self, deck: Deck) -> None:
        self.deck = deck

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
        players[playerID].hit(deck.deal())
        
    def hit_dealer(self, dealer: Player, deck: Deck) -> None:
        # Dealer hits until its hand value is >= 17
        while self.hand_value(dealer.hands[0]) < 17:
            dealer.hit(deck.deal())

    def bust_dealer(self, dealer: Player) -> None:
        dealer.hands[0] = [Card('2','Clubs')]
        return

    def determine_winners(self, dealer, players) -> List[bool]:
        winners = []
        for player in players:
            try:
                if self.hand_value(player.hands[0]) > self.hand_value(dealer.hands[0]):
                    winners.append(True)
                    # TODO pay bets with a function here
                elif self.hand_value(player.hands[0]) == self.hand_value(dealer.hands[0]):
                    # we are going to treat this as a loss for now
                    winners.append(False)
                else:
                    winners.append(False)
            except IndexError:
                # IndexError occurs when a player has no hand because they busted
                winners.append(False)
        return winners

    def play(self, numPlayers) -> None:
        d = Display()
        playing = True
        players = []

        self.deck.shuffle()

        while playing:
            
            for i in range(numPlayers):
                players.append(Player())
            
            dealer = Player(isDealer=True)

            for i in range(2):
                for player in players:
                    player.hands[0].append(self.deck.deal())

                dealer.hands[0].append(self.deck.deal())

            for player in players:
                d.display_hand(player.hands[0], players.index(player))
            d.display_dealer_hand(dealer)

            winner_determined = False

            blackjacks = self.check_for_blackjack(players, dealer)
            d.display_blackjacks(blackjacks)

            if blackjacks[0]:
                winner_determined = True
                

            for i in range(len(blackjacks)):
                if blackjacks[i] and not winner_determined:
                    # TODO pay players[i] their bet with a function
                    del players[i].hands[0]

            while not winner_determined:
                for player in players:
                    playerStand, playerBusted = False, False
                    while not playerStand or playerBusted:
                        choice = d.prompt_player(players.index(player))
                        if choice == 'h':
                            self.hit_player(players, players.index(player), self.deck)
                            d.display_hand(player.hands[0], players.index(player))
                            if self.check_if_busted(player, players):
                                d.display_busted(player, players)
                                playerBusted = True
                        elif choice == 's':
                            playerStand = True
                    

                d.display_dealer_hand(dealer, hidden= False)
                self.hit_dealer(dealer, self.deck)
                d.display_dealer_hand(dealer, hidden= False)
                if (self.hand_value(dealer.hands[0]) > 21):
                    self.bust_dealer(dealer)
                    d.display_busted(dealer, players)

                d.display_winning_players(self.determine_winners(dealer, players))

                winner_determined = True
            
            playingPrompt = input("Play again? (Enter a blank line to quit): ")
            if playingPrompt == '':
                playing = False