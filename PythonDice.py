import random


print("\nWelcome to the dice app\n")


def roll(sides):
    outcome = random.randint(1, sides)
    print("\t" + str(outcome))
    return outcome


while True:
    while True:
        try:
            sides = int(input("How many sides: "))
            dice = int(input("How many dice: "))
            if dice < 1 or sides < 1:
                print("Invalid")
            else:
                break
        except ValueError:
            print("Invlaid")
    total = 0
    print("\nYou Rolled " + str(dice) + " with " + str(sides) + " sides")
    print("\n-----The Results-----")
    for i in range(0, dice):
        total += roll(sides)
    print("The total value of the roll is: " + str(total))
    if input("\nRoll again?") != 'y':
        exit()
