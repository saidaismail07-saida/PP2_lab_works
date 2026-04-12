import pygame

pygame.init()

screen_size = width, height = (600, 600)

screen = pygame.display.set_mode(screen_size)

COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

done = False
is_green = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_green = not is_green
    if is_green:
        screen.fill(COLOR_GREEN)
        pygame.draw.circle(screen, COLOR_BLUE, (100, 100), 100, 4)
    else:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_GREEN, (100, 100), 100, 4)
    pygame.display.flip()

pygame.quit()