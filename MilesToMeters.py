print("Miles per hour to Meters per second convertion\n")

while True:
    try:
        miles = float(input("Whats your miles per hour: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...\n")
        
meters = round(miles / 2.237, 2)
print("Your speed in MPS is: " + str(meters))
