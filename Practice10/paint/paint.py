import pygame
import math

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

mode = "white"
tool = "brush"

shapes = []
brush_lines = []

start_pos = None
last_pos = None

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                mode = "red"
            if event.key == pygame.K_g:
                mode = "green"
            if event.key == pygame.K_b:
                mode = "blue"

            if event.key == pygame.K_1:
                tool = "brush"
            if event.key == pygame.K_2:
                tool = "rect"
            if event.key == pygame.K_3:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            color = {
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "blue": (0, 0, 255),
                "white": (255, 255, 255)
            }[mode]

            if tool == "rect":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                shapes.append(("rect", color, (x, y, w, h)))

            elif tool == "circle":
                r = int(math.dist(start_pos, end_pos))
                shapes.append(("circle", color, start_pos, r))

    
    if pygame.mouse.get_pressed()[0] and tool in ["brush", "eraser"]:
        pos = pygame.mouse.get_pos()

        if tool == "eraser":
            color = (0, 0, 0)
        else:
            color = {
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "blue": (0, 0, 255),
                "white": (255, 255, 255)
            }[mode]

        if last_pos is not None:
            brush_lines.append((color, last_pos, pos))

        last_pos = pos
    else:
        last_pos = None

    # фон
    screen.fill((0, 0, 0))

    # brush
    for b in brush_lines:
        pygame.draw.line(screen, b[0], b[1], b[2], 5)

    #shapes
    for s in shapes:
        if s[0] == "rect":
            pygame.draw.rect(screen, s[1], s[2], 2)

        elif s[0] == "circle":
            pygame.draw.circle(screen, s[1], s[2], s[3], 3)

    pygame.display.flip()

pygame.quit()