import time


print("Prime number thing")
primes = []


def primeHunter(start, number):
    maybe = 0
    while start < (number / 2 + 1):
        if number % start == 0:
            maybe += 1
        if maybe > 1:
            return False
            break
        start += 1
    if maybe < 2:
        return True


while True:
    print("\nEnter a 1 to see if a number is prime")
    print("Or enter a 2 to see all the prime numbers up to a given number")
    while True:
        try:
            choice = int(input())
            if choice > 3 or choice < 1:
                print("Invaild choice")
            else:
                if choice == 3:
                    exit()
                number = int(input("\nWhat number: "))
                if number < 1:
                    print("invalid choice")
                else:
                    break
        except ValueError:
            print("Invalid option")

    print()
    start = 1
    if choice == 1:
        print("PRIME!") if primeHunter(start, number) else print("NOT PRIME!")
    else:
        begin = time.time()
        for i in range(1, number + 1):
            if primeHunter(start, i):
                primes.append(i)
        finish = time.time()
        print("\nIt took " + str(finish - begin) + " To compleate")
        if input("Press Enter to view the list of prime numbers") == '':
            for i in primes:
                print(i)
        print()
