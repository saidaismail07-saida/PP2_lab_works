import pygame

def text(s, x, y, screen, font):
    img = font.render(s, True, (255,255,255))
    screen.blit(img, (x,y))


def menu(screen, font):
    screen.fill((0,0,0))
    text("TSIS 3 RACER", 120, 100, screen, font)
    text("1 - Play", 120, 200, screen, font)
    text("2 - Leaderboard", 120, 250, screen, font)
    text("3 - Quit", 120, 300, screen, font)


def game_over(screen, font, score):
    screen.fill((0,0,0))
    text("GAME OVER", 120, 100, screen, font)
    text(f"Score: {score}", 120, 200, screen, font)
    text("R - Restart", 120, 300, screen, font)


def leaderboard(screen, font, data):
    screen.fill((0,0,0))
    text("LEADERBOARD", 120, 50, screen, font)

    y = 120
    for i, d in enumerate(data):
        text(f"{i+1}. {d['name']} - {d['score']}", 100, y, screen, font)
        y += 30