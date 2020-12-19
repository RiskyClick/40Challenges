import random


class Healthy():
    def __init__(self, row, col, title='0'):
        self.row = row
        self.col = col
        self.title = title


class Sick(Healthy):
    def __init__(self, row, col, IR, MR, title='I'):
        super().__init__(row, col, title)
        self.title = title
        self.IR = IR
        self.MR = MR

    def infect(self, visual):
        try:
            if random.randint(0, 100) < self.IR and visual[self.row - 1][self.col - 1].title == '0':
                visual[self.row - 1][self.col - 1] = Sick(self.row - 1, self.col - 1, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row - 1][self.col].title == '0':
                visual[self.row - 1][self.col] = Sick(self.row - 1, self.col, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row - 1][self.col + 1].title == '0':
                visual[self.row - 1][self.col + 1] = Sick(self.row - 1, self.col + 1, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row][self.col - 1].title == '0':
                visual[self.row][self.col - 1] = Sick(self.row, self.col - 1, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row][self.col + 1].title == '0':
                visual[self.row][self.col + 1] = Sick(self.row, self.col + 1, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row + 1][self.col - 1].title == '0':
                visual[self.row + 1][self.col - 1] = Sick(self.row + 1, self.col - 1, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row + 1][self.col].title == '0':
                visual[self.row + 1][self.col] = Sick(self.row + 1, self.col, self.IR, self.MR)
            if random.randint(0, 100) < self.IR and visual[self.row + 1][self.col + 1].title == '0':
                visual[self.row + 1][self.col + 1] = Sick(self.row + 1, self.col + 1, self.IR, self.MR)
            if random.randint(0, 100) < self.MR:
                visual[self.row][self.col] = Dead(self.row, self.col, self.IR)
        except IndexError:
            pass


class Dead(Sick):
    def __init__(self, row, col, IF, title='X'):
        super().__init__(row, col, IF, title)
        self.IR = 0
        self.title = title


class Simmulation():
    def __init__(self, size, visual=[]):
        self.size = size
        self.visual = visual

    def generateVisual(self, IR, MR):
        col = []
        r = 0
        annoying = 1
        for pos, val in enumerate(range(self.size)):
            if random.randint(0, 100) < IR:
                col.append(Sick(len(self.visual),
                                len(col),
                                IR, MR))
            else:
                col.append(Healthy(len(self.visual),
                                   len(col)))
            if annoying % 100 == 0:
                self.visual.append(col)
                col = []
                r += 1
            annoying += 1
        self.visual.append(col)

    def showVisual(self):
        for i in self.visual:
            for j in i:
                print(j.title, end='')
            print()

    def dayPass(self):
        for i in self.visual:
            for j in i:
                if j.title == 'I':
                    j.infect(self.visual)


print("Welcome to the epidemic spread map")
size = int(input("What would you like the population size to be: "))
IR = int(input("What presentage is the infection rate: "))
MR = int(input("What percentage is the mortality rate: "))
sim = Simmulation(size)
sim.generateVisual(IR, MR)
sim.showVisual()
day = 1
while True:
    print("AFTER " + str(day) + " DAYS")
    input("Press any key to cycle another day")
    sim.dayPass()
    sim.showVisual()
    day += 1
