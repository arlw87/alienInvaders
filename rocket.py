import pygame

class Rocket():
    def __init__(self, screen, settings):
        """intitlises the ship and setsd its starting postion"""
        self.screen = screen
        self.scaling_factor = 6

        self.settings = settings
        #load the ship image and get its rects
        self.image = pygame.image.load('images/rocket.bmp')
        print("width: ", self.image.get_width())
        print("height: ", self.image.get_height())
        #this scales the images surface
        self.image = pygame.transform.scale(self.image, ((int(self.image.get_width()/self.scaling_factor)),(int(self.image.get_height()/self.scaling_factor))))
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        print(self.rect)

        #start the rcoket at the bottom center of the screen_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #moving right flag
        self.moving_right = False
        self.moving_left = False

        #get rocket height
        self.rocket_height = self.rect.height

    def blitme(self):
        """Draw the ship at its current lcoation"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.rect.bottomright < self.screen_rect.bottomright:
            if self.moving_right == True:
                self.rect.centerx = self.rect.centerx + self.settings.rocket_speed_factor
        if self.rect.bottomleft > self.screen_rect.bottomleft:
            if self.moving_left == True:
                self.rect.centerx = self.rect.centerx - self.settings.rocket_speed_factor
        #print("pos", self.rect.centerx)
