# Only once per file
import pygame
pygame.init()

# Get display size so any screen works
screen_dimensions = pygame.display.Info()
screen_x = screen_dimensions.current_w
screen_y = screen_dimensions.current_h
screen = pygame.display.set_mode((screen_x, screen_y))

running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, size=30)

while running:
    for event in pygame.event.get():
        # Quit program if the top right X is clicked or ESC is pressed
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    delta = clock.tick(60) / 1000

    pygame.display.flip()