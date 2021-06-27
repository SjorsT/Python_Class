import random

def dice():
    try:
        x = int(input('Enter the amount of sides: '))
        print(random.randint(1, x))
    except:
        print("Invalid input!")
    dice()

dice()