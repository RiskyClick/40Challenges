print("Welcome to the Ferinhight or however the fuck you spell it to K and C\n")

while True:
    try:
        f = float(input("Enter degree in F: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...\n")

c = round((f - 32) * (5 / 9), 4)
k = round((c + 273.15), 4)

print()
print("Degrees in Fahreneheit: \t" + str(f))
print("Degrees in Celsius: \t\t" + str(c))
print("Degrees in Kelvin: \t\t" + str(k))
