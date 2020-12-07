print("=====CALCULATOR=====")
data = []


def brain(first, second, opp):
    if opp == '+':
        print(str(first) + " + " + str(second) + " = " + str(first + second))
        data.append(str(first) + " + " + str(second) + " = "
                    + str(first + second))
    elif opp == '-':
        print(str(first) + " - " + str(second) + " = " + str(first - second))
        data.append(str(first) + " - " + str(second) + " = "
                    + str(first - second))
    elif opp == '*':
        print(str(first) + " * " + str(second) + " = " + str(first * second))
        data.append(str(first) + " * " + str(second) + " = " +
                    str(first * second))
    elif opp == '/':
        if second == 0:
            print("Cant div by 0")
            data.append("DIV ERROR")
        else:
            print(str(first) + " / " + str(second) + " = " + str(first/second))
            data.append(str(first) + " / " + str(second) + " = "
                        + str(first / second))
    elif opp == '^':
        print(str(first) + " ^ " + str(second) + " = "
              + str(pow(first, second)))
        data.append(str(first) + " ^ " + str(second) + ' = '
                    + str(pow(first, second)))
    else:
        print("Not a valid opperation")
        data.append("OPP ERROR")


while True:
    while True:
        try:
            first = int(input("First digit: "))
            second = int(input("Second digit: "))
            opp = input("Opperator: ")
            break
        except ValueError:
            print("Invalid")

    brain(first, second, opp)
    if input("\nTry another set of numbers: ") == 'n':
        print("\t----Summary----")
        for i in data:
            print("\t" + i)
        exit()
