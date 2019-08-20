import os

class Settings():
    """A class to store all settings for ALien Invasion"""

    def __init__(self):
        """The initial game settings"""
        """These are the static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (230, 230, 230)
        #
        #bullet Settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5


        # 1 is moving to the right, -1 moving to the left
        self.fleet_direction = 1

        #GameStat settings
        self.ship_limit = 3

        #button Settings
        self.green_button = (0, 250, 0)
        self.red_button = (250, 0, 0)

        self.speed_up_factor = 1.1
        self.score_factor = 1.5

        #sounds
        #music location
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.musicName = 'musicTrack.wav'
        self.musicPath = "%s/sounds/%s" %(self.dir_path, self.musicName)

        self.laserSoundsName = "Laser_Gun_short.wav"
        self.laserSoundsPath = "%s/sounds/%s" %(self.dir_path, self.laserSoundsName)

        self.endGameMusic = "someMusic.wave"

        self.resest_dynamic_settings()

    def resest_dynamic_settings(self):
        self.bullet_speed_factor = 3
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.rocket_speed_factor = 2
        self.alien_points = 50

    def increase_speed(self):
        self.bullet_speed_factor *= self.speed_up_factor
        self.alien_speed *= self.speed_up_factor
        #self.fleet_drop_speed *= self.speed_up_factor = 1.1
        self.rocket_speed_factor *= self.speed_up_factor
        self.alien_points = int(self.score_factor * self.alien_points)
