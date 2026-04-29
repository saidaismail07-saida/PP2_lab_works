import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 24)


class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (CELL_SIZE, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, GREEN, (*block, CELL_SIZE, CELL_SIZE))

    def check_self_collision(self):
        return self.body[0] in self.body[1:]


class Food:
    def __init__(self, snake):
        self.position = self.random_position(snake)
        self.weight = random.choice([1, 2, 3])  # разный вес
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 5000  # 5 секунд

    def random_position(self, snake):
        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE)//CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE)//CELL_SIZE) * CELL_SIZE
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self):
        if self.weight == 1:
            color = (255, 0, 0)
        elif self.weight == 2:
            color = (255, 165, 0)
        else:
            color = (255, 255, 0)

        pygame.draw.rect(screen, color, (*self.position, CELL_SIZE, CELL_SIZE))

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.lifetime


snake = Snake()
food = Food(snake)

score = 0
level = 1
speed = 10

running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                snake.direction = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                snake.direction = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                snake.direction = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                snake.direction = (CELL_SIZE, 0)

    snake.move()

    head_x, head_y = snake.body[0]

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    if snake.check_self_collision():
        print("GAME OVER")
        pygame.quit()
        sys.exit()

     
    if food.is_expired():
        food = Food(snake)

    if snake.body[0] == food.position:
        snake.grow()
        score += food.weight
        food = Food(snake)

        if score % 3 == 0:
            level += 1
            speed += 2

    screen.fill(BLACK)

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.flip()