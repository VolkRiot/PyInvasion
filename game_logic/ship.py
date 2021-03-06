import pygame

class Ship():
    
    def __init__(self, screen):
        # Initialize ship and place at staritn postion constructor
        self.screen = screen
        
        # Load the ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Create ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement boolean
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        # Draw ship
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
