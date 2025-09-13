# Basic pygame setup
import pygame
pygame.init()
import random
random.seed()

# Import the levels
from level_one import level1

def start_screen():
    screen_dimensions = pygame.display.Info()
    screen_x = screen_dimensions.current_w
    screen_y = screen_dimensions.current_h
    screen = pygame.display.set_mode((screen_x, screen_y))

    running = True
    font = pygame.font.Font(None, size=30)

    while running:

        for event in pygame.event.get():
            # Quit program if the top right X is clicked or ESC is pressed
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1_collision:
                    level1()

        # Find the poisition of the mouse on the screen
        mouse_position = pygame.mouse.get_pos()

        welcome_message = font.render("Welcome to Beech's Big Adventure!", True, 'white')
        screen.blit(welcome_message, (screen_x / 2 - 170, 20))
        selection_message = font.render("Please choose a level!", True, 'white')
        screen.blit(selection_message, (screen_x / 2 - 100, 50))
        escape_text = font.render('Press ESC to quit', True, ('white')) 
        screen.blit(escape_text, (screen_x - 185, 20))

        # Hitbox for level 1
        level1_hitbox = pygame.Rect(120, 190, 130, 120)

        # Images and text for level 1
        level1_message = font.render("Level 1", True, 'white')
        screen.blit(level1_message, (150, 200))

        chicken_img = pygame.image.load('roast_chicken.png')
        chicken_img = pygame.transform.scale(chicken_img, (chicken_img.get_width() / 5, chicken_img.get_height() / 5))
        screen.blit(chicken_img, (120, 200))

        level1_collision = level1_hitbox.collidepoint(mouse_position)

        pygame.display.flip()

start_screen()