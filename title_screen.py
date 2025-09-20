# Basic pygame setup
import pygame
pygame.init()
import random
random.seed()
import time

# Import the levels
from level_one import level1
from level_two import level2
from level_three import level3

### Features to add:
### Make the buttons expand slightly when moused over

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
                if level3_collision:
                    level3()

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
        level3_hitbox = pygame.Rect(520, 190, 130, 120)

        # # Uncomment to see the hitboxes
        # pygame.draw.rect(screen, 'green', (120, 190, 130, 120))
        # pygame.draw.rect(screen, 'green', (320, 190, 130, 120))
        # pygame.draw.rect(screen, 'green', (520, 190, 130, 120))

        # Images and text for level 1
        chicken_x = 120
        chicken_y = 200
        level1_message = font.render("Level 1", True, 'white')
        screen.blit(level1_message, (150, 200))
        chicken_img = pygame.image.load('roast_chicken.png')
        chicken_width = chicken_img.get_width() / 5
        chicken_height = chicken_img.get_height() / 5
        level1_collision = level1_hitbox.collidepoint(mouse_position)
        if level1_collision:
            chicken_width = chicken_img.get_width() / 4
            chicken_height = chicken_img.get_height() / 4
            chicken_x = 105
            chicken_y = 185
        chicken_img = pygame.transform.scale(chicken_img, (chicken_width, chicken_height))
        screen.blit(chicken_img, (chicken_x, chicken_y))




        # Images and text for level 2 
        seagull_img = pygame.image.load('seagull.png')
        seagull_x = 335
        seagull_y = 230
        seagull_width = seagull_img.get_width() / 4
        seagull_height = seagull_img.get_height() / 4
        level2_message = font.render("Level 2", True, 'white')
        screen.blit(level2_message, (350, 200))
        level2_collision = level2_hitbox.collidepoint(mouse_position)
        if level2_collision:
            seagull_width = seagull_img.get_width() / 3
            seagull_height = seagull_img.get_height() / 3
            seagull_x = 320
            seagull_y = 215
        seagull_img = pygame.transform.scale(seagull_img, (seagull_width, seagull_height))
        screen.blit(seagull_img, (seagull_x, seagull_y))

        # Images and text for level 3
        dog_treat_img = pygame.image.load('dog_treat.png')
        dog_treat_x = 525
        dog_treat_y = 235
        dog_treat_width = dog_treat_img.get_width() / 16
        dog_treat_height = dog_treat_img.get_height() / 16
        level3_message = font.render("Level 3", True, 'white')
        screen.blit(level3_message, (550, 200))
        level3_collision = level3_hitbox.collidepoint(mouse_position)
        if level3_collision:
            dog_treat_width = dog_treat_img.get_width() / 13
            dog_treat_height = dog_treat_img.get_height() / 13
            dog_treat_x = 510
            dog_treat_y = 226
        dog_treat_img = pygame.transform.scale(dog_treat_img, (dog_treat_width, dog_treat_height))
        screen.blit(dog_treat_img, (dog_treat_x, dog_treat_y))

        pygame.display.flip()

start_screen()