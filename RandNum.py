import random

print('Enter the amount of sides')
x = input()

try:
    x = int(x)
    print(random.randint(1, x))

except:
    print("Invalid input!")

