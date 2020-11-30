import random

print("Welcome to the coin toss app")
heads = 0
tails = 0
while True:
    try:
        count = int(input("How many flips do you want to do: "))
        break
    except ValueError:
        print("Not a vlaid number")

for i in range(count):
    int = random.randint(1, 10) % 2
    if int == 0:
        print("HEADS")
        heads += 1
    else:
        print("TAILS")
        tails += 1
    if tails == heads:
        print("We have an euqal amount of heads and tails at " + str(heads))

print("\nResults\n")
print("Side\tCount\tPercentage")
print("Heads\t" + str(heads) + '/' + str(count) + '\t'
      '' + str(heads/count*100) + "%")
print("Tails\t" + str(tails) + "/" + str(count) + '\t'
      '' + str(tails/count*100) + "%")
