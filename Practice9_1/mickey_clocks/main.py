import pygame
import sys
from clock import Clock

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mickey.draw(screen)

    pygame.display.flip()
    clock.tick(1)