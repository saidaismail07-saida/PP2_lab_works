import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()

bg = pygame.image.load("car_road.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

font = pygame.font.SysFont("Arial", 36)


class Player:
    def __init__(self):
        self.image = pygame.image.load("mycar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 100
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Enemy:
    def __init__(self):
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.x = random.randint(0, WIDTH - 50)
        self.y = -100
        self.speed = 5

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -100
            self.x = random.randint(0, WIDTH - 50)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def collide(self, player):
        enemy_rect = pygame.Rect(self.x, self.y, 50, 80)
        player_rect = pygame.Rect(player.x, player.y, 50, 80)
        return enemy_rect.colliderect(player_rect)


class Coin:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = -20
        self.weight = random.choice([1, 2, 3]) 
        self.radius = 8 + self.weight * 3
        self.speed = 4

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), self.radius)

    def collide(self, player):
        return (player.x < self.x < player.x + 50 and
                player.y < self.y < player.y + 80)


player = Player()
enemy = Enemy()
coins = []

score = 0
game_over = False

SPAWN = pygame.USEREVENT
pygame.time.set_timer(SPAWN, 1500)


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SPAWN:
            coins.append(Coin())

    if not game_over:
        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.blit(bg, (0, 0))

        enemy.move()
        enemy.draw()

        if enemy.collide(player):
            game_over = True

        for coin in coins[:]:
            coin.move()
            coin.draw()

            if coin.collide(player):
                score += coin.weight
                coins.remove(coin)

                if score % 5 == 0:
                    enemy.speed += 1

            elif coin.y > HEIGHT:
                coins.remove(coin)

        player.draw()

        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

    else:
        screen.fill((0, 0, 0))

        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 20))

        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()