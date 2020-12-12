import random
import time


class Card():
    def __init__(self, suit, number, face=''):
        self.suit = suit
        self.number = number
        self.face = face

    def showCard(self):
        if len(self.face) > 2:
            print(str(self.face) + " of " + self.suit)
        else:
            print(str(self.number) + " of " + self.suit)

    def flipAce(self):
        if self.face == 'Ace':
            if self.number == 1:
                self.number == 11
            else:
                self.number = 1
        else:
            return


class Player():
    def __init__(self, name='Dealer', money=50000, score=0):
        self.name = name
        self.money = money
        self.score = 0

    def hit(self, number):
        self.score += number

    def bust(self):
        if self.score > 21:
            return True
        else:
            return False

    def bet(self, amount):
        self.money += amount

    def broke(self):
        if self.money > 0:
            return False
        else:
            print("\nBREAK HIS LEGGGGGSSSS!!!!")
            return True


def makeDeck():
    deck = []
    suits = 1
    faces = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
    while suits <= 4:
        if suits == 1:
            for i in range(1, 14):
                if i in faces:
                    deck.append(Card('Spade', 10, faces[i]))
                else:
                    deck.append(Card('Spade', i))
        elif suits == 2:
            for i in range(1, 14):
                if i in faces:
                    deck.append(Card('Harts', 10, faces[i]))
                else:
                    deck.append(Card('Harts', i))
        elif suits == 3:
            for i in range(1, 14):
                if i in faces:
                    deck.append(Card('Diamond', 10, faces[i]))
                else:
                    deck.append(Card('Diamond', i))
        else:
            for i in range(1, 14):
                if i in faces:
                    deck.append(Card('Club', 10, faces[i]))
                else:
                    deck.append(Card('Club', i))
        suits += 1
    return deck * 4


def pullCard(deck, pile, person, userDeck):
    pile.append(deck.pop(random.randint(0, len(deck))))
    pile[len(pile) - 1].showCard()
    userDeck.append(pile[len(pile) - 1])
    person.hit(pile[len(pile) - 1].number)
    return pile[len(pile) - 1]


def ace(person, deck):
    for i in deck:
        i.flipAce()


while True:
    print("\n=====Welcome to Casino Blackjack!=====\n")
    name = input("Whats your name? ").title()
    while True:
        try:
            money = int(input("How much money you got: "))
            if money < 1:
                print("Not enough money sukkka")
            else:
                break
        except ValueError:
            print("THAT AINT MONEY")
    dealer = Player()
    player = Player(name, money)
    theDeck = makeDeck()
    for i in theDeck:
        i.flipAce()
        print(i.number)
        i.showCard()
    usedDeck = []
    print("\nWecome " + name)
    while player.broke() is False:
        dealerDeck = []
        playerDeck = []
        player.score = 0
        dealer.score = 0
        print("\nDealer shows")
        pullCard(theDeck, usedDeck, dealer, dealerDeck)
        bet = int(input("Your bet: "))
        print("\nYour cards are")
        time.sleep(1)
        pullCard(theDeck, usedDeck, player, playerDeck)
        time.sleep(1)
        pullCard(theDeck, usedDeck, player, playerDeck)
        while player.bust() is False:
            ace(player, playerDeck)
            print("Your total is " + str(player.score))
            if input("\nDo you want to hit? ") == 'hit':
                pullCard(theDeck, usedDeck, player, playerDeck)
                ace(player, playerDeck)
                time.sleep(1)
                if player.bust():
                    print("Your total is " + str(player.score))
                    print("YOU BUSTED!!")
                    player.bet(bet * -1)
            else:
                print("Dealers Draws")
                while dealer.score < player.score:
                    pullCard(theDeck, usedDeck, dealer, dealerDeck)
                    ace(dealer, playerDeck)
                    time.sleep(1)
                    if dealer.bust():
                        break
                if dealer.bust():
                    print("\nThe dealer Busted")
                    print("You win!")
                    player.bet(bet)
                    break
                else:
                    print("\nDealer Wins!!!!")
                    print("You lose!")
                    player.bet(bet * -1)
                    break
        print("Your money is: " + str(player.money))
