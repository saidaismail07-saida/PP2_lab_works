import pygame
import sys
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

center = (300, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute

    sec_angle = sec * 6
    min_angle = minute * 6

    screen.fill((255, 255, 255))

    # секундная стрелка (красная)
    x1 = center[0] + 200 * math.cos(math.radians(sec_angle - 90))
    y1 = center[1] + 200 * math.sin(math.radians(sec_angle - 90))
    pygame.draw.line(screen, (255, 0, 0), center, (x1, y1), 3)

    # минутная стрелка (чёрная)
    x2 = center[0] + 150 * math.cos(math.radians(min_angle - 90))
    y2 = center[1] + 150 * math.sin(math.radians(min_angle - 90))
    pygame.draw.line(screen, (0, 0, 0), center, (x2, y2), 5)

    pygame.display.flip()
    clock.tick(60)