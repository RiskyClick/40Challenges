def operator(num, op):
    count = 1
    if op == 'm':
        while count < 10:
            print("\t" + str(count) + " * " + str(num) + " = " + str(count * num))
            count += 1
    else:
        while count < 10:
            print("\t" + str(count) + " ** " + str(num) + " = " + str(count ** num))
            count += 1


print("Welcome to Multiplication/Exponentiation Table Program\n")
name = input("Whats your name: ").title().strip()
while True:
    try:
        num = float(input("Hi " + name + ", what number would you like to table: "))
        break
    except ValueError:
        print("Not a valid number. Try Again")
print("Multiplication\n")
operator(num, 'm')
print("\nExponent\n")
operator(num, 'e')

message = name + " Math is Cool"
print(message.lower())
print("\t" + message.title())
print("\t\t" + message.upper())
print("\t\t\t" + message)
