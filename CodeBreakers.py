print("Welcome to the code braker app")

cyfer = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

scram = False
while True:
    while True:
        choice = input('Do you want to scramble or unscramble: ')
        if choice == 'scramble':
            scram = True
            break
        elif choice == 'unscramble':
            scram = False
            break
        else:
            print("Not a valid choice try again")

    if scram:
        print("Enter the message you would like to scramble")
        message = input().strip().lower()
        scrambled = ''
        for c in message:
            if c not in cyfer:
                continue
            else:
                letter = cyfer[c]
                letter += 10
                if letter > 26:
                    letter = letter % 26
                for key, val in cyfer.items():
                    if val == letter:
                        scrambled += key
        print("The scrambled message is:")
        print(scrambled)
    else:
        print("Enter the scrambled message")
        message = input()
        unscramble = ''
        for c in message:
            letter = cyfer[c]
            letter -= 10
            if letter < 1:
                letter = letter % 26
            for key, val in cyfer.items():
                if val == letter:
                    unscramble += key
        print("The decoded message is:")
        print(unscramble)
    if input("Do you want to keep going (y/n): ") == 'n':
        break
