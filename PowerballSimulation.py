import random
import math


def buyTickets(masterList, lottoNums, tixs):
    bought = []
    for j in range(0, 5):
        bought.append(random.randint(0, lottoRange))
    bought.sort()
    bought.append(random.randint(0, powerRange))
    if bought == lottoNums:
        print("Winning ticket numbers: " + str(bought))
        print("Purchased a total of " + str(tixs) + " tickets!")
        exit()
    else:
        for i in masterList:
            if i == bought:
                print("Alrady picked those numbers.")
                return False
        print(bought)
        masterList.append(bought)
        return True


print("\n================POWER BALL!!!!================")
while True:
    lottoNums = []
    bought = []
    masterList = []
    try:
        lottoRange = int(input("What is the range of the numbers: "))
        powerRange = int(input("What is the range of the power number: "))
        if lottoRange < 0 or powerRange < 0:
            print("Invalid choice")
        else:
            odds = math.factorial(lottoRange)
            odds = odds / (math.factorial(5) * math.factorial(lottoRange - 5))
            odds *= powerRange
            print("The odds are 1 to: " + str(odds))
            buy = int(input("How many tickets do you want to buy: "))
            break
    except ValueError:
        print("Invaild choice.")
for i in range(0, 5):
    lottoNums.append(random.randint(0, lottoRange))
lottoNums.sort()
lottoNums.append(random.randint(0, powerRange))

print("\n==========Tonights winning numbers are============")
print("\t" + str(lottoNums))
input("Press enter to start the purchases")
while True:
    count = 0
    tickets = 1
    while count < buy:
        if buyTickets(masterList, lottoNums, tickets):
            tickets += 1
        else:
            count -= 1
        count += 1
    print("You didnt win.")
    buy = int(input("How many more tickets do you want to buy: "))
    if buy < 1:
        exit()
