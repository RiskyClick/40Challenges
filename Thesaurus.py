import random

theDic = {
        "hot": ['hot1', 'hot2', 'hot3', 'hot4'],
        "cold": ['cold1', 'cold2', 'cold3', 'cold4'],
        "happy": ['happy1', 'happy2', 'happy3', 'happy4'],
        "sad": ['sad1', 'sad2', 'sad3', 'sad4'],
    }
print("Welcome to the thesorus")

print("\nThese are the words in the thesorus")
for k in theDic.keys():
    print("\t" + k)


while True:
    choice = input("\nWhat word do you want a thing for: ")
    rand = random.randint(0, 3)
    if choice not in theDic.keys():
        print("thats not an option")
    else:
        print(theDic[choice][rand])
        break
if input("\nWhat you like to see the whole kit? (y/n): ") == 'y':
    for k, v in theDic.items():
        print()
        print(k.title() + " Sysnonims are")
        for i in v:
            print("\t- " + str(i))
