import random


class Card():
    def __init__(self, suit, number, ace=False):
        self.suit = suit
        self.number = number
        self.ace = ace

    def showCard(self):
        print(str(self.number) + " of " + self.suit)

    def isAce(self):
        return self.ace


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
            return True


def makeDeck():
    deck = []
    suits = 1
    while suits <= 4:
        if suits == 1:
            for i in range(1, 14):
                if i == 1:
                    deck.append(Card('Spade', i, True))
                else:
                    deck.append(Card('Spade', i))
        elif suits == 2:
            for i in range(1, 14):
                if i == 1:
                    deck.append(Card('Harts', i, True))
                else:
                    deck.append(Card('Harts', i))
        elif suits == 3:
            for i in range(1, 14):
                if i == 1:
                    deck.append(Card('Diamond', i, True))
                else:
                    deck.append(Card('Diamond', i))
        else:
            for i in range(1, 14):
                if i == 1:
                    deck.append(Card('Club', i, True))
                else:
                    deck.append(Card('Club', i))
        suits += 1
    return deck * 4


def pullCard(deck, pile):
    pile.append(deck.pop(random.randint(0, len(deck))))
    return pile[len(pile) - 1]


while True:
    print("Welcome to Casino Blackjack!")
    name = input("Whats your name? ").title()
    money = int(input("How much money ya got? "))
    dealer = Player()
    player = Player(name, money)
    theDeck = makeDeck()
    usedDeck = []
    print("Wecome " + name)
    while player.broke() is False:
        card = pullCard(theDeck, usedDeck)
        print("Dealer shows")
        card.showCard()
        bet = input("Your bet: ")
        while player.bust() is False or dealer.bust() is False:
            print("You pull a")
            card = pullCard(theDeck, usedDeck)
            card.showCard()
            player.hit(card.number)
            print("and a")
            card = pullCard(theDeck, usedDeck)
            card.showCard()
            player.hit(card.number)
            while True:
                print("Your total is: " + str(player.score))
                if input("Do you want to hit? ") == 'hit':
                    card = pullCard(theDeck, usedDeck)
                    card.showCard()
                    player.hit(card.number)
                else:
                    break
