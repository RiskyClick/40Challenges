def printRoster(roster):
    print("\n\t\t\tThe starting 5")
    print("\t\tPoint Guard: " + "\t\t" + roster[0])
    print("\t\tShooting Guard: " + "\t\t" + roster[1])
    print("\t\tSmall Forward: " + "\t\t" + roster[2])
    print("\t\tPower Forward: " + "\t\t" + roster[3])
    print("\t\tCenter: " + "\t\t" + roster[4])


print("\nWelcome to the basketball Roster App\n")
roster = []

roster.append(str(input("Who is your point guard: ")).title())
roster.append(str(input("Who is your shooting guard: ")).title())
roster.append(str(input("Who is your small forward: ")).title())
roster.append(str(input("Who is your power forward: ")).title())
roster.append(str(input("Who is your center: ")).title())

printRoster(roster)

print("\nOh no, " + roster[2] + " is hurt.")
out = roster.remove(roster[2])
print("You only have " + str(len(roster)) + " players")
roster.insert(2, str(input("Who will fill the position: ")).title())

printRoster(roster)

print("Okay good luck " + roster[2] + ", you will do great!")
print("You now have a " + str(len(roster)) + " person lineup")
