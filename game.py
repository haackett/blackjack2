from typing import List
from card import Card
from deck import Deck
from player import Player
from display import Display
from hand import Hand

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

    def check_if_busted(self, player: Player) -> None:
        for index, hand in enumerate(player.hands):
            if (hand.hand_value() > 21):
                player.bust_hand(index)
        
    def check_for_blackjack(self, players: List[Player], dealer: Player) -> List[bool]:
        blackjacks = []
        if dealer.hands[0].hand_value() == 21:
            blackjacks.append(True)
        else:
            blackjacks.append(False)
        for player in players:
            if player.hands[0].hand_value() == 21:
                blackjacks.append(True)
            else:
                blackjacks.append(False)
        return blackjacks

    def hit_player(self, player, handIndex, deck) -> None:
        player.hit(deck.deal(), handIndex)
        
    def hit_dealer(self, dealer: Player, deck: Deck) -> None:
        # Dealer hits until its hand value is >= 17
        while dealer.hands[0].hand_value() < 17:
            dealer.hit(deck.deal())

    def bust_dealer(self, dealer: Player) -> None:
        dealer.bust_hand()

    def determine_standing(self, dealer, players) -> List[List[int]]:
        #1 : win, 0 : tie, -1 : loss
        dealerScore = dealer.hands[0].hand_value()
        standingOfPlayers = []
        for player in players:
            standingOfHands = []
            for hand in player.hands:
                if not hand.busted:
                    if dealer.hands[0].busted == True:
                        standingOfHands.append(1)
                    else:    
                        if hand.hand_value() > dealerScore:
                            standingOfHands.append(1)
                        elif hand.hand_value() == dealerScore:
                            standingOfHands.append(0)
                        else:
                            standingOfHands.append(-1)
                else:
                    standingOfHands.append(-1)
            standingOfPlayers.append(standingOfHands)
        return standingOfPlayers

    def play(self, numPlayers) -> None:
        d = Display()
        playing = True
        players = []
        
        for i in range(numPlayers):
                players.append(Player())
            

        self.deck.shuffle()

        while playing:
            
            dealer = Player(isDealer=True)

            for i in range(2):
                for player in players:
                    player.hit(self.deck.deal())

                dealer.hit(self.deck.deal())

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
                            self.hit_player(player, 0, self.deck)
                            d.display_hand(player.hands[0], players.index(player))
                            if self.check_if_busted(player):
                                d.display_busted(player, players)
                                playerBusted = True
                        elif choice == 's':
                            playerStand = True
                    

                d.display_dealer_hand(dealer, hidden= False)
                self.hit_dealer(dealer, self.deck)
                d.display_dealer_hand(dealer, hidden= False)
                if (dealer.hands[0].hand_value() > 21):
                    self.bust_dealer(dealer)
                    d.display_busted(dealer, players)

                d.display_winning_players(self.determine_standing(dealer, players))

                winner_determined = True
            
            playingPrompt = input("Play again? (Enter a blank line to quit): ")
            if playingPrompt == '':
                playing = False
            print("\n\n\n\n\n")