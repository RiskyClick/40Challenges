import random


def theBrain(ych, cch):
    print("\t" + name + ": " + str(ych))
    if cch == 1:
        print("\tComputer: Rock")
        if ych == 'Rock':
            print("\tIts a tie. How boring.")
            return 3
        elif ych == 'Paper':
            print("\tPaper covers rock. You win!")
            return 1
        elif ych == 'Scissors':
            print("\tRock crushes Scissors. You Lose!")
            return 2
        else:
            print("\tNot a valid choice. You Lose!")
            return 2
    elif cch == 2:
        print("\tComputer: Paper")
        if ych == 'Rock':
            print("\tPaper covers rock. You lose!")
            return 2
        elif ych == 'Paper':
            print("\tIts a tie")
            return 3
        elif ych == 'Scissors':
            print("\tScissors cut paper. You win!")
            return 1
        else:
            print("\tNot a valid choice. You Lose!")
            return 2
    else:
        print("\tComputer: Scissors")
        if ych == 'Rock':
            print("\tRock crushes scissors. You win!")
            return 1
        elif ych == 'Paper':
            print("\tScissors cut paper. You Lose!")
            return 2
        elif ych == 'Scissors':
            print("\tIts a tie!")
            return 3
        else:
            print("\tNot a valid choice. You Lose!")
            return 2


print("Welcome to rock paper sisors")
name = input("Whats your name: ").title()
yourScore = 0
compScore = 0

while True:
    try:
        rounds = int(input("How many rounds do you want to play: "))
        break
    except ValueError:
        print("Thats not a vaild number")
for i in range(1, rounds + 1):
    print("\nRound " + str(i))
    print(name + ": " + str(yourScore) + "\tComputer: " + str(compScore))
    yourChoice = input("Pick Rock, Paper, or Scissors: ").title()
    compChoice = random.randint(1, 3)
    result = theBrain(yourChoice, compChoice)
    if result == 1:
        yourScore += 1
    elif result == 2:
        compScore += 1

print("\nFinal Game Results")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(yourScore))
print("\tComputer Score: " + str(compScore))
if compScore > yourScore:
    print("\tWinner: Computer!")
elif yourScore > compScore:
    print("\tWinner: " + name + "!")
else:
    print("\tITS A TIE!")
