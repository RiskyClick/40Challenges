print("Welcome to the factor generator")
facs = []

while True:
    facs = []
    while True:
        try:
            factor = int(input("\nEnter the number you want factorized!: "))
            break
        except ValueError:
            print("Not a vaild number")
    posible = 0
    while posible < (factor / 2):
        posible += 1
        if factor % posible == 0:
            facs.append(posible)
    facs.append(factor)
    print("\nFactors of " + str(factor) + " are")
    for i in facs:
        print(i)
    print("\nIn summary")
    for i, j in enumerate(facs):
        print(str(j) + "\t * \t" + str(facs[len(facs) - i - 1]) + '\t = \t'
              + str(factor))

    if input("\nWant to do another number?: ") == 'n':
        exit(0)
