import random
import os

class GuessingGame:

    def gameStart(self):
        try:
            minGuess = int(input("To guess a number, first pick the minimum value: "))
            maxGuess = int(input("Now pick a maximum value: "))
        except:
            print("Numbers are hard, aren't they?")
            return

        if minGuess > maxGuess:
            print("That's not how numbers work, fuckwad")
            return

        goal = random.randint(minGuess, maxGuess)
        tries = 1

        while True:
            try:
                guess = int(input("Input your guess: "))
            except:
                print("That's not a number you dunce.")
                continue
            if guess == goal:
                print(f"Whoopdeefuckingdoo, you got it. Took you {tries} tries, you fucking schlomo.")
                playAgain = input("Play again? (Y/N): ")
                if playAgain == "Y":
                    self.clearConsole()
                    self.gameStart()
                    break
                
                elif playAgain == "N":
                    print("Aight bye")
                    break

                else:
                    print("Ok fuck off then with your made up bullshit. This is why we can't have nice things.")
                    break
            elif guess > goal:
                print("Guessed too high!")
            else:
                print("Guessed too low!")
            tries += 1

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

if __name__ == "__main__":
    GuessingGame().gameStart()
                