print("Yes or no polling\n")
poll = {}
no = 0
yes = 0
issue = input("What do you want to vote on: ")
voters = int(input("How many people do you want to vote: "))

for i in range(0, voters):
    name = input("\nWhats your name: ").title().strip()
    if name not in poll.keys():
        choice = input("Should we " + issue + ": ").title()
        if choice != 'Yes' and choice != 'No':
            print("Not and option but whatever\n")
            poll[name] = choice
        else:
            print("Thanks " + name + " your vote has been counted\n")
            poll[name] = choice
    else:
        print("They heave already voted")
                    

for k, v in poll.items():
    if v == 'Yes':
        yes += 1
    elif v == 'No':
        no += 1
print("\nThe Resutls")
print("YES: " + str(yes) + "\tNO: " + str(no))
if yes > no:
    print("Yes votes win")
elif no > yes:
    print("No votes win")
else:
    print("ITS A TIE!!")

if input("\nEnter admin password for resutls: ") == 'admin':
    for k, v in poll.items():
        print(k + "\t" + v)
