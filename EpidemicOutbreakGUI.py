# Import and initialize the pygame library
import pygame
import math
import random
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1800, 800])


class Human():
    def __init__(self, x, y, IR, MR, status='H', color=(0, 128, 0), size=5, sickTimer=0):
        self.x = x
        self.y = y
        self.IR = IR
        self.MR = MR
        self.size = size
        self.color = color
        self.status = status
        self.sickTimer = 0

    def changeStatus(self, MR=0):
        if self.status == 'H':
            self.status = 'S'
            self.color = (255, 255, 0)
        if self.status == 'S':
            self.sickTimer += 1
            if self.sickTimer > 1000 and random.randint(0, 100) < MR:
                self.status = 'D'
                self.color = (255, 0, 0)

    def move(self):
        self.x += random.randint(-2, 2)
        self.y += random.randint(-2, 2)

    def collide(self, antiMaskers, key):
        for k, v in enumerate(antiMaskers):
            if abs(self.x - v.x) < self.size / 2 and abs(self.y - v.y) < self.size / 2 and key != k:
                if random.randint(0, 100) < self.IR:
                    v.changeStatus()


II = 20#int(input("Whats the initial infection rate: "))
IR = 40#int(input("What % chance of speading the infection: "))
MR = 20#int(input("Whats the mortality rate ater infected: "))
population = 5000#int(input("What is the sample size: "))
antiMaskers = []
pop = 1
while pop < population:
    if random.randint(0, 100) < II:
        antiMaskers.append(Human(random.randint(1, 1800), random.randint(1, 800), IR, MR, 'I', (255, 255, 0)))
    else:
        antiMaskers.append(Human(random.randint(1, 1800), random.randint(1, 800), IR, MR))
    pop += 1

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    for k, v in enumerate(antiMaskers):
        pygame.draw.circle(screen, v.color, (v.x, v.y), v.size)
        if v.status == 'I':
            v.collide(antiMaskers, k)
        elif v.status == 'S':
            v.changeStatus(MR)
        if v.status != 'D':
            v.move()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
