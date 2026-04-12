import pygame
from clock import MickeyClock

pygame.init()

screen = pygame.display.set_mode((600, 600))
center = (300, 300)

hand = pygame.image.load("images/hand_right.png").convert_alpha()
hand = pygame.image.load("images/hand_left.png").convert_alpha()
hand = pygame.image.load("images/clock.png").convert_alpha()
hand = pygame.image.load("images/mickey.png").convert_alpha()


hand = pygame.transform.scale(hand, (20, 200))

clock_obj = MickeyClock(screen, center, hand)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    clock_obj.update()

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
