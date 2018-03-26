import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    blue = (135, 206, 235)

    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(blue)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        gf.check_events(ship)
        ship.update()
        # Watch for keyboard and watch events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship)

        # Make the most recently draw screen visible
        pygame.display.flip()

run_game()
