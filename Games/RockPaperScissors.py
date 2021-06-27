import random

class RockPaperScissors:

    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.points = 0
        self.compPoints = 0
        self.goal = 1
    
    def gameStart(self):
        self.points = 0
        self.compPoints = 0
        self.goal = self.getGoal()
        self.playerTurn()

    def playerTurn(self):
        choice = self.getChoice()
        compChoice = self.getCompChoice()
        print(f"The computer chose: {compChoice}")
        result = self.determineWinner(choice, compChoice)
        self.finishGame(result)

    def getChoice(self):
        choice = str.lower(input("Pick Rock, Paper or Scissors: "))
        if choice != "rock" and choice != "paper" and choice != "scissors":
            print("There's three options to choose from, literal 5 year olds can play this game. How can one person be this stupid?")
            self.getChoice()
        else:
            return choice

    def getCompChoice(self):
        return self.options[random.randint(0, 2)]

    def getGoal(self):
        try:
            goal = int(input("First to how many points: "))
            return goal
        except:
            print("Input a number, you retard")
            self.getGoal()

    def determineWinner(self, choice, compChoice):
        if choice == compChoice:
            return "tie"
        elif choice == "scissors":
            if compChoice == "paper":
                return "win"
            elif compChoice == "rock":
                return "loss"
        elif choice == "paper":
            if compChoice == "rock":
                return "win"
            elif compChoice == "scissors":
                return "loss"
        elif choice == "rock":
            if compChoice == "scissors":
                return "win"
            elif compChoice == "paper":
                return "loss"

    def finishGame(self, result):
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You get a point!")
            self.points += 1
        else:
            print("The computer gets a point!")
            self.compPoints += 1

        if(self.points >= self.goal):
            print("You win!")
            self.gameEnd()
        elif(self.compPoints >= self.goal):
            print("The computer wins!")
            self.gameEnd()
        else:
            print(f"You: {self.points} - Computer: {self.compPoints}")
            self.playerTurn()

    def gameEnd(self):
        playAgain = input("Play again? (Y/N): ")
        if playAgain == "Y":
            self.gameStart()
        elif playAgain == "N":
            print("Aight bye")
            return
        else:
            print("That's not one of the options, you braindead horsefucker")
            self.gameEnd()
        

        



if __name__ == "__main__":
    RockPaperScissors().gameStart()