import pygame
from racer import Racer
from ui import menu, game_over, leaderboard
from persistence import *

pygame.init()

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 3 Racer")

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

# ---------------- IMAGES ----------------
car_img = pygame.image.load("assets/car.png")
road_img = pygame.image.load("assets/car_road.png")

car_img = pygame.transform.scale(car_img, (40, 60))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# ---------------- GAME STATE ----------------
player = Racer()
state = "menu"
name = "Player"

running = True

# ---------------- MAIN LOOP ----------------
while running:
    clock.tick(60)

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # -------- MENU --------
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player = Racer()
                    state = "game"

                elif event.key == pygame.K_2:
                    state = "leaderboard"

                elif event.key == pygame.K_3:
                    running = False

        # -------- GAME OVER --------
        elif state == "gameover":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Racer()
                    state = "game"

                elif event.key == pygame.K_h:
                    player = Racer()
                    state = "menu"

        # -------- LEADERBOARD --------
        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

    keys = pygame.key.get_pressed()

    # ---------------- MENU ----------------
    if state == "menu":
        menu(screen, font)

    # ---------------- GAME ----------------
    elif state == "game":

        # background
        screen.blit(road_img, (0, 0))

        if player.alive:
            player.move(keys)
            player.spawn()
            player.update()
            player.check()
            player.update_power()
            player.update_score()

            # player car (PNG)
            screen.blit(car_img, (player.x, player.y))

            # obstacles
            for o in player.obstacles:
                pygame.draw.rect(screen, (255, 255, 255), (o[0], o[1], 40, 40))

            # powerups
            for p in player.powerups:
                pygame.draw.rect(screen, (0, 255, 0), (p[0], p[1], 40, 40))

            # score
            txt = font.render(f"Score: {player.score}", True, (255, 255, 255))
            screen.blit(txt, (10, 10))

        else:
            save_leaderboard([{"name": name, "score": player.score}])
            state = "gameover"

    # ---------------- GAME OVER ----------------
    elif state == "gameover":
        game_over(screen, font, player.score)

    # ---------------- LEADERBOARD ----------------
    elif state == "leaderboard":
        leaderboard(screen, font, load_leaderboard())

    pygame.display.flip()

pygame.quit()