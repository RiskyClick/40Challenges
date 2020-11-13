import math


def getnumber(side):
    while True:
        try:
            return float(input("Enter length for side " + side + ": "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...\n")


print("Welcome to the right triangle solver\n")
a = getnumber("A")
b = getnumber("B")

c = round(math.sqrt(a**2 + b**2), 3)
area = round(a * b * .5, 3)

print("Side C is: \t\t" + str(c))
print("Area is: \t\t" + str(area))
