# Import and initialize the pygame library
import pygame
import random

pygame.init()
font = pygame.font.SysFont("comicsans", 30, True)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1800, 800])


class Human():
    def __init__(self, x, y, IR, MR, status='H',
                 color=(0, 128, 0), size=5, sickTimer=0):
        self.x = x
        self.y = y
        self.IR = IR
        self.MR = MR
        self.size = size
        self.color = color
        self.status = status
        self.sickTimer = 0
        self.dx = random.uniform(-2.0, 2.0)
        self.dy = random.uniform(-2.0, 2.0)

    def changeStatus(self, MR=0):
        if self.status == 'H':
            self.status = 'S'
            self.color = (255, 255, 0)
        if self.status == 'S':
            self.sickTimer += 1
            if self.sickTimer > 1000 and random.randint(0, 100) < MR:
                self.status = 'D'
                self.color = (255, 0, 0)
            elif self.sickTimer > 1000:
                self.status = 'C'
                self.color = (0, 0, 255)

    def move(self):
        if self.x > 1800:
            self.x = 1799
            self.dx *= -1
        elif self.x < 0:
            self.x = 1
            self.dx *= -1
        elif self.y > 800:
            self.y = 799
            self.dy *= -1
        elif self.y < 0:
            self.y = 1
            self.dy *= -1
        else:
            self.x += self.dx
            self.y += self.dy

    def collide(self, antiMaskers, key):
        for k, v in enumerate(antiMaskers):
            if abs(self.x - v.x) < self.size / 2 and abs(self.y - v.y) <\
                    self.size / 2 and key != k:
                if random.randint(0, 100) < self.IR:
                    v.changeStatus()


h, i, c, d = 0, 0, 0, 0
health = font.render("Healthy:\t" + str(h), 1, (255, 255, 255))
infected = font.render("Infected:\t" + str(i), 1, (255, 255, 255))
dead = font.render("Dead:\t" + str(d), 1, (255, 255, 255))
cured = font.render("Cured:\t" + str(c), 1, (255, 255, 255))
preGame = True


II = 2
IR = 40
MR = 50
population = 2000
antiMaskers = []
pop = 1
while pop < population:
    if random.randint(0, 100) < II:
        antiMaskers.append(Human(random.randint(1, 1800),
                           random.randint(1, 800), IR, MR, 'I', (255, 255, 0)))
    else:
        antiMaskers.append(Human(random.randint(1, 1800),
                                 random.randint(1, 800), IR, MR))
    pop += 1
screen.fill((0, 0, 0))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(health, (2, 5))
    screen.blit(infected, (2, 30))
    screen.blit(cured, (2, 55))
    screen.blit(dead, (2, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    h, i, c, d = 0, 0, 0, 0
    for k, v in enumerate(antiMaskers):
        pygame.draw.circle(screen, v.color, (v.x, v.y), v.size)
        if v.status == 'I':
            i += 1
            v.collide(antiMaskers, k)
        elif v.status == 'S':
            i += 1
            v.changeStatus(MR)
        if v.status != 'D':
            v.move()
        if v.status == 'D':
            d += 1
        if v.status == 'C':
            c += 1
        if v.status == 'H':
            h += 1
    health = font.render("Healthy:  " + str(h), 1, (255, 255, 255))
    infected = font.render("Infected: " + str(i), 1, (255, 255, 255))
    dead = font.render("Dead:      " + str(d), 1, (255, 255, 255))
    cured = font.render("Cured:    " + str(c), 1, (255, 255, 255))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
