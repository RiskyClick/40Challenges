print("Prime number thing")
primes = []

def primeHunter()

while True:
    start = 1
    print("Enter a 1 to see if a number is prime")
    print("Or enter a 2 to see all the prime numbers up to a given number")
    while True:
        try:
            choice = int(input())
            if choice > 3 or choice < 1:
                print("Invaild choice")
            else:
                number = int(input("\nWhat number: "))
                if number < 1:
                    print("invalid choice")
                else:
                    break
        except ValueError:
            print("Invalid option")

    print()
    if choice == 1:
        maybe = 0
        while start < (number / 2 + 1):
            if number % start == 0:
                maybe += 1
            if maybe > 1:
                print(str(number) + " NOT PRIME!\n")
                break
            start += 1
        if maybe < 2:
            print(str(number) + " PRIME!\n")
    elif choice == 2:
        maybe = 0
        check = 1
        while start <= number:
            while check < int(start / 2):
                maybe = 0
                if start % check == 0:
                    maybe += 1
                if maybe > 1:
                    continue
                check += 1
            if maybe < 1:
                primes.append(start)
            start += 1
        print(primes)
    else:
        exit()
