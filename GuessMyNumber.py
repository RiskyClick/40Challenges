import random


print("Here is the nubmer guessing game")
theNum = random.randint(1, 100)
atmp = 10

name = input("Whats your name: ").title()
print("\nHi " + name + ", I am thinking of a nubmer between 1 and 100")
while True:
    try:
        guess = int(input("What what number am i thinking of: "))
        if guess == theNum:
            print("\nGood job " + name + ', you guessed the number'
                  'in ' + str(9 - atmp) + " guesses!")
            break
        elif guess < theNum:
            print("That number is too low\n")
        else:
            print("That number is too high\n")
        atmp -= 1
        if atmp == 0:
            print("\nGame over!")
            break
    except ValueError:
        print("That is not a valid number\n")
        atmp -= 1
