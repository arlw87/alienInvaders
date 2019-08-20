import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship """

    def __init__(self, settings, screen, rocket):
        """create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        #create a bullet rectangle at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        #set the rectangle center position to the center position of the ship
        self.rect.centerx = rocket.rect.centerx
        self.rect.top = rocket.rect.top

        #store the y position of the bullet as a decimal
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speedFactor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speedFactor
        #update the rectangles update_position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
