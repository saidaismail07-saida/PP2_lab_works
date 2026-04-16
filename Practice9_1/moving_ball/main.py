import pygame
import sys
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()
ball = Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    ball.move(keys)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)