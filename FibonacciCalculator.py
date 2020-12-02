print("Welcome to the Fibonacci Calculator")
fibArr = [1]
pos = 0

while True:
    try:
        upTo = int(input('Enter the number you would'
                         'like to calculate Fib to: '))
        break
    except ValueError:
        print("Not a number. Try again!")

print("The first " + str(upTo) + " numbers of the fib sequence are:")
while len(fibArr) <= upTo:
    print(fibArr[pos])
    if len(fibArr) < 2:
        fibArr.append(1)
    else:
        addTo = fibArr[pos] + fibArr[pos - 1]
        fibArr.append(addTo)
    pos += 1
