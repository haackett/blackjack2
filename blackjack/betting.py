from blackjack.player import Player

class Betting():
    def buyin(player: Player, cash: float) -> None:
        player.stack = cash

    def bet(player: Player, bet: float) -> None:
        if (player.stack - bet >= 0):
            player.stack = player.stack - bet
            player.bet = bet
        else: 
            return ValueError("Bet is greater than the player's stack")

    def pay_blackjack():

    def pay_players():
        
        for player in Players:
            #do some stuff for ties

            #do some stuff for wins

    def cashout():
        #call a method in db.py