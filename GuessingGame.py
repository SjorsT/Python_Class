import random
import os

def Game():
    try:
        minGuess = int(input("To guess a number, first pick the minimum value: "))
        maxGuess = int(input("Now pick a maximum value: "))
    except:
        print("Numbers are hard, aren't they?")

    if minGuess > maxGuess:
        print("That's not how numbers work, fuckwad")
        exit()

    goal = random.randint(minGuess, maxGuess)
    tries = 1

    while True:
        try:
            guess = int(input("Input your guess: "))
        except:
            print("That's not a number you dunce.")
            continue
        if guess == goal:
            print("Whoopdeefuckingdoo, you got it. Took you %d tries, you fucking schlomo."%tries)
            playAgain = input("Play again? (Y/N): ")
            if playAgain == "Y":
                clearConsole()
                Game()
                break
            
            elif playAgain == "N":
                print("Aight bye")
                break

            else:
                print("Ok fuck off then with your made up bullshit. This is why we can't have nice things.")
                break
        else:
            tries += 1
            print("Wrong. Try again.")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
            
Game()