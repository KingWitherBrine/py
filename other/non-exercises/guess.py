import random

guess = int(input('Please enter a number 0 through 1000: '))
tries = 1
actual = random.randint(0, 1000)

while guess != actual:
    tries += 1
    if guess < actual:
        print("Too small. Please enter another number: ")
        guess = int(input())
    else:
        print("Too big. Please enter another number: ")
        guess = int(input())

print("Found it after", tries, "tries")