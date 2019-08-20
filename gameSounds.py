#Sounds module
import pygame

class gameSounds():
    """A class for the sounds of the game"""

    def __init__(self, bgMusic, endMusic, soundEffect):
        pygame.mixer.pre_init()
        pygame.mixer.init()
        self.bgMusic = bgMusic
        self.endMusic = endMusic
        self.soundEffect = soundEffect

    def playBgMusic(self):
        pygame.mixer.music.load(self.bgMusic)
        pygame.mixer.music.play(-1)


    def playSoundEffort(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.soundEffect))

    def playEndMusic(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.endMusic)
        pygame.mixer.music.play(1)
