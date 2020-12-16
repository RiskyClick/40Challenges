import random


class Healthy():
    def __init__(self, row, col, title='0'):
        self.row = row
        self.col = col
        self.title = title


class Sick(Healthy):
    def __init__(self, row, col, IR, title='I'):
        super().__init__(row, col, title)
        self.title = title
        self.IR = IR


class Dead(Sick):
    def __init__(self, row, col, IF, title='X'):
        super().__init__(row, col, IF, title)
        self.IR = 0
        self.title = title


class Simmulation():
    def __init__(self, size, visual=[]):
        self.size = size
        self.visual = visual

    def generateVisual(self, IR):
        rows = int(self.size / 10)
        odds = int(IR * self.size / 100)
        sick = 0
        for key, val in enumerate(range(rows)):
            row = []
            for k, v, in enumerate(range(100)):
                sick += 1
                if sick == odds:
                    sick = 0
                    row.append(Sick(key, k, IR))
                else:
                    row.append(Healthy(key, k))
            self.visual.append(row)

    def showVisual(self):
        for i in self.visual:
            for j in i:
                print(j.title, end='')
            print()


size = int(input("Whats the size: "))
sim = Simmulation(size)
ifc = int(input("Whats the infection rate: "))
sim.generateVisual(ifc)
sim.showVisual()
