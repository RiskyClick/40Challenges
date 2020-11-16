print("Welcome to the grade sorter app\n")


grades = []
grades.append(str(input("What is your first grade: ")))
grades.append(str(input("What is your second grade: ")))
grades.append(str(input("What is your third grade: ")))
grades.append(str(input("What is your fourth grade: ")))

print("\nHere are your grades: " + str(grades))
grades.sort(reverse=True)
print("Here are your grades from hight to low: " + str(grades))

print("\nDropping your lowest 2 grades\n")
print(grades.pop())
print(grades.pop())

print("\nThe remaning grades are: " + str(grades))
print("Nice job on that " + grades[0])
