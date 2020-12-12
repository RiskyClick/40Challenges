import random


class Creature():

    def __init__(self, name, hunger, board, tired, dirty):
        self.name = name
        self.hunger = hunger
        self.board = board
        self.tired = tired
        self.dirty = dirty
        self.awake = True
        self.foodSupply = 5
        self.dead = False

    def forage(self):
        food = random.randint(0, 5)
        self.foodSupply += food
        print(self.name + " got " + str(food) + " units of food")
        self.hunger += 1
        self.tired += 1
        self.dirty += 1

    def eat(self):
        if self.foodSupply < 1:
            print("Not enough food. Go forage for more!")
            self.board += 1
            self.tired += 1
            self.dirty += 1
        else:
            self.foodSupply -= 1
            self.hunger -= random.randint(0, 3)
            self.board += 1
            self.tired += 1
            self.dirty += 1

    def wakeUp(self):
        woke = random.randint(0, 100) % 2
        self.hunger += 1
        self.dirty += 1
        if woke == 0:
            print(self.name + " got there lazy ass out of bed!")
            self.awake = True
            self.tired = 0
            self.board = 0
        else:
            print("Was up all night and sleeping all day")

    def sleep(self):
        self.awake = False
        self.hunger += 1
        self.board += 1
        self.tired = 0
        self.dirty += 1

    def play(self):
        self.hunger += 1
        self.board -= 1
        self.tired += 1
        self.dirty += 1

    def wash(self):
        self.hunger += 1
        self.board += 1
        self.tired += 1
        self.dirty = 0

    def stats(self):
        print("\n\t========Summary========")
        print("\tName:\t\t" + self.name)
        print("\tHunger:\t\t" + str(self.hunger))
        print("\tBordom:\t\t" + str(self.board))
        print("\tTiredness:\t" + str(self.tired))
        print("\tDirty:\t\t" + str(self.dirty))
        print("\tFood Supply:\t" + str(self.foodSupply))
        print("\tAwake\n") if self.awake else print("\tSleeping\n")

    def died(self):
        if self.hunger > 9:
            print("You have to eat!")
            if self.hunger > 10:
                print(self.name + " has starved to death. Game over")
                self.dead = True
        elif self.board > 10:
            print(self.name + " is so board they fell asleep.")
            self.awake = False
        elif self.tired > 10:
            print(self.name + " is so tired they fell asleep")
            self.awake = False
        elif self.dirty > 10:
            print(self.name + " is gross take a shower!")
            if self.dirty > 15:
                print(self.name + " has developed a infection"
                      "and died. GameOver")
                self.dead = True


def makeChoice(pet):
    if pet.awake:
        print("\n\tTo forage presss 1")
        print("\tTo eat presss 2")
        print("\tTo play presss 3")
        print("\tTo bathe presss 4")
        print("\tTo sleep press 5\n")
        while True:
            try:
                chocie = int(input("Pick and number from the list: "))
                if chocie == 1:
                    pet.forage()
                    return
                elif chocie == 2:
                    pet.eat()
                    return
                elif chocie == 3:
                    pet.play()
                    return
                elif chocie == 4:
                    pet.wash()
                    return
                elif chocie == 5:
                    pet.sleep()
                    return
                else:
                    print("Not a Valid choice")
            except ValueError:
                print("Invalid Choice")
    else:
        print(pet.name + " is asleep.")
        input("Press any key to wake up " + pet.name)
        pet.wakeUp()


print("\nHere is one of those kill your pet games\n")
while True:
    if input("Press Enter to make a new pet ") == 'n':
        exit()
    name = input("Whats the name of your pet? ").title()
    RIP = Creature(name, 0, 0, 0, 0)
    round = 1
    while not RIP.dead:
        RIP.stats()
        makeChoice(RIP)
        RIP.died()
        round += 1
    print("\t==========End Game Summary==========")
    print(RIP.name + " Survived " + str(round) + " Rounds")
    RIP.stats()
