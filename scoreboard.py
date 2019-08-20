import pygame.font

class Scoreboard():
    """A class to report the score of the game"""

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        #font Settings
        self.text_size = 30
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, self.text_size)

        self.back_ground_color = (0,0,0)
        self.high_score = 0

        #Prepare the intial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_lives(self):
        self.image_lives = pygame.image.load('images/rocket.bmp')
        self.scaling_factor = 14
        self.image_lives = pygame.transform.scale(self.image_lives, ((int(self.image_lives.get_width()/self.scaling_factor)),(int(self.image_lives.get_height()/self.scaling_factor))))
        self.rect_lives = self.image_lives.get_rect()
        self.rect_lives.top = 10
        self.rect_lives.left = self.screen_rect.left + 20


    def prep_score(self):
        current_score = self.stats.score
        round_score = int(round(current_score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 10

    def prep_high_score(self):
        self.high_score = self.stats.high_score
        high_score_str = "High Score: {:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.center = self.screen_rect.center
        self.high_score_image_rect.top = 10

    def prep_level(self):
        self.level = self.stats.level
        #print("In SB Class, Level: ",self.level)
        level_str = "Level: {}".format(self.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.screen_rect.right - 20
        self.level_image_rect.top = 30

    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        for rockets_left in range(self.stats.ships_left):
            self.rect_lives.left = (self.screen_rect.left + 20) + (rockets_left * 2 * self.image_lives.get_width())
            self.screen.blit(self.image_lives, self.rect_lives)
