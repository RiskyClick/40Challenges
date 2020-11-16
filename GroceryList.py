import datetime


x = datetime.datetime.now()


def addToList(groceryList):
    groceryList.append(str(input("Type the food you want to add to the Grocery List: ")).title())


def buyItem(groceryList):
    print("Current Grocery List has " + str(len(groceryList)) + " items\n" + str(groceryList))
    while True:
        try:
            item = str(input("What food did you just buy: ")).title()
            groceryList.remove(item)
            print("Removing " + item + " from the list ...")
            break
        except ValueError:
            print(item + " not found in store")


print("\nWelcome to the Grocery List App")
print("The current Date and Time is: " + x.strftime("%x") + "\t" + x.strftime("%X"))
print("You currently have Meat and Cheese in your list\n")
groceryList = ['Meat', 'Cheese']


addToList(groceryList)
addToList(groceryList)
addToList(groceryList)

print("\nHere is your Grocery List:\n " + str(groceryList))
groceryList.sort()
print("here is your Grocery List Sorted: \n" + str(groceryList))

print("\n... Simulating Grocery Shopping ...\n")

buyItem(groceryList)
buyItem(groceryList)
buyItem(groceryList)
out = groceryList.pop()

print("\nSorry we are all out of " + str(out))
groceryList.append(str(input("What would you like instead: ")).title())

print("\nHere is what remains on your Grocery List\n" + str(groceryList))
