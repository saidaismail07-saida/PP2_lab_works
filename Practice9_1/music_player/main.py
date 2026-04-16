import pygame
from player import Player

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Saida", 18)

player = Player()

running = True
clock = pygame.time.Clock()

def draw():
    screen.fill((30, 30, 30))

    title = font.render("🎵 Music Player", True, (255, 255, 255))
    track = font.render("Current: " + player.get_current_track(), True, (0, 200, 255))

    controls = [
        "P = Play",
        "S = Stop",
        "N = Next",
        "B = Previous",
        "Q = Quit"
    ]

    screen.blit(title, (20, 20))
    screen.blit(track, (20, 80))

    for i, text in enumerate(controls):
        img = font.render(text, True, (200, 200, 200))
        screen.blit(img, (20, 140 + i * 30))

    pygame.display.update()


while running:
    clock.tick(30)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

            elif event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.prev_track()

pygame.quit()