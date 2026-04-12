import pygame
from datetime import datetime

class MickeyClock:
    def __init__(self, screen, center, hand_image):
        self.screen = screen
        self.center = center
        self.hand_image = hand_image

    def draw_hand(self, angle):
        rotated = pygame.transform.rotate(self.hand_image, -angle)
        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def update(self):
        now = datetime.now()
        minute = now.minute
        second = now.second

        minute_angle = minute * 6
        second_angle = second * 6

        self.draw_hand(second_angle)
        self.draw_hand(minute_angle)