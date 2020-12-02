print("Voter Reg App")

name = input("Whats your name: ").title()
while True:
    try:
        age = int(input("How old are you: "))
        if age < 18:
            print("Not old enough to vote.")
            exit(0)
        else:
            break
    except ValueError:
        print("Not a valid number")

print("Congraz " + name + ",  you can reg to vote!")
print("Here are your choices")
print("\tRepublican\n\tDemocratic\n\tIndependent\n\tLibratarian\n\tGreen")
while True:
    try:
        choice = input("What party are you joining?: ").title()
        if choice == 'Republican':
            print("Major Party")
            break
        elif choice == 'Democratic':
            print("Major Party")
            break
        elif choice == 'Independent':
            print("Minor Party")
            break
        elif choice == 'Libertarian':
            print("Minor Party")
            break
        elif choice == 'Green':
            print("Minor Party")
            break
        else:
            print("party not in list")
    except ValueError:
        print("I dont think anything is going to be printied here")
