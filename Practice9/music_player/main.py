import pygame
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((600, 200))
font = pygame.font.SysFont("Arial", 24)

playlist = [
    "music/track1.mp3",
    "music/track2.mp3"
]

player = MusicPlayer(playlist)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            if event.key == pygame.K_s:
                player.stop()
            if event.key == pygame.K_n:
                player.next()
            if event.key == pygame.K_b:
                player.prev()

    screen.fill("black")
    text = font.render("P-play S-stop N-next B-back", True, "white")
    screen.blit(text, (50, 80))

    pygame.display.flip()

pygame.quit()