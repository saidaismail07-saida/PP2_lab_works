import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

mode = "white"
tool = "brush"

shapes = []
brush_lines = []

start_pos = None
last_pos = None


def get_color(mode):
    return {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "white": (255, 255, 255)
    }[mode]


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
            if event.key == pygame.K_w:
                mode = "white"

            if event.key == pygame.K_1:
                tool = "brush"
            if event.key == pygame.K_2:
                tool = "rect"
            if event.key == pygame.K_3:
                tool = "circle"
            if event.key == pygame.K_4:
                tool = "square"
            if event.key == pygame.K_5:
                tool = "rtriangle"
            if event.key == pygame.K_6:
                tool = "etriangle"
            if event.key == pygame.K_7:
                tool = "rhombus"
            if event.key == pygame.K_e:
                tool = "eraser"

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            color = get_color(mode)

            x = min(start_pos[0], end_pos[0])
            y = min(start_pos[1], end_pos[1])
            w = abs(start_pos[0] - end_pos[0])
            h = abs(start_pos[1] - end_pos[1])

            if tool == "rect":
                shapes.append(("rect", color, (x, y, w, h)))

            elif tool == "circle":
                r = int(math.dist(start_pos, end_pos))
                shapes.append(("circle", color, start_pos, r))

            elif tool == "square":
                size = min(w, h)
                shapes.append(("square", color, (x, y, size)))

            elif tool == "rtriangle":
                points = [(x, y), (x, y + h), (x + w, y + h)]
                shapes.append(("poly", color, points))

            elif tool == "etriangle":
                points = [
                    (x + w // 2, y),
                    (x, y + h),
                    (x + w, y + h)
                ]
                shapes.append(("poly", color, points))

            elif tool == "rhombus":
                points = [
                    (x + w // 2, y),
                    (x + w, y + h // 2),
                    (x + w // 2, y + h),
                    (x, y + h // 2)
                ]
                shapes.append(("poly", color, points))

    if pygame.mouse.get_pressed()[0] and tool in ["brush", "eraser"]:
        pos = pygame.mouse.get_pos()

        color = (0, 0, 0) if tool == "eraser" else get_color(mode)

        if last_pos is not None:
            brush_lines.append((color, last_pos, pos))

        last_pos = pos
    else:
        last_pos = None

    screen.fill((0, 0, 0))

    for line in brush_lines:
        pygame.draw.line(screen, line[0], line[1], line[2], 5)

    for s in shapes:
        if s[0] == "rect":
            pygame.draw.rect(screen, s[1], s[2], 2)

        elif s[0] == "circle":
            pygame.draw.circle(screen, s[1], s[2], s[3], 2)

        elif s[0] == "square":
            pygame.draw.rect(screen, s[1], (s[2][0], s[2][1], s[2][2], s[2][2]), 2)

        elif s[0] == "poly":
            pygame.draw.polygon(screen, s[1], s[2], 2)

    pygame.display.flip()

pygame.quit()