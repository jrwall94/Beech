# Basic pygame setup
import pygame
pygame.init()
import random
random.seed()

# Get display size so any screen works
screen_dimensions = pygame.display.Info()
screen_x = screen_dimensions.current_w
screen_y = screen_dimensions.current_h
screen = pygame.display.set_mode((screen_x, screen_y))

running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, size=30)

# Starting in the middle
char_x = screen.get_width() / 2 - 25
char_y = screen.get_height() / 2 - 25

# Make random coordinates for 3 chickens, between 20 and screensize-100
### Make sure they do not overlap
chicken1_x = random.randrange(20, screen_x - 100)
chicken1_y = random.randrange(20, screen_y - 100)
chicken2_x = random.randrange(20, screen_x - 100)
chicken2_y = random.randrange(20, screen_y - 100)
chicken3_x = random.randrange(20, screen_x - 100)
chicken3_y = random.randrange(20, screen_y - 100)

squirrel_x = random.randrange(20, screen_x - 100)
squirrel_y = random.randrange(20, screen_y - 100)

char_xspeed = 0
char_yspeed = 0

chicken1_hit = False
chicken2_hit = False
chicken3_hit = False
chicken_counter = 0
squirrel_hit = False

# Start the game
while running:

    # Set framerate to 60
    # delta is time since last frame (in seconds) - Use for physics independent of framerate
    delta = clock.tick(60) / 1000
    if not squirrel_hit:
        max_speed = delta * 160
    # Squirrel gives a speedboost
    elif squirrel_hit:
        max_speed = delta * 500

    # Called before other rendering to hide old images
    # Currently forest green
    screen.fill((34, 139, 34))

    # Time to bring in the chicken
    chicken_img = pygame.image.load('roast_chicken.png')
    chicken_img = pygame.transform.scale(chicken_img, (chicken_img.get_width() / 10, chicken_img.get_height() / 10))
    # Colorkey initially found using colour picker in Paint, then cropped manually in GIMP

    # Same for the squirrel
    squirrel_img = pygame.image.load('squirrel.png')
    squirrel_img = pygame.transform.scale(squirrel_img, (squirrel_img.get_width() / 10, squirrel_img.get_height() / 10))
    squirrel_img.convert_alpha()

    # Draw the chickens, erase them when they get hit
    if not chicken1_hit:
        screen.blit(chicken_img, (chicken1_x, chicken1_y))
    if not chicken2_hit:
        screen.blit(chicken_img, (chicken2_x, chicken2_y))
    if not chicken3_hit:
        screen.blit(chicken_img, (chicken3_x, chicken3_y))
    if not squirrel_hit:
        screen.blit(squirrel_img, (squirrel_x, squirrel_y))

    hitbox_chicken1 = pygame.Rect(chicken1_x, chicken1_y, chicken_img.get_width(), chicken_img.get_height())
    hitbox_chicken2 = pygame.Rect(chicken2_x, chicken2_y, chicken_img.get_width(), chicken_img.get_height())
    hitbox_chicken3 = pygame.Rect(chicken3_x, chicken3_y, chicken_img.get_width(), chicken_img.get_height())
    hitbox_squirrel = pygame.Rect(squirrel_x, squirrel_y, squirrel_img.get_width(), squirrel_img.get_height())

    # Remove the chicken hitbox when the chicken gets hit
    ### For now it is just moved off the screen due to conflict types
    if chicken1_hit:
        hitbox_chicken1 = pygame.Rect(-200, -200, chicken_img.get_width(), chicken_img.get_height())
    if chicken2_hit:
        hitbox_chicken2 = pygame.Rect(-200, -200, chicken_img.get_width(), chicken_img.get_height())
    if chicken3_hit:
        hitbox_chicken3 = pygame.Rect(-200, -200, chicken_img.get_width(), chicken_img.get_height())
    if squirrel_hit:
        hitbox_squirrel = pygame.Rect(-200, -200, squirrel_img.get_width(), squirrel_img.get_height())

    # Event queue
    for event in pygame.event.get():
        # Quit program if the top right X is clicked or ESC is pressed
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw rectangle in middle of screen
    pygame.draw.rect(screen,'black',(char_x, char_y, 50, 50))

    ### replace dimensions with char_img.get_width(), char_img.get_width() after using custom image
    hitbox_player = pygame.Rect(char_x, char_y, 50, 50)

    collision1 = hitbox_chicken1.colliderect(hitbox_player)
    collision2 = hitbox_chicken2.colliderect(hitbox_player)
    collision3 = hitbox_chicken3.colliderect(hitbox_player)
    collision_squirrel = hitbox_squirrel.colliderect(hitbox_player)


    if collision1:
        chicken1_hit = True
        chicken_counter += 1
    if collision2:
        chicken2_hit = True
        chicken_counter += 1
    if collision3:
        chicken3_hit = True
        chicken_counter += 1
    if collision_squirrel:
        squirrel_hit = True

    # Level 1 Message
    welcome_text = font.render('Level 1', True, ('white'))
    screen.blit(welcome_text, (screen_x - 85, 10))
    # Chicken counter message
    objective_text = font.render(f"{chicken_counter} Chickens Collected", True, ('white'))
    screen.blit(objective_text, (10, 10))
    # Leave info message
    escape_text = font.render('Press ESC to quit', True, ('white')) 
    screen.blit(escape_text, (screen_x - 185, 40))

    # Victory message
    victory_text = font.render('Congratulations! You collected all the chickens!', True, ('white'))
    if chicken_counter == 3:
        screen.blit(victory_text, (screen_x / 2 - 250, screen_y / 2 - 10))

    # The WASD / Arrow key controls for the game
    # Constrain the character to the playing screen
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_a] or pressed[pygame.K_LEFT]) and char_x > 0:
        char_x -= max_speed
    if (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]) and char_x < screen_x - 50:
        char_x += max_speed
    if (pressed[pygame.K_w] or pressed[pygame.K_UP]) and char_y > 0:
        char_y -= max_speed
    if (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and char_y < screen_y - 50:
        char_y += max_speed

    # Make the changes to the display
    pygame.display.flip()
