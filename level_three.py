# Only once per file
import pygame
pygame.init()
import math
import time

### Features to add:
### Save to file when the application is closed (save treats and number of each building)

def level3():

    # Get display size so any screen works
    screen_dimensions = pygame.display.Info()
    screen_x = screen_dimensions.current_w
    screen_y = screen_dimensions.current_h
    screen = pygame.display.set_mode((screen_x, screen_y))

    running = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, size=30)

    TREAT_UPDATE = pygame.USEREVENT + 1
    pygame.time.set_timer(TREAT_UPDATE, 1000)

    shopping = False
    # Set higher for testing
    starting_treats = 0
    treats = starting_treats
    # Shoppers
    shoppers = 0
    cost_shoppers = 10
    shoppers_speed = 2
    shoppers_colour = 'white'
    # Brokers
    brokers = 0
    cost_broker = 150
    broker_speed = 24
    broker_colour = 'white'
    # Supermarkets
    markets = 0
    cost_market = 2000
    market_speed = 300
    market_colour = 'white'
    # Treat Factories
    factories = 0
    cost_factory = 100000
    factory_speed = 40000
    factory_colour = 'white'
    # Puppy Wizards
    wizards = 0
    cost_wizard = 8000000
    wizard_speed = 640000
    wizard_colour = 'white'
    # Doggy Overlords
    overlords = 0
    cost_overlord = 100000000
    overlord_speed = 8000000
    overlord_colour = 'white'
    # Sophie
    sophies = 0
    cost_sophie = 6000000000
    sophie_speed = 500000000
    sophie_colour = 'white'

    # Ascend
    win = False
    first_loop = True
    cost_ascend = 100000000000
    victory_message = font.render("Congratulations! You have ascended!", True, 'white')
    victory_message2 = font.render("You are now a dog treat!!", True, 'white')
    escape_message = font.render(".", True, 'white')
    escape_message2 = font.render("Press <ESC> to go back to the main menu", True, 'white')
    ascend_message = font.render(f"cost: {cost_ascend:,}", True, 'white')

    # Load all of the images
    shopper_img = pygame.image.load('personal_shopper.png').convert_alpha()
    shopper_img = pygame.transform.scale(shopper_img, (shopper_img.get_width() / 2, shopper_img.get_height() / 2))
    broker_img = pygame.image.load('broker.png').convert_alpha()
    broker_img = pygame.transform.scale(broker_img, (broker_img.get_width() / 8, broker_img.get_height() / 8))
    market_img = pygame.image.load('supermarket.png').convert_alpha()
    market_img = pygame.transform.scale(market_img, (market_img.get_width() / 5, market_img.get_height() / 5))
    factory_img = pygame.image.load('factory.png').convert_alpha()
    factory_img = pygame.transform.scale(factory_img, (factory_img.get_width() / 12, factory_img.get_height() / 12))
    wizard_img = pygame.image.load('wizard.png').convert_alpha()
    wizard_img = pygame.transform.scale(wizard_img, (wizard_img.get_width() / 12, wizard_img.get_height() / 12))
    overlord_img =pygame.image.load('overlord.png').convert_alpha()
    overlord_img = pygame.transform.scale(overlord_img, (overlord_img.get_width() / 2, overlord_img.get_height() / 2))
    sophie_img = pygame.image.load('sophie.png').convert_alpha()
    sophie_img = pygame.transform.scale(sophie_img, (sophie_img.get_width() / 5, sophie_img.get_height() / 5))

    while running:

        screen.fill('purple')

        treat_rate = ((shoppers * shoppers_speed) + (brokers * broker_speed) + (markets * market_speed) + (factories * factory_speed) +
                    (wizards * wizard_speed) + (overlords * overlord_speed) + (sophies * sophie_speed)
                    )

        for event in pygame.event.get():
            # Quit program if the top right X is clicked or ESC is pressed
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # Update treats here, occurs once per half second
            if event.type == TREAT_UPDATE:
                treats += treat_rate
            # Click treat to gain 1 treat
            if event.type == pygame.MOUSEBUTTONDOWN:
                if collision_treat:
                    treats += 1
                elif collision_shopper and treats >= cost_shoppers:
                    shoppers += 1
                    treats -= cost_shoppers
                    cost_shoppers = math.ceil(cost_shoppers * 1.1)
                elif collision_broker and treats >= cost_broker:
                    brokers += 1
                    treats -= cost_broker
                    cost_broker = math.ceil(cost_broker * 1.1)
                elif collision_market and treats >= cost_market:
                    markets += 1
                    treats -= cost_market
                    cost_market = math.ceil(cost_market * 1.2)
                elif collision_factory and treats >= cost_factory:
                    factories += 1
                    treats -= cost_factory
                    cost_factory = math.ceil(cost_factory * 1.3)
                elif collision_wizard and treats >= cost_wizard:
                    wizards += 1
                    treats -= cost_wizard
                    cost_wizard = math.ceil(cost_wizard * 1.3)
                elif collision_overlord and treats >= cost_overlord:
                    overlords += 1
                    treats -= cost_overlord
                    cost_overlord = math.ceil(cost_overlord * 1.2)
                elif collision_sophie and treats >= cost_sophie:
                    sophies += 1
                    treats -= cost_sophie
                    cost_sophie = math.ceil(cost_sophie * 1.1)
                elif collision_ascend and treats >= cost_ascend:
                    win = True
                    running = False

        mouse_position = pygame.mouse.get_pos()

        # Uncomment to see hitboxes
        # # Shopper
        # pygame.draw.rect(screen, 'blue', (390, 90, 420, 40))
        # # Broker
        # pygame.draw.rect(screen, 'blue', (390, 190, 420, 40))
        # # Market
        # pygame.draw.rect(screen, 'blue', (390, 290, 420, 40))
        # # Factory
        # pygame.draw.rect(screen, 'blue', (390, 390, 420, 40))
        # # Wizards
        # pygame.draw.rect(screen, 'blue', (390, 490, 420, 40))
        # # Overlords
        # pygame.draw.rect(screen, 'blue', (390, 590, 420, 40))
        # # Sophies
        # pygame.draw.rect(screen, 'blue', (390, 690, 420, 40))

        if treats >= 1:
            shopping = True
        
        treat_image = pygame.image.load('dog_treat.png').convert_alpha()
        treat_width = treat_image.get_width() / 15
        treat_height = treat_image.get_height() / 15
        treat_x = 190
        treat_y = screen_y / 2 - 30
        # Uncomment to see treat hitbox
        # pygame.draw.rect(screen, 'brown', (190, screen_y / 2 - 30, 130, 60))
        hitbox_treat = pygame.Rect(190, screen_y / 2 - 30, 130, 60)
        collision_treat = hitbox_treat.collidepoint(mouse_position)
        # Make the treat bigger when you mouse over it
        if collision_treat:
            treat_width = treat_image.get_width() / 10
            treat_height = treat_image.get_height() / 10
            treat_x = 160
            treat_y = screen_y / 2 - 43

        treat_image = pygame.transform.scale(treat_image, (treat_width, treat_height))
        screen.blit(treat_image, (treat_x, treat_y))



        treat_counter = font.render(f"Treats: {treats:,}", True, 'white')
        screen.blit(treat_counter, (50, 20))

        # Shoppers
        buy_shopper = font.render(f"Buy 1 personal shopper (cost: {cost_shoppers:,} treats)", True, shoppers_colour)
        if shopping:
            screen.blit(buy_shopper, (750, 100))
        hitbox_shopper = pygame.Rect(750, 90, 420, 40)
        collision_shopper = hitbox_shopper.collidepoint(mouse_position)
        
        if collision_shopper:
            if treats >= cost_shoppers:
                shoppers_colour = 'green'
            elif treats < cost_shoppers:
                shoppers_colour = 'red'
        else:
            shoppers_colour = 'white'

        # Brokers
        buy_broker = font.render(f"Buy 1 treat broker (cost: {cost_broker:,} treats)", True, broker_colour)
        if shoppers >= 1:
            screen.blit(buy_broker, (750, 200))
        hitbox_broker = pygame.Rect(750, 190, 420, 40)
        collision_broker = hitbox_broker.collidepoint(mouse_position)
        
        if collision_broker:
            if treats >= cost_broker:
                broker_colour = 'green'
            elif treats < cost_broker:
                broker_colour = 'red'
        else:
            broker_colour = 'white'

        # Markets
        buy_market = font.render(f"Buy 1 Supermarket (cost: {cost_market:,} treats)", True, market_colour)
        if brokers >= 1:
            screen.blit(buy_market, (750, 300))
        hitbox_market = pygame.Rect(750, 290, 420, 40)
        collision_market = hitbox_market.collidepoint(mouse_position)
        
        if collision_market:
            if treats >= cost_market:
                market_colour = 'green'
            elif treats < cost_market:
                market_colour = 'red'
        else:
            market_colour = 'white'

        # Factories
        buy_factory = font.render(f"Buy 1 Treat Factory (cost: {cost_factory:,} treats)", True, factory_colour)
        if markets >= 1:
            screen.blit(buy_factory, (750, 400))
        hitbox_factory = pygame.Rect(750, 390, 420, 40)
        collision_factory = hitbox_factory.collidepoint(mouse_position)
        
        if collision_factory:
            if treats >= cost_factory:
                factory_colour = 'green'
            elif treats < cost_factory:
                factory_colour = 'red'
        else:
            factory_colour = 'white'

        # Wizards
        buy_wizard = font.render(f"Buy 1 Puppy Wizard (cost: {cost_wizard:,} treats)", True, wizard_colour)
        if factories >= 1:
            screen.blit(buy_wizard, (750, 500))
        hitbox_wizard = pygame.Rect(750, 490, 420, 40)
        collision_wizard = hitbox_wizard.collidepoint(mouse_position)
        
        if collision_wizard:
            if treats >= cost_wizard:
                wizard_colour = 'green'
            elif treats < cost_wizard:
                wizard_colour = 'red'
        else:
            wizard_colour = 'white'

        # Overlords
        buy_overlord = font.render(f"Buy 1 Dog Overlord (cost: {cost_overlord:,} treats)", True, overlord_colour)
        if wizards >= 1:
            screen.blit(buy_overlord, (750, 600))
        hitbox_overlord = pygame.Rect(750, 590, 420, 40)
        collision_overlord = hitbox_overlord.collidepoint(mouse_position)
        
        if collision_overlord:
            if treats >= cost_overlord:
                overlord_colour = 'green'
            elif treats < cost_overlord:
                overlord_colour = 'red'
        else:
            overlord_colour = 'white'

        # Sophies
        buy_sophie = font.render(f"Buy 1 Sophie (cost: {cost_sophie:,} treats)", True, sophie_colour)
        if overlords >= 1:
            screen.blit(buy_sophie, (750, 700))
        hitbox_sophie = pygame.Rect(750, 690, 420, 40)
        collision_sophie = hitbox_sophie.collidepoint(mouse_position)
        
        if collision_sophie:
            if treats >= cost_sophie:
                sophie_colour = 'green'
            elif treats < cost_sophie:
                sophie_colour = 'red'
        else:
            sophie_colour = 'white'

        # Ascend

        ascend_x = 105
        ascend_y = screen_y - 300
        ascend_img = pygame.image.load('ascend.png').convert_alpha()
        ascend_width = ascend_img.get_width() / 5
        ascend_height = ascend_img.get_height() / 5
        # pygame.draw.rect(screen, 'blue', (160, screen_y - 250, 200, 100))
        hitbox_ascend = pygame.Rect(160, screen_y-250, 200, 100)
        collision_ascend = hitbox_ascend.collidepoint(mouse_position)
        if collision_ascend:
            ascend_width = ascend_width * 1.5
            ascend_height = ascend_height * 1.5
            ascend_x = 30
            ascend_y = screen_y - 350
        ascend_img = pygame.transform.scale(ascend_img, (ascend_width, ascend_height))

        # List of purchases
        shopper_counter = font.render(f"Personal Shoppers: {shoppers:,} providing {(shoppers * shoppers_speed):,} treats per second", True, 'white')
        if shopping:
            screen.blit(shopper_counter, (750, 125))
            screen.blit(shopper_img, (625, 50))
        broker_counter = font.render(f"Treat Brokers: {brokers:,} providing {(brokers * broker_speed):,} treats per second", True, 'white')
        if shoppers >= 1:
            screen.blit(broker_counter, (750, 225))
            screen.blit(broker_img, (640, 175))
        market_counter = font.render(f"Supermarkets: {markets:,} providing {(markets * market_speed):,} treats per second", True, 'white')
        if brokers >= 1:
            screen.blit(market_counter, (750, 325))
            screen.blit(market_img, (615, 260))
        factory_counter = font.render(f"Treat Factories: {factories:,} providing {(factories * factory_speed):,} treats per second", True, 'white')
        if markets >= 1:
            screen.blit(factory_counter, (750, 425))
            screen.blit(factory_img, (625, 380))
        wizard_counter = font.render(f"Puppy Wizards: {wizards:,} providing {wizards * wizard_speed:,} treats per second", True, 'white')
        if factories >= 1:
            screen.blit(wizard_counter, (750, 525))
            screen.blit(wizard_img, (635, 470))
        overlord_counter = font.render(f"Dog Overlords: {overlords:,} providing {overlords * overlord_speed:,} treats per second", True, 'white')
        if wizards >= 1:
            screen.blit(overlord_counter, (750, 625))
            screen.blit(overlord_img, (625, 560))
        sophie_counter = font.render(f"Sophies: {sophies:,} providing {sophies * sophie_speed:,} treats per second", True, 'white')
        if overlords >= 1:
            screen.blit(sophie_counter, (750, 725))
            screen.blit(sophie_img, (645, 675))
        if sophies >= 1:
            screen.blit(ascend_img, (ascend_x, ascend_y))
            screen.blit(ascend_message, (150, screen_y - 120))

        # Total rate
        treat_rate = font.render(f"Total treats per second: {treat_rate:,}", True, 'white')
        screen.blit(treat_rate, (650, screen_y - 60))

        delta = clock.tick(60) / 1000

        pygame.display.flip()

    dot_x = screen_x / 2 - 50

    while win:

        if first_loop:
            screen.fill('purple')
            pygame.display.flip()
            time.sleep(1.5)
            screen.fill((203, 179, 135))
            pygame.display.flip()
            time.sleep(1.5)
            screen.blit(victory_message, (screen_x / 2 - 190, screen_y / 2 - 150))
            pygame.display.flip()
            time.sleep(1.5)
            screen.blit(victory_message2, (screen_x / 2 - 120, screen_y / 2 - 100))
            pygame.display.flip()
            time.sleep(1.5)
            for i in range(10):
                screen.blit(escape_message, (dot_x, screen_y / 2 - 50))
                pygame.display.flip()
                dot_x += 10
                time.sleep(0.5)
            screen.blit(escape_message2, (screen_x / 2 - 200, screen_y / 2 + 10))
            pygame.display.flip()
            time.sleep(0.5)
            first_loop = False

        for event in pygame.event.get():
            # Quit program if the top right X is clicked or ESC is pressed
            if event.type == pygame.QUIT: 
                win = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    win = False
        
        pygame.display.flip()