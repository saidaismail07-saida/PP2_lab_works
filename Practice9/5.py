import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

screen.fill("white")

color   = (0, 0, 0)
radius  = 5
drawing = False

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  color = (255, 0, 0)
            if event.key == pygame.K_g:  color = (0, 255, 0)
            if event.key == pygame.K_p:  color = (255, 0, 255)
            if event.key == pygame.K_o:  color = (255, 165, 0)
            if event.key == pygame.K_y:  color = (255, 255, 0)
            if event.key == pygame.K_b:  color = (0, 0, 255)
            if event.key == pygame.K_k:  color = (0, 0, 0)
            if event.key == pygame.K_e:  color = (255, 255, 255)  # eraser
            if event.key == pygame.K_c:  screen.fill("white")     # clear
            if event.key == pygame.K_UP:   radius = min(radius + 2, 50)
            if event.key == pygame.K_DOWN: radius = max(radius - 2, 1)

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, mouse_pos, radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()