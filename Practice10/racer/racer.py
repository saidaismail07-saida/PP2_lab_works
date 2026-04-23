import pygame
import random
import sys

pygame.init()

# размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

clock = pygame.time.Clock()

# 🎨 загружаем фон
bg = pygame.image.load("car_road.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# шрифт для счётчика
font = pygame.font.SysFont("Arial", 24)


# 🚗 класс машины игрока
class Player:
    def __init__(self):
        # загружаем картинку машины
        self.image = pygame.image.load("mycar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 80))

        # начальная позиция
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 100
        self.speed = 5

    def move(self, keys):
        # движение влево
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        # движение вправо
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        # рисуем машину
        screen.blit(self.image, (self.x, self.y))


# 🪙 класс монеты
class Coin:
    def __init__(self):
        # случайная позиция по X
        self.x = random.randint(50, WIDTH - 50)
        self.y = -20
        self.radius = 10
        self.speed = 5

    def move(self):
        # движение вниз
        self.y += self.speed

    def draw(self):
        # рисуем монету
        pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), self.radius)

    def collide(self, player):
        # проверка столкновения с машиной
        if (player.x < self.x < player.x + 50 and
                player.y < self.y < player.y + 80):
            return True
        return False


player = Player()

coins = []          # список монет
coin_count = 0      # количество собранных монет

# ⏱️ событие для появления монет
SPAWN_COIN = pygame.USEREVENT
pygame.time.set_timer(SPAWN_COIN, 1500)  # каждые 1.5 секунды

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == SPAWN_COIN:
            coins.append(Coin())

    keys = pygame.key.get_pressed()
    player.move(keys)

    # фон
    screen.blit(bg, (0, 0))

    
    for coin in coins[:]:
        coin.move()
        coin.draw()

        
        if coin.collide(player):
            coins.remove(coin)
            coin_count += 1

        
        elif coin.y > HEIGHT:
            coins.remove(coin)

    
    player.draw()

    text = font.render(f"Coins: {coin_count}", True, (0, 0, 0))
    screen.blit(text, (WIDTH - 130, 10))

    pygame.display.flip()