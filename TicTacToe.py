import random

exBoard = "-----------------\n|| 1 || 2 || 3 ||\n-----------------\n"
exBoard += "|| 4 || 5 || 6 ||\n-----------------\n|| 7 || 8 || 9 ||\n"
exBoard += "-----------------\n"


data = {
    '1': 20,
    '2': 25,
    '3': 30,
    '4': 54,
    '5': 59,
    '6': 64,
    '7': 88,
    '8': 93,
    '9': 98,
}

lineB = [17, 34, 51, 68, 85, 102]

player = False

winCombos = [[20, 25, 30],
             [54, 59, 64],
             [88, 93, 98],
             [20, 59, 98],
             [30, 59, 88],
             [20, 54, 88],
             [25, 59, 93],
             [30, 64, 98]]


def clearBoard():
    return ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                 '-', '-', '-', '-', '|', '|', ' ', '_', ' ', '|', '|', ' ',
                 '_', ' ', '|', '|', ' ', '_', ' ', '|', '|', '-', '-', '-',
                 '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                 '-', '-', '|', '|', ' ', '_', ' ', '|', '|', ' ', '_', ' ',
                 '|', '|', ' ', '_', ' ', '|', '|', '-', '-', '-', '-', '-',
                 '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                 '|', '|', ' ', '_', ' ', '|', '|', ' ', '_', ' ', '|', '|',
                 ' ', '_', ' ', '|', '|', '-', '-', '-', '-', '-', '-', '-',
                 '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']


def displayBoard():
    print(exBoard)
    for c, v in enumerate(gameBoard):
        if c in lineB:
            print()
        print(v, end='')
    print()


def onlyGameBoard():
    for c, v in enumerate(gameBoard):
        if c in lineB:
            print()
        print(v, end='')
    print()


def makeChoice(xBank, yBank, bank):
    while True:
        choice = input("Enter choice: ")
        if data.get(choice) is not None:
            if data[choice] in bank:
                print("SPOT TAKEN CHOOSE AGIN!")
            else:
                bank.append(data[choice])
                if len(bank) % 2 == 0:
                    gameBoard[data[choice]] = 'X'
                    xBank.append(data[choice])
                    xBank.sort()
                    player = False
                else:
                    gameBoard[data[choice]] = 'O'
                    yBank.append(data[choice])
                    yBank.sort()
                    player = True
                break
        else:
            print("NOT A NUMBER 1 - 9")


while True:
    print("\nWelcome to Tic Tac Toe")
    if input("Would you like to play a game? ") == 'no':
        exit()
    else:
        gameBoard = clearBoard()
        currentGame = True
        bank = []
        xBank = []
        yBank = []
        if random.randint(0, 100) % 2 == 0:
            print("\nPlayer X goes first!")
            bank.append(10000)
        else:
            print("\nPlayer O goes first!")
        while currentGame:
            displayBoard()
            makeChoice(xBank, yBank, bank)
            for i in winCombos:
                if set(i).issubset(set(xBank)):
                    print("PLAYER X WINS!")
                    onlyGameBoard()
                    print("PLAYER X WINS!\n")
                    currentGame = False
                elif set(i).issubset(set(yBank)):
                    print("PLAYER O WINS!")
                    onlyGameBoard()
                    print("PLAYER O WINS!\n")
                    currentGame = False
            if len(bank) > 9:
                displayBoard()
                print("ITS A TIE!\n")
                break
