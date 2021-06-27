import time
import os
from Games.RolePlayingGame import RolePlayingGame
from Games.GuessingGame import GuessingGame
from Games.RockPaperScissors import RockPaperScissors

class Menu:

    def chooseMenu(self):
        game1 = RolePlayingGame()
        game2 = GuessingGame()
        game3 = RockPaperScissors()

        x = input("Please select your program by using the assigned numbers:\n1: Roleplaying Game\n2: Guessing Game\n3: Rock paper scissors\nType 'exit' to exit the program\n")
        if x == "exit":
            self.exitProgram()
        elif x == "1":
            game1.gameStart()
        elif x == "2":
            game2.gameStart()
        elif x == "3":
            game3.gameStart()
        else:
            print("That program does not exist yet!")
        
        self.chooseMenu()

    def exitProgram(self):
        print("Aight I'mma head out")
        time.sleep(3)
        self.clearConsole()
        exit()

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

if __name__ == "__main__":
    Menu().chooseMenu()

