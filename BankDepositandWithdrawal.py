print("Welcome to pyton first national bank\n")

data = {
    'keith': {
        'password': 'butt',
        'savings': 1000.00,
        'checking': 304968.00,
    }
}


def getNumber():
    while True:
        try:
            num = round(float(input("Enter ammount: ")), 2)
            return num
        except ValueError:
            print("Not a valid number")


def displayInfo(name):
    print("\n\t=====" + name + "=====")
    for i in data[name]:
        if i != 'password':
            print(i + ": $" + str(format(data[name][i], '.2f')))
    print()


def makeChange(name):
    keys = data[name].keys()
    while True:
        getChoice = input("\nWhat account: ")
        if getChoice not in keys:
            print("\nNot an existing account")
            if input("Would you like to add that account? ") == 'y':
                other = getNumber()
                data[name][getChoice] = other
        else:
            depOrWith = input("w or d: ")
            if depOrWith == 'w':
                amount = getNumber()
                data[name][getChoice] -= amount
                break
            elif depOrWith == 'd':
                amount = getNumber()
                data[name][getChoice] += amount
                break
            else:
                print("Not a valid choice")


def addAccount(name):
    password = input("Enter a password: ")
    print("Checking accoout")
    checking = getNumber()
    print("Savings Account")
    savings = getNumber()
    data[name] = {
        'password': password,
        'savings': savings,
        'checking': checking,
    }


def verify(name, password='none'):
    keys = data.keys()
    if name not in keys:
        if input("Would you like to set up an account? ") == 'y':
            addAccount(name)
        else:
            return False
    if password == 'none':
        password = input("Enter password: ")
        if password != data[name]['password']:
            print("Incorrect Password\n")
            return False
        else:
            return True
    return False


while True:
    name = input("Enter username: ")
    if verify(name):
        while True:
            displayInfo(name)
            choice = input("Would you like to make " +
                           "a trasaction?: ")
            if choice == 'n':
                break
            elif choice == 'y':
                makeChange(name)
            else:
                print("Not a vlid choice")
