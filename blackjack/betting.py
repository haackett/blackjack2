from blackjack.player import Player
from typing import List

def buyin(player : Player, cash: float) -> None:
    player.stack = cash

def bet(player : Player, bet: float) -> None:
    if (player.stack - bet >= 0):
        player.stack = player.stack - bet
        player.bet = bet
    else: 
        return ValueError("Bet is greater than the player's stack")

def clear_bet(player : Player) -> None:
    player.bet = 0

def pay_blackjack(blackjacks : List[bool], players : List[Player]) -> None:
    dealerHasBlackjack = blackjacks[0]
    playerBlackjacks = blackjacks[1:]
    for playerIndex, player in enumerate(playerBlackjacks):
        if player:
            if not dealerHasBlackjack:
                players[playerIndex].stack = players[playerIndex].stack + players[playerIndex].bet * 2.5
            else:
                players[playerIndex].stack = players[playerIndex].stack + players[playerIndex].bet
            clear_bet(players[playerIndex])
def pay_players(playerStandings : List[List[int]], players : List[Player]) -> None:
    for playerIndex, player in enumerate(playerStandings):
        for hand in player:
            if hand == 0:
                players[playerIndex].stack = players[playerIndex].stack + players[playerIndex].bet
            elif hand == 1:
                players[playerIndex].stack = players[playerIndex].stack + players[playerIndex].bet * 2
        clear_bet(players[playerIndex])
    return        

def get_stacks(players : List[Player]) -> List[float]:
    stacks = []
    for player in players:
        stacks.append(player.stack)
    return stacks
