import math

def getABC():
    while True:
        try:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            print()
            return a, b, c
        except ValueError:
            print("Not valid")


print("\nWelcome to the quadratic solver.\n")

while True:
    try:
        loops = int(input("How many equations do you have? "))
        break
    except ValueError:
        print("Not a valid number. Try again.")

for loop in range(0, loops):
    print("\n\t\tSolving Equation #" + str(loop + 1))
    print("====================================================")
    a, b, c = getABC()
    im = (b**2) - (4*a*c)
    if im < 0:
        first = (-1 * b) / (2*a)
        x1 = "\tX1: " + str(first) + " + " + str(math.sqrt(im * -1) / (2*a)) + "i"
        x2 = "\tX2: " + str(first) + " - " + str(math.sqrt(im * -1) / (2*a)) + "i"
        print(x1)
        print(x2)
    else:
        xPos = "\tX1: " + str(((-1*b) + math.sqrt(((b**2) - (4*a*c)))) / (2*a)) + " + 0i"
        xNeg = "\tX2: " + str(((-1*b) - math.sqrt(((b**2) - (4*a*c)))) / (2*a)) + " - 0i"
        print(xPos)
        print(xNeg)
