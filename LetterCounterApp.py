count = 0
print("Welcome to the letter counter app\n")
name = input("Whats your name: ").title().strip()
print("Hey " + name)
message = input("\nEnter a message: \n")
message = message.upper()
letter = input("\nWhat letter do you want me to count: ")
letter = letter.upper()
count = message.count(letter)
print("\n" + name + ", the message has " + str(count) + " " + letter + "'s in it.")
