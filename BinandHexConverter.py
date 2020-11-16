def getValidNum():
    while True:
        try:
            num = int(input("Enter the number you would like calculated: "))
            return num
            break
        except ValueError:
            print("Not a valid number. Try again.")


def printNums(theList, start, stop):
    for el in range(start, stop + 1):
        print(theList[el])


print("\nWelcome to the Binary and Hex converter\n")
dec = []
binary = []
hexa = []

upTo = getValidNum()

i = 0
for el in range(0, upTo + 1):
    dec.append(i)
    binary.append(bin(i))
    hexa.append(hex(i))
    i += 1


start = getValidNum()
stop = getValidNum()

print("Decimal values from " + str(start) + " to " + str(stop))
printNums(dec, start, stop)
print("Binary values from " + str(start) + " to " + str(stop))
printNums(binary, start, stop)
print("Hex values from " + str(start) + " to " + str(stop))
printNums(hexa, start, stop)

input = input("Press Enter to see all numbers from 1 to " + str(upTo))
if input == "":
    for el in range(1, upTo + 1):
        print(str(dec[el]) + "\t" + str(binary[el]) + "\t" + str(hexa[el]))
