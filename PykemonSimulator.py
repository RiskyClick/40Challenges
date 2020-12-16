import random
import time


class Pokemon():
    def __init__(self, name, level, speed, strength,
                 armor, health=100, heals=3):
        self.name = name
        self.level = level
        self.speed = speed
        self.strength = strength
        self.armor = armor
        self.health = health
        self.heals = heals

    def reUp(self):
        self.health = 100
        self.heals = 3

    def display(self):
        print("==========Your Current Pokemon Stats=========")
        print("\tName: " + self.name)
        print("\tLevel: " + str(self.level))
        print("\tSpeed: " + str(self.speed))
        print("\tStrength: " + str(self.strength))
        print("\tArmor: " + str(self.armor))
        print()

    def heal(self):
        self.heals -= 1
        he = random.randint(5, 10)
        print("Healing " + str(he))
        if self.health > 100:
            print("health adjustment")
            self.health = 100
        self.health += he

    def attack(self, challenger):
        spread = 100 - challenger.speed
        if spread < 1:
            spread = 2
        dodge = random.randint(1, spread) % random.randint(1, spread)
        damage = random.randint(0, 10)
        damage += self.strength
        damage -= challenger.armor
        if damage < 1:
            damage = 1
        if random.randint(1, 5) == 5:
            print("Lucky hit multiplyer!!!!")
            damage *= 2
        if dodge == '0':
            print(challenger.name + " DODGES HIT!")
            print("No damage taken!")
        else:
            if damage > 30:
                damage = 30
            print(self.name + " Deals " + str(damage))
            challenger.health -= damage


class Player():
    def __init__(self, pokemon, pokeball=[]):
        self.pokemon = pokemon
        self.pokeball = pokeball

    def addPoke(self, poke):
        self.pokeball.append(poke)

    def showPokeball(self):
        for i in self.pokeball:
            i.display()


class GamePlay():
    def __init__(self, tranning=5, location=0):
        self.tranning = tranning
        self.location = location

    def battle(self, poke1, poke2):
        print("\n=========!!BATTLE!!===========")
        self.tranning += 1
        while True:
            if poke1.health < 1:
                return False
            choice = input("Do you attack, run, or heal? ")
            if choice == 'attack':
                print("\n=====You choose attack!=====")
                poke1.attack(poke2)
            elif choice == 'heal':
                if poke1.heals > 0:
                    print("\n=====You choose heal=====")
                    poke1.heal()
                    print("You have " + str(poke1.heals) + " heals left!")
                else:
                    print("You dont have any heals left.")
                    print("You attack out of despreation")
                    poke1.attack(poke2)
            elif choice == 'run':
                print("\n==========You Run Away==========")
                poke1.level -= 1
                poke1.reUp()
                return False
            if poke2.health < 1:
                print("\n==========You Defeated " + poke2.name + "==========")
                print(poke2.name + " Has Been Added To you Pokeball")
                poke1.reUp()
                poke2.reUp()
                return True
            if poke2.health < 20 and poke2.heals > 0:
                print("=====Challenger heals=====")
                time.sleep(1)
                poke2.heal()
            else:
                print("=====challenger atacks=====")
                time.sleep(1)
                poke2.attack(poke1)
            print(poke1.name + " health is at: " + str(poke1.health))
            print(poke2.name + " health is at: " + str(poke2.health))

    def train(self, poke):
        print("\n====================Tranning====================")
        if self.tranning < 1:
            print("No tranning for you. Go battle some")
            return
        else:
            self.tranning -= 1
            op = random.randint(1, 3)
            poke.level += 1
            if op == 1:
                print("You got more speed")
                poke.speed += random.randint(0, 5)
            elif op == 2:
                print("You got more strength")
                poke.strength += random.randint(0, 5)
            else:
                print("You got more armor")
                poke.armor += random.randint(0, 5)
        poke.display()

    def travel(self):
        print("\n==========Traveling==========")
        generate = random.randint(1, 3)
        if generate == 3:
            print("A WILD POKEMON APPERS!!!")
            return True
        print("Noting noteworthy")
        self.location += 1
        self.tranning += 1
        return False

    def generate(self, you):
        stats = [random.randint(you.level - 5, you.level + 5),
                 random.randint(you.speed - 5, you.speed + 5),
                 random.randint(you.strength - 5, you.strength + 5),
                 random.randint(you.armor - 5, you.armor + 5)]
        for key, value in enumerate(stats):
            if value < 1:
                stats[key] = 1
            if value > 100:
                stats[key] = 100

        challenger = Pokemon('Testing', stats[0], stats[1], stats[2], stats[3])
        challenger.display()
        return challenger


print("==========Welcome to Pokemon==========")
newGame = GamePlay()
yourname = input("Enter your pokemon trainer name: ").title()
yourPoke = Pokemon('Picachu', 1, random.randint(1, 5),
                   random.randint(1, 5), random.randint(1, 5))
you = Player(yourPoke)
you.addPoke(yourPoke)

print("\nHello " + yourname + " your first pokemon is")
yourPoke.display()
while True:
    print("You are at " + str(newGame.location))
    choice = input("Do you want to travel or train? ")
    if choice == 'travel':
        if newGame.travel():
            challenger = newGame.generate(yourPoke)
            if newGame.battle(yourPoke, challenger):
                you.addPoke(challenger)
            else:
                print(yourPoke.name + " has died in a hail of gunfire")
                you.pokeball.pop()
                if len(you.pokeball) < 1:
                    print("==========GameOver==========")
                    exit()
                else:
                    yourPoke = you.pokeball[len(you.pokeball) - 1]
                    yourPoke.reUp()
    else:
        yourPoke.display()
        newGame.train(yourPoke)
