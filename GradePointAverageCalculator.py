print("Welcome to GPA calculator")
name = str(input("Whats your name: ")).title()
size = int(input("How many grades do you want calculated: "))
grades = []
sum = 0
for i in range(size):
    grades.append(int(input("Enter grade: ")))

grades.sort(reverse=True)
print("Grades from best to worst: ")
for el in grades:
    sum = sum + el
    print("\t" + str(el))

print(name + "'s grade summary")
print("\tTotal number of grades: " + str(size))
print("\tBest grade: " + str(grades[0]))
print("\tWorst grade: " + str(grades[size - 1]))
print("\tAverage GPA: " + str(sum / size))

des = int(input("What is your preferd score: "))
needed = (des * (size + 1)) - sum
print("Good luck " + str(name))
print("you will need to score a " + str(needed) + ' on your next assingment to'
      ' gain a GPA of ' + str(des))

print("Lets see what your grade would have been if you studdyed more")
while True:
    find = int(input("What score do you want to change: "))
    if find in grades:
        print("WE ARE IN HERE")
        pos = grades.index(find)
        False
        break
    else:
        print(str(find) + " is not in the grade book.")
grades[pos] = int(input("What do you want to change " + str(find) + " too: "))
grades.sort(reverse=True)
new = 0
print("Grades from best to worst: ")
for el in grades:
    new += el
    print("\t" + str(el))

print(name + "'s new grade summary")
print("\tTotal number of grades: " + str(size))
print("\tBest grade: " + str(grades[0]))
print("\tWorst grade: " + str(grades[size - 1]))
print("\tAverage GPA: " + str(new / size))

print("Your new GPA would be " + str(new / size) + ' comapred to your current'
      ' score of ' + str(sum / size))
print("That is a diffrence of " + str((new / size) - (sum / size)) + ' points')

print("Too bad i have to print this passive agressive message")
print("witch is odd beacuse oviously this is a udemy course for self leaners")
print("Here are your grades: ")
print(grades)
print("Go ask for a hot dog!")
