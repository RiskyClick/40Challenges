print("Even odd sortering app")


while True:
    even = []
    odd = []
    print("Enter a string of numbers seprated by ,")
    string = input().strip()
    temp = 0
    print("\n-----Result Summary-----")
    for i, v in enumerate(string):
        if v == ',':
            if temp == 0:
                integer = int(string[temp:i])
            else:
                integer = int(string[temp + 1:i])
            temp = i
            if integer % 2 == 0:
                print("\t" + str(integer) + " Is even")
                even.append(integer)
            else:
                print("\t" + str(integer) + " Is odd")
                odd.append(integer)
    print("\nThe Folling are  even:")
    even.sort()
    for i in even:
        print("\t" + str(i))
    print("\nThe Following are ood:")
    odd.sort()
    for i in odd:
        print("\t" + str(i))
    if input("What to do another set of numbers? (y/n)") == 'n':
        exit(0)
