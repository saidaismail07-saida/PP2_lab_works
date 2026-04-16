import pygame
import datetime
import math

class Clock:
    def __init__(self):
        self.bg = pygame.image.load("mickey_clocks.png").convert()
        self.bg = pygame.transform.scale(self.bg, (600, 600))

        self.center = (300, 300)

    def draw(self, screen):
        # фон
        screen.blit(self.bg, (0, 0))

        now = datetime.datetime.now()
        sec = now.second
        minute = now.minute

        # углы
        sec_angle = math.radians(sec * 6 - 90)
        min_angle = math.radians(minute * 6 - 90)

        # секунды (длинная стрелка)
        sec_x = self.center[0] + 200 * math.cos(sec_angle)
        sec_y = self.center[1] + 200 * math.sin(sec_angle)

        # минуты (короче)
        min_x = self.center[0] + 150 * math.cos(min_angle)
        min_y = self.center[1] + 150 * math.sin(min_angle)

        # рисуем стрелки
        pygame.draw.line(screen, (255, 0, 0), self.center, (sec_x, sec_y), 3)
        pygame.draw.line(screen, (0, 0, 0), self.center, (min_x, min_y), 6)