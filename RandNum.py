import random

print('Enter the amount of sides')
x = input()

try:
    print(random.randint(1, x))
    x = int(x)
    print(random.randint(1, x))

except:
    print("Invalid input!")

