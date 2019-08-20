#This file will have a class for the aliens
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, screen, settings):
        #Sprite Inheritance
        super(Alien, self).__init__()
        self.settings = settings
        self.screen = screen
        self.scaling_factor = 10

        #load image, scale and get rect of image
        self.image = pygame.image.load('images/ufo.bmp')
        #print("width: ", self.image.get_width())
        #print("height: ", self.image.get_height())
        #this scales the images surface
        self.image = pygame.transform.scale(self.image, ((int(self.image.get_width()/self.scaling_factor)),(int(self.image.get_height()/self.scaling_factor))))
        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()

        self.alien_width = self.rect.width
        self.alien_height = self.rect.height

        #start the alien at the top left of the screen
        #leave a space of one width and one height of the ufo
        self.rect.y = self.alien_height
        self.rect.x = self.alien_width

        #store the aliens position
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the ship at its current lcoation"""
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        if self.rect.right > self.settings.screen_width:
            #print("Edge")
            return True
        elif self.rect.left < 0:
            #print("Edge")
            return True
        else:
            return False

    def update(self):
        #print("Direction: ", self.settings.fleet_direction)
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
