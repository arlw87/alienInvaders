class GameStats():
    """Track the stats of alien invaders"""

    def __init__(self, settings):
        self.settings = settings
        #dont start the game automatically
        self.game_active = False
        self.game_over = False
        self.high_score = 0
        self.reset_stats()

        #new stats


    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.level = 1
        self.score = 0
