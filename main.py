from deck import Deck
from game import Game

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