import random

SIZE = 20


class Snake:
    def __init__(self):
        self.body = [(10,10),(9,10),(8,10)]
        self.dir = (1,0)

        self.food = self.spawn()
        self.poison = self.spawn()

        self.score = 0
        self.level = 1
        self.alive = True

        self.obstacles = []

    def spawn(self):
        return (random.randint(0,19), random.randint(0,19))

    def move(self):
        head = self.body[0]
        new = (head[0]+self.dir[0], head[1]+self.dir[1])

        if new[0]<0 or new[0]>=20 or new[1]<0 or new[1]>=20:
            self.alive = False
            return

        if new in self.body[1:] or new in self.obstacles:
            self.alive = False
            return

        self.body.insert(0,new)

        if new == self.food:
            self.score += 1
            self.food = self.spawn()
        else:
            self.body.pop()

        if new == self.poison:
            self.poison = self.spawn()
            for _ in range(2):
                if len(self.body)>1:
                    self.body.pop()

        if len(self.body)<=1:
            self.alive=False

        if self.score % 5 == 0:
            self.level += 1
            if self.level >= 3:
                self.obstacles.append(self.spawn())