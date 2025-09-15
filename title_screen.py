# Basic pygame setup
import pygame
pygame.init()
import random
random.seed()

# Import the levels
from level_one import level1
from level_two import level2

def start_screen():
    screen_dimensions = pygame.display.Info()
    screen_x = screen_dimensions.current_w
    screen_y = screen_dimensions.current_h
    screen = pygame.display.set_mode((screen_x, screen_y))

    running = True
    font = pygame.font.Font(None, size=30)

    while running:

        screen.fill('black')

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
                if level2_collision:
                    level2()

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
        level2_hitbox = pygame.Rect(320, 190, 130, 120)

        # Uncomment to see the hitboxes
        # pygame.draw.rect(screen, 'green', (120, 190, 130, 120))
        # pygame.draw.rect(screen, 'green', (320, 190, 130, 120))

        # Images and text for level 1
        level1_message = font.render("Level 1", True, 'white')
        screen.blit(level1_message, (150, 200))
        chicken_img = pygame.image.load('roast_chicken.png')
        chicken_img = pygame.transform.scale(chicken_img, (chicken_img.get_width() / 5, chicken_img.get_height() / 5))
        screen.blit(chicken_img, (120, 200))
        level1_collision = level1_hitbox.collidepoint(mouse_position)

        # Images and text for level 2
        level2_message = font.render("Level 2", True, 'white')
        screen.blit(level2_message, (350, 200))
        seagull_img = pygame.image.load('seagull.png')
        seagull_img = pygame.transform.scale(seagull_img, (seagull_img.get_width() / 4, seagull_img.get_height() / 4))
        screen.blit(seagull_img, (335, 230))
        level2_collision = level2_hitbox.collidepoint(mouse_position)


        pygame.display.flip()

start_screen()