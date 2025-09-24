# Only once per file
import pygame
pygame.init()
import random
import time

def level4():

    looping = True
    level = 1

    while looping:

        random.seed()
        # Get display size so any screen works
        screen_dimensions = pygame.display.Info()
        screen_x = screen_dimensions.current_w
        screen_y = screen_dimensions.current_h
        screen = pygame.display.set_mode((screen_x, screen_y))

        running = True
        looping = True
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, size=30)

        goose_x = screen_x / 2 - 60
        goose_y = screen_y / 2

        num_geese = level + 1

        victory = False

        geese_velx = []
        geese_vely = []

        geese_x = [screen_x / 2 - 60] * num_geese
        geese_y = [screen_y - 170 - 51] * num_geese
        hit_counter = 0
        first_time = True

        # Initialize with a time ahead of the present. This will break in ~32,000 years. Update before then
        beat_time = 1_000_000_000_000

        hitbox_geese = [0] * num_geese
        collision_geese = [0] * num_geese
        geese_rect = [0] * num_geese
        goose_colour = ['white'] * num_geese
        geese_dead = [False] * num_geese

        # Goose velocity
        for goose_velx in range(num_geese):
            geese_velx.append(random.randint(-8, 8))

        for goose_vely in range(num_geese):
            geese_vely.append(random.randint(-10, -3))


        while running:

            delta = clock.tick(60) / 1000

            mouse_position = pygame.mouse.get_pos()

            screen.fill((135, 206, 235))

            level_message = font.render(f"Level {level}", True, 'black')
            screen.blit(level_message, (screen_x / 2 - 30, 10))

                # Draw goose hitboxes
            for i in range(num_geese):
                hitbox_geese[i] = (pygame.Rect(geese_x[i], geese_y[i], 120, 50))
                collision_geese[i] = hitbox_geese[i].collidepoint(mouse_position)

            for event in pygame.event.get():
                # Quit program if the top right X is clicked or ESC is pressed
                if event.type == pygame.QUIT: 
                    running = False
                    looping = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        looping = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(num_geese):
                        if collision_geese[i] and not geese_dead[i]:
                            goose_colour[i] = 'red'
                            geese_dead[i] = True
                            hit_counter += 1


            # Draw geese (hidden behind grass)

            # Move outside of while loop once set

            # Draw grass ground
            pygame.draw.rect(screen, (124, 252, 0), (0, screen_y - 170, screen_x, 170))

            # for goose in range(3):
            for goose in range(num_geese):
                geese_rect[goose] = pygame.draw.rect(screen, goose_colour[goose], (geese_x[goose], geese_y[goose], 120, 50))

            

            # Draw shooter
            pygame.draw.rect(screen, 'black', (screen_x / 2 - 30, screen_y - 200, 60, 100))

            # Move goose
            for goose in range(num_geese):
                geese_y[goose] += geese_vely[goose]
                geese_x[goose] += geese_velx[goose]

                # Bounce goose if it hits the edge of screen
                if geese_dead[goose] == False:
                    if geese_y[goose] <= 0 or geese_y[goose] >= screen_y - 170 - 50:
                        geese_vely[goose] = -geese_vely[goose]
                    if geese_x[goose] <= 0 or geese_x[goose] >= screen_x - 120:
                        geese_velx[goose] = -geese_velx[goose]
                elif geese_dead[goose] == True:
                    geese_velx[goose] = 0
                    if geese_y[goose] <= screen_y - 50:
                        geese_vely[goose] = 10
                    else:
                        geese_vely[goose] = 0

            
            # If all the geese are dead, assign victory. Make sure it only happens once
            if all(geese_dead) and first_time:
                if level <= 9:
                    victory = True
                    first_time = False
                else:
                    victory_message = font.render("You Win!!", True, 'black')
                    exit_message = font.render("Press <ESC> to exit", True, 'black')
                    screen.blit(victory_message, (screen_x / 2 - 50, screen_y / 2 - 100))
                    screen.blit(exit_message, (screen_x / 2 - 100, screen_y / 2 - 70))

            if victory:
                beat_time = time.time()
                victory = False
            if time.time() - beat_time >= 2:
                break


            # If mouse collides with a goose, delete it

            # for i in range(num_geese):
            #     if collision_geese[i]:
            #         del geese_rect[i]
            #         num_geese -= 1

            pygame.display.flip()

        if level <= 9:
            level += 1
        else:
            looping = False