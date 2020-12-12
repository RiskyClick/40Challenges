import matplotlib.pyplot as pyplot


def printLoan(loan, months):
    print("\n----------Loan Summary After " + str(months) + "----------")
    for key, value in loan.items():
        print(key.title() + ": \t" + str(value))


def getLoan():
    loan = {}
    while True:
        try:
            loan['principal'] = float(input("Enter Principal: "))
            loan['intrest'] = float(input("Enter Intrest: ")) / 100
            loan['monthly'] = float(input("Enter Monthly Payment: "))
            loan['paid amount'] = 0
            return loan
        except ValueError:
            print("Not a valid number")


def intrest(loan):
    loan['principal'] = loan['principal']+loan['principal']*loan['intrest']/12


def payment(loan):
    loan['principal'] -= loan['monthly']
    if loan['principal'] > 0:
        loan['paid amount'] += loan['monthly']
    else:
        loan['paid amount'] += loan['monthly'] + loan['principal']
        loan['principal'] = 0


def summary(laon, months, initPrince):
    print("\n----------Paid Off----------")
    print("Initial loan was: $" + str(initPrince) + " at a rate of " +
          str(loan['intrest'] * 100))
    print("Monthy payment was: $" + loan['monthly'])
    print("You spent: $" + str(round(loan['paid amount'], 2)) + ' In total')
    intrest = round(loan['paid amount'] - initPrince, 2)
    print("You spent: $" + str(intrest) + " on intrest")


def makeGraph(data, loan):
    xcor = []
    ycor = []
    for point in data:
        xcor.append(point[0])
        ycor.append(point[1])
    pyplot.plot(xcor, ycor)
    pyplot.title(str(100 * loan['intrest']) + "% Intrest With $"
                 + str(loan['monthly']) + " Monthy Payments")
    pyplot.xlable("Month")
    pyplot.ylable("Principal")
    pyplot.show()


loan = getLoan()
monthNumber = 0
startingPrincipal = loan['principal']
data = []

printLoan(loan, monthNumber)
input("Press enter to pay off loan")
while loan['principal'] > 0:
    if loan['principal'] > startingPrincipal:
        break
    monthNumber += 1
    intrest(loan)
    payment(loan)
    data.append((monthNumber, loan['principal']))
    printLoan(loan, monthNumber)

if loan['principal'] <= 0:
    summary(loan, monthNumber, startingPrincipal)
    makeGraph(data, loan)
else:
    print("Not gonna happen")
    print("You must increase your monthly payment")
