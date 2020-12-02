print("Welcome to the DATABASE!!!!!\n")
database = {
    "user1": "123",
    "user2": '456',
    'user3': '789',
    'user4': '101112',
    'admin': '00'
}
atmp = 0
name = input("Whats your username: ")
if name not in database.keys():
    print(name + " not in user database. Goodbye!")
    exit(0)
else:
    while True:
        password = input("Whats your password: ")
        if database[name] == password:
            print('\nHello ' + name + " you are logged in.")
            if name == 'admin':
                for k, v in database.items():
                    print("USER: " + k + "\tPASS: " + v)
                exit(0)
            break
        else:
            print("inccorect password\n")
            atmp += 1
            if atmp > 2:
                print("You are now locked out permenetly!")
                exit(0)
if input("Would you like to change your password y/n: ") == 'y':
    newPass = input("Enter your new password: ")
    if len(newPass) < 4:
        print("Password not long enough")
    else:
        database[name] = newPass
print("\n" + name + " your password is " + database[name])
