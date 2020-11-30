print("Welcome to the shipping sccounts program\n")
name = input("Enter a name: ").title()
print("Hello " + name + ", here are the prices for shipping\n")

print("Oders from 1 to 100 are:\t$5.10 each")
print("Oders from 101 to 500 are:\t$5.00 each")
print("Oders from 501 to 1000 are:\t$4.95 each")
print("Oders over 1001 are:\t\t$4.80 each\n")

while True:
    try:
        for i in range(100):
            orders = int(input("How many orders do you want to ship: "))
            if orders < 1:
                print("Not valid")
            elif orders <= 100:
                price = 5.10
                break
            elif orders <= 500:
                price = 5.0
                break
            elif orders <= 1000:
                price = 4.95
                break
            else:
                price = 4.80
                break
        break
    except ValueError:
        print("Not a number")
print(str(orders) + " at " + str(format(price, '.2f')) + ' Total Cost: $'
      '' + str(format(price * orders, '.2f')))

choice = input("\nWould you like to place this order? (y/n): ")
if choice == 'y':
    print("Pay up SUCKKA!!")
else:
    print("Broke ass bitch")
