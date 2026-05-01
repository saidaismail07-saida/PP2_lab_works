import pygame
import random

WIDTH = 400

class Racer:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = 500

        self.speed = 5
        self.base_speed = 5

        self.coins = 0
        self.distance = 0
        self.score = 0

        self.alive = True

        self.obstacles = []
        self.powerups = []

        self.active_power = None
        self.power_timer = 0

        self.lanes = [80, 170, 260]

    # ---------------- MOVEMENT ----------------
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.x = max(0, min(WIDTH - 40, self.x))
        self.distance += 1

    # ---------------- SPAWN ----------------
    def spawn(self):
        if random.randint(1, 40) == 1:
            self.obstacles.append([random.choice(self.lanes), -40])

        if random.randint(1, 120) == 1:
            self.powerups.append([random.choice(self.lanes), -40, random.choice(["nitro","shield","repair"])])

    # ---------------- UPDATE ----------------
    def update(self):
        for o in self.obstacles:
            o[1] += self.speed + 2

        for p in self.powerups:
            p[1] += 4

        self.obstacles = [o for o in self.obstacles if o[1] < 600]
        self.powerups = [p for p in self.powerups if p[1] < 600]

    # ---------------- COLLISION ----------------
    def check(self):
        car = pygame.Rect(self.x, self.y, 40, 60)

        # obstacles
        for o in self.obstacles:
            if car.colliderect(pygame.Rect(o[0], o[1], 40, 40)):
                if self.active_power == "shield":
                    self.active_power = None
                else:
                    self.alive = False

        # powerups
        for p in self.powerups:
            if car.colliderect(pygame.Rect(p[0], p[1], 40, 40)):
                self.active_power = p[2]
                self.power_timer = pygame.time.get_ticks()

    # ---------------- POWERUPS ----------------
    def update_power(self):
        if self.active_power == "nitro":
            self.speed = 10
        else:
            self.speed = self.base_speed

        if self.active_power and pygame.time.get_ticks() - self.power_timer > 4000:
            self.active_power = None

    # ---------------- SCORE ----------------
    def update_score(self):
        self.score = self.coins * 10 + self.distance // 10