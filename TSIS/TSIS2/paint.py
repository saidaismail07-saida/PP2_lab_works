import os
print("WORKING DIR:", os.getcwd())
import pygame
import datetime
from collections import deque

pygame.init()

WIDTH, HEIGHT = 900, 650
PANEL_HEIGHT = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = BLACK
tool = "pencil"
brush_size = 5

last_pos = None
start_pos = None

text = ""
text_pos = None
typing = False


# FLOOD FILL
def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()

    try:
        old_color = surface.get_at((x, y))
    except:
        return

    if old_color == new_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()

        if 0 <= cx < width and 0 <= cy < height:
            if surface.get_at((cx, cy)) == old_color:
                surface.set_at((cx, cy), new_color)

                queue.append((cx+1, cy))
                queue.append((cx-1, cy))
                queue.append((cx, cy+1))
                queue.append((cx, cy-1))


# TOOLBAR
def draw_toolbar():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, PANEL_HEIGHT))

    txt = "R-red G-green B-blue | 1-2px 2-5px 3-10px | 4-pencil 5-line 6-fill 7-text | Ctrl+S save"
    render = font.render(txt, True, BLACK)
    screen.blit(render, (10, 20))


def save_canvas():
    filename = datetime.datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
    pygame.image.save(screen, filename)
    print("SAVED:", filename)


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYBOARD
        if event.type == pygame.KEYDOWN:

            # COLORS
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_b:
                color = BLUE

            # BRUSH SIZE
            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            # TOOLS
            if event.key == pygame.K_4:
                tool = "pencil"
            if event.key == pygame.K_5:
                tool = "line"
            if event.key == pygame.K_6:
                tool = "fill"
            if event.key == pygame.K_7:
                tool = "text"

            # SAVE
            if event.key == pygame.K_s:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    save_canvas()

            # TEXT typing
            if typing:
                if event.key == pygame.K_RETURN:
                    img = font.render(text, True, color)
                    screen.blit(img, text_pos)
                    typing = False

                elif event.key == pygame.K_ESCAPE:
                    typing = False

                else:
                    text += event.unicode

        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            if y < PANEL_HEIGHT:
                continue

            if tool == "line":
                start_pos = event.pos

            elif tool == "fill":
                flood_fill(screen, x, y, color)

            elif tool == "text":
                text_pos = event.pos
                text = ""
                typing = True

        if event.type == pygame.MOUSEBUTTONUP:

            if tool == "line":
                end_pos = event.pos

                if end_pos[1] > PANEL_HEIGHT:
                    pygame.draw.line(screen, color, start_pos, end_pos, brush_size)

    # PENCIL
    if tool == "pencil" and pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

        if y > PANEL_HEIGHT:
            if last_pos is not None:
                pygame.draw.line(screen, color, last_pos, (x, y), brush_size)

            last_pos = (x, y)
    else:
        last_pos = None

    # DRAW
    draw_toolbar()

    pygame.display.flip()

pygame.quit()