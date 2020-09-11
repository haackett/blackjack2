from blackjack.game import Game
from blackjack.shoe import Shoe

def main():
    while True:
        numPlayers = input("Enter the number of players: ")
        try:
            numPlayers = int(numPlayers)
            break
        except ValueError:
            print("Invalid input! Must be an integer.")

    numDecks = 6
    g = Game(Shoe(numDecks))
    g.play(numPlayers)

main()