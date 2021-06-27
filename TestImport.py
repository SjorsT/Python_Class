import sys

sys.path.insert(1, "./Games")

from RolePlayingGame import RolePlayingGame
from GuessingGame import GuessingGame

game1 = RolePlayingGame()
game2 = GuessingGame()

x = int(input("What you wanna do"))
if x == 1:
    game1.gameStart()
elif x == 2:
    game2.gameStart()