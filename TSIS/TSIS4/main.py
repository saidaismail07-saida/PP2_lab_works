import pygame
import json

from game import Snake
from db import *

pygame.init()
init_db()

# SCREEN
W, H = 400, 400
screen = pygame.display.set_mode((W,H))
font = pygame.font.SysFont("Arial",20)
clock = pygame.time.Clock()

# STATE
state = "menu"

username = ""
player_id = None
game = Snake()

settings = {
    "grid": True,
    "sound": True
}


# ---------------- BUTTON ----------------
def button(text,x,y,w,h,color):
    pygame.draw.rect(screen,color,(x,y,w,h))
    txt = font.render(text,True,(0,0,0))
    screen.blit(txt,(x+10,y+10))
    return pygame.Rect(x,y,w,h)


# ---------------- MENU ----------------
def draw_menu():
    screen.fill((0,0,0))
    return [
        button("PLAY",120,80,160,50,(0,255,0)),
        button("LEADERBOARD",120,150,160,50,(255,255,0)),
        button("SETTINGS",120,220,160,50,(0,150,255)),
        button("QUIT",120,290,160,50,(255,0,0))
    ]


# ---------------- GAME OVER ----------------
def draw_gameover(score, level, best):
    screen.fill((0,0,0))
    screen.blit(font.render("GAME OVER",True,(255,0,0)),(120,50))
    screen.blit(font.render(f"Score: {score}",True,(255,255,255)),(120,100))
    screen.blit(font.render(f"Level: {level}",True,(255,255,255)),(120,140))
    screen.blit(font.render(f"Best: {best}",True,(255,255,0)),(120,180))

    return [
        button("RETRY",120,240,160,50,(0,255,0)),
        button("MENU",120,310,160,50,(255,255,0))
    ]


# ---------------- LEADERBOARD ----------------
def draw_leaderboard():
    screen.fill((0,0,0))
    screen.blit(font.render("LEADERBOARD",True,(255,255,255)),(120,20))

    y=80
    for i,row in enumerate(get_top10()):
        txt = font.render(f"{i+1}. {row[0]} {row[1]} L{row[2]}",True,(255,255,255))
        screen.blit(txt,(40,y))
        y+=25

    return button("BACK",140,330,120,50,(255,0,0))


# ---------------- SETTINGS ----------------
def draw_settings():
    screen.fill((0,0,0))
    screen.blit(font.render("SETTINGS",True,(255,255,255)),(140,30))

    g = button(f"GRID: {settings['grid']}",120,120,160,50,(100,100,255))
    s = button(f"SOUND: {settings['sound']}",120,190,160,50,(100,255,100))
    save = button("SAVE & BACK",120,260,160,50,(255,255,0))

    return g,s,save


# ---------------- LOOP ----------------
running = True

while running:
    clock.tick(8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MENU INPUT
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_id = get_player(username)
                    game = Snake()
                    state = "game"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        # GAME INPUT
        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and game.dir != (1,0):
                    game.dir = (-1,0)
                if event.key == pygame.K_RIGHT and game.dir != (-1,0):
                    game.dir = (1,0)
                if event.key == pygame.K_UP and game.dir != (0,1):
                    game.dir = (0,-1)
                if event.key == pygame.K_DOWN and game.dir != (0,-1):
                    game.dir = (0,1)

        # GAMEOVER INPUT
        elif state == "gameover":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry.collidepoint(event.pos):
                    game = Snake()
                    state = "game"
                if menu_btn.collidepoint(event.pos):
                    state = "menu"

        # LEADERBOARD INPUT
        elif state == "leaderboard":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    state = "menu"

        # SETTINGS INPUT
        elif state == "settings":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if g.collidepoint(event.pos):
                    settings["grid"] = not settings["grid"]
                if s.collidepoint(event.pos):
                    settings["sound"] = not settings["sound"]
                if save.collidepoint(event.pos):
                    state = "menu"


    # ---------------- DRAW ----------------
    screen.fill((0,0,0))

    if state == "menu":
        buttons = draw_menu()
        play, lb, st, qt = buttons

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(event.pos):
                state = "game"
            if lb.collidepoint(event.pos):
                state = "leaderboard"
            if st.collidepoint(event.pos):
                state = "settings"
            if qt.collidepoint(event.pos):
                running = False

        screen.blit(font.render("Enter name: "+username,True,(255,255,255)),(20,350))

    elif state == "game":
        if game.alive:
            game.move()

            for b in game.body:
                pygame.draw.rect(screen,(0,255,0),(b[0]*20,b[1]*20,20,20))

            pygame.draw.rect(screen,(255,0,0),(game.food[0]*20,game.food[1]*20,20,20))
            pygame.draw.rect(screen,(100,0,0),(game.poison[0]*20,game.poison[1]*20,20,20))

        else:
            save_game(player_id, game.score, game.level)
            best = best_score(player_id)
            state = "gameover"

    elif state == "gameover":
        retry, menu_btn = draw_gameover(game.score, game.level, best_score(player_id))

    elif state == "leaderboard":
        back = draw_leaderboard()

    elif state == "settings":
        g,s,save = draw_settings()

    pygame.display.flip()

pygame.quit()