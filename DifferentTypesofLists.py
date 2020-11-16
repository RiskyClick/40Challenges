def printer(data, title):
    print("the variable " + title + " is a " + str(type(data)))
    print("it contains the elements: " + str(data))
    print("The element " + str(data[0]) + " is a " + str(type(data[0])))
    print()


print("\t\tSummary Table\n")
numStrings = ['15', '100', '55', '45']
numInts = [15, 200, 55, 45]
numFloats = [2.2, 5.0, 1.245]
numLists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


printer(numStrings, "numStrings")
printer(numInts, "numInts")
printer(numFloats, "numFloats")
printer(numLists, "numLists")

numStrings.sort()
numInts.sort()

print("Now sorting numStrings and numInts ... ")
print("Sorted numStrings: " + str(numStrings))
print("Sorted numInts: " + str(numInts))
print("\nStrings are sorted alfabetically while integers are sorted numerically!")
