from blackjack.deck import Deck
from blackjack.game import Game

def main():
    while True:
        numPlayers = input("Enter the number of players: ")
        try:
            numPlayers = int(numPlayers)
            break
        except ValueError:
            print("Invalid input! Must be an integer.")

    g = Game(Deck())
    g.play(numPlayers)

main()