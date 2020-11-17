import math


print("\nFactorial Calcualtor\n")

while True:
    try:
        givin = int(input("What number do you want o factorial: "))
        break
    except ValueError:
        print("Not a valid number")

dis = list(range(1, givin + 1))
play = [str(element) for element in dis]
ed = str(givin) + "! = " + "*".join(play)


print("\nHere is the number using the math library:")
print("The factorial of " + str(givin) + " is " + str(math.factorial(givin)))

print("\nHere is the number using my own algo:")
total = 1
for i in range(1, givin + 1):
    total *= i

print("The factorial of " + str(givin) + " is " + str(total))
