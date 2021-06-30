import random
import os

class Hangman:

    def __init__(self):
        self.playing = False

    def gameStart(self):
        self.playing = True
        goal = self.getWord()
        playingField = "_" * len(goal)
        print(playingField)
        self.turn(goal)

    def getWord(self):
        wordList = open('./Games/HangmanWords.txt').read().splitlines()
        return random.choice(wordList)

    def turn(self, goal):
        lettersGuessed =[]
        wrongGuess = 0
        
        while self.playing:
            fails = 0
            guess = input("Guess a letter: ")
            if len(guess) != 1:
                print("Please type ONE letter!")
                continue
            elif guess.isalpha() == False:
                print("Only letters are accepted")
                continue
            if guess in lettersGuessed:
                print("Letter has already been guessed!")
            else:
                lettersGuessed += guess
                for char in goal:
                    if char in lettersGuessed:
                        print(char,end="")
                    else:
                        print("_",end="")
                        fails += 1
                if fails == 0:
                    self.gameOver(len(lettersGuessed), True, goal)
                    break
                print("\n")
                if lettersGuessed[len(lettersGuessed)-1] not in goal:
                    wrongGuess += 1
                    self.asciiPrint(wrongGuess, len(lettersGuessed), goal)

    def asciiPrint(self, wrongGuess, tries, goal):
        asciiList = open('./Games/HangmanAscii.txt').read().split(',')
        print(asciiList[wrongGuess-1])
        if wrongGuess >= 7:
            self.gameOver(tries, False, goal)

    def gameOver(self, tries, win, goal):
        self.playing = False
        if win :
            print(f"\nYou won! It took you {tries} tries! The word was: {goal}")
        else:
            print(f"\nYou lost after {tries} tries! The word was: {goal}")

        playAgain = input("Play again? (Y/N): ")
        if playAgain == "Y":
            self.clearConsole()
            self.gameStart()
                
        elif playAgain == "N":
            print("Aight bye")     

        else:
            print("Ok fuck off then with your made up bullshit. This is why we can't have nice things.")       
            
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

if __name__ == "__main__":
    Hangman().gameStart()
