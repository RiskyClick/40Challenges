def removeTeacher(teacher):
    print("You dont like a teacher anymore.")
    while True:
        try:
            teachers.remove(str(input("Who is getting the axe: ")).title())
            break
        except ValueError:
            print("That teacher is not in the list. Choose again")


def printTeachers(teachers):
    print("\nYour favorite teachers ranked are: " + str(teachers))
    print("Your favorite teachers alphabeticly are: " + str(sorted(teachers)))
    print("Your favorite teachers in reverse alphabeticly are: " + str(sorted(teachers, reverse=True)))
    print("\nYour top two teachers are: " + teachers[0] + " and " + teachers[1])
    print("Your next two favore teachers are: " + teachers[2] + " and " + teachers[3])
    print("your least favorite is: " + teachers[-1])
    print("You have a total of " + str(len(teachers)) + " in this list\n")


def addTeachers(teachers, place):
    teachers.append(str(input("Who is your " + place + " fav teacher: ").title()))


print("\nWelcome to the Favorite Teachers Program\n")

teachers = []

addTeachers(teachers, "first")
addTeachers(teachers, "second")
addTeachers(teachers, "thrid")
addTeachers(teachers, "fourth")

printTeachers(teachers)

teachers.insert(0, str(input("\nOpps, " + teachers[0] + " is no longer your favorite teacher. Who is your new favorite teacher: ")).title())
printTeachers(teachers)

removeTeacher(teachers)
printTeachers(teachers)
