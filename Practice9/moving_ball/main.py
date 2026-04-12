import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = Ball()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -20, WIDTH, HEIGHT)
            if event.key == pygame.K_DOWN:
                ball.move(0, 20, WIDTH, HEIGHT)
            if event.key == pygame.K_LEFT:
                ball.move(-20, 0, WIDTH, HEIGHT)
            if event.key == pygame.K_RIGHT:
                ball.move(20, 0, WIDTH, HEIGHT)

    screen.fill("white")
    ball.draw(screen)

    pygame.display.flip()

pygame.quit()