from blackjack.player import Player
from typing import List

def buyin(player : Player, cash: float) -> None:
    player.stack = cash

def is_bet_valid(player: Player, bet : float) -> bool:
    if bet < 0:
        return False
    if (player.stack - bet >= 0):
        return True
    else: 
        return False

def bet(player : Player, bet: float) -> None:
        player.stack = player.stack - bet
        player.bet = bet

def pay(player : Player, amount: float) -> None:
    player.stack = player.stack + amount

def clear_bet(player : Player) -> None:
    player.bet = 0


