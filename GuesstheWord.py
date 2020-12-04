import random


data = {
    'fruits': ['apple', 'bannana', 'orange', 'kiwi', 'tomato'],
    'sports': ['baseball', 'football', 'soccer', 'rugby', 'knifefight'],
    'cars': ['ford', 'chevrolet', 'mazda', 'toyota', 'hovercraft'],
    'animals': ['money', 'cat', 'dog', 'chinchila', 'bear'],
}

print("Welome to the word gruessing game")
while True:
    hints = []
    cata = random.choice(list(data.keys()))
    word = data[cata][random.randint(0, len(data[cata]) - 1)]
    arr = ['-'] * len(word)
    print("The catagory is: " + cata + ', there are: '
          '' + str(len(word)) + " letters")
    while True:
        print(' '.join(map(str, arr)))
        guess = input("\nYour Guess: ")
        if word != guess:
            if len(hints) == len(arr) - 1:
                print("Game Over!")
                print("We were looking for: " + word)
                exit()
            else:
                print("\nInccorect")
                print("Here is a hint")
            while True:
                ind = random.randint(0, len(word) - 1)
                if ind not in hints:
                    hints.append(ind)
                    arr[ind] = word[ind]
                    break
        else:
            print("\nCorrect!")
            if 'n' == input("Play again? (y/n): "):
                exit()
            else:
                break
