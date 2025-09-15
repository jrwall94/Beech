# Only once per file
import pygame
pygame.init()
import random

def level2():

    noquit = True
    random.seed()

    while noquit:

        random.seed()

        # Get display size so any screen works
        screen_dimensions = pygame.display.Info()
        screen_x = screen_dimensions.current_w
        screen_y = screen_dimensions.current_h
        screen = pygame.display.set_mode((screen_x, screen_y))

        started = False
        running = True
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, size=30)
        font2 = pygame.font.Font(None, size=60)

        # Set framerate to 144
        # delta is time since last frame (in seconds) - Use for physics independent of framerate
        #*** First tick may be different from the ones following?
        delta = clock.tick(144) / 1000

        # Starting in the middle
        char_x = 350
        char_y = screen.get_height() / 2 - 50

        # Start motionless
        char_velocity = 0 * delta
        char_grav = 15 * delta
        max_velocity = 4.5
        pipe_speed = 200 * delta

        pipe_vert_gap = 200
        # Time between pipes in millisesconds
        pipe_wait_time = 2500

        dead = False
        score = 0
        intro_x = 120

        # Setup for drawing an adjustable number of pipes
        pipe_num = 0
        # Game will end abruptly after this many pipes. Reccomended: 100
        num_pipes = 100
        # Make an array of false, set to true as the pipes should spawn in
        # Use more than needed to give the program time to complete after the player finishes
        draw_pipe = [False] * (num_pipes + 10)
        PIPE_SPAWN = pygame.USEREVENT + 1
        pygame.time.set_timer(PIPE_SPAWN, pipe_wait_time)
        pipe_x = [screen_x] * num_pipes
        hitbox_pipe_upper = [0] * num_pipes
        hitbox_pipe_lower = [0] * num_pipes
        top_pipe_length = [0] * num_pipes
        collision = [False] * num_pipes
        for i in range(num_pipes):
            top_pipe_length[i] = random.randrange(50, screen_y - 300)

        while running:

            for event in pygame.event.get():
                # Quit program if the top right X is clicked or ESC is pressed
                if event.type == pygame.QUIT: 
                    running = False
                    noquit = False
                elif event.type == PIPE_SPAWN:
                    if started:
                        draw_pipe[pipe_num] = True
                        pipe_num += 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        noquit = False
                    elif dead and event.key == pygame.K_r:
                        running = False
                    elif event.key == pygame.K_SPACE and not dead:
                        started = True
                        char_velocity = -5
                        

            delta = clock.tick(144) / 1000

            screen.fill((135, 206, 235))

            # Draw the character on the screen
            pygame.draw.rect(screen,'black',(char_x, char_y, 40, 40))
            hitbox_player = pygame.Rect(char_x, char_y, 40, 40)

            if char_velocity < max_velocity:
                char_velocity += char_grav

            # Start things moving when player presses spacebar the first time
            if started:
                char_y += char_velocity
                # pipe1_x -= pipe_speed

            # collision1 = hitbox_player.colliderect(hitbox_pipe1_upper) or hitbox_player.colliderect(hitbox_pipe1_lower)

            # Draw num_pipes pipe pairs
            for i in range(num_pipes):
                if draw_pipe[i]:
                    pygame.draw.rect(screen, 'green', (pipe_x[i], 0, 60, top_pipe_length[i]))
                    pygame.draw.rect(screen, 'green', (pipe_x[i], top_pipe_length[i] + pipe_vert_gap , 60, screen_y - top_pipe_length[i] - pipe_vert_gap))
                    hitbox_pipe_upper[i] = pygame.Rect(pipe_x[i], 0, 60, top_pipe_length[i])
                    hitbox_pipe_lower[i] = pygame.Rect(pipe_x[i], top_pipe_length[i] + pipe_vert_gap , 60, screen_y - top_pipe_length[i] - pipe_vert_gap)
                    if started:
                        pipe_x[i] -= pipe_speed
                    collision[i] = hitbox_player.colliderect(hitbox_pipe_upper[i]) or hitbox_player.colliderect(hitbox_pipe_lower[i])
                if (350-(pipe_speed/2) < pipe_x[i] < 350+(pipe_speed/2)) and started:
                    score += 1

            score_message = font.render(f"Your score was {score}!", True, 'white')
            victory_message = font.render(f"Your score was {score}! You beat the game!!", True, 'white')
            # End if collision occurs
            if char_y < 0 or char_y > screen_y:
                started = False
                screen.blit(score_message, (screen_x / 2 - 120, screen_y / 2 - 40))
                dead = True
            if score == num_pipes:
                started = False
                screen.blit(victory_message, (screen_x / 2 - 210, screen_y / 2 - 40))
                dead = True
            for i in range(num_pipes):
                if collision[i] == True:
                    started = False
                    screen.blit(score_message, (screen_x / 2 - 120, screen_y / 2 - 40))
                    dead = True

            scorekeeper = font2.render(f"{score}", True, 'white')

            screen.blit(scorekeeper, (screen_x / 2 - 10, 20))



            if not dead:
                intro_message = font.render('Press <Spacebar> to begin', True, 'white')
            if dead:
                intro_message = font.render('Press <R> to restart, or <ESC> to quit', True, 'white')
                intro_x = 210
            if not started:
                screen.blit(intro_message, (screen_x / 2 - intro_x, screen_y / 2 - 20))


            # Show speeds if wanted for testing
            # temp_vel = font.render(f'{char_velocity}', True, 'white')
            # temp_grav = font.render(f'{char_grav}', True, 'white')

            # screen.blit(temp_vel, (30, 30))
            # screen.blit(temp_grav, (30, 60))

            pygame.display.flip()