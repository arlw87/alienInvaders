#main
#Authour Andrew White
#Started on Saturday 13th July

#import some libraries
import pygame
from settings import Settings
from rocket import Rocket
from aliens import Alien
import game_functions as funcs
from pygame.sprite import Group
from GameStats import GameStats
from button import Button
from scoreboard import Scoreboard
from gameSounds import gameSounds

#set some parmeters of the game
bgColor = (230,120,230)

def run_game():
    #initialise and create the screen object
    pygame.init()
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_heigh))
    pygame.display.set_caption("Invaders Must Die")

    #play some music
    print(gs.musicName)
    print(gs.musicPath)
    #pygame.mixer.init
    #pygame.mixer.music.load(gs.musicPath)
    #pygame.mixer.music.play(-1)

    #Create sounds object
    sounds = gameSounds(gs.musicPath, gs.endGameMusic, gs.laserSoundsPath)
    #sounds.playBgMusic()

    #Create the Rocket
    rocket = Rocket(screen, gs)

    #group for the bullets
    bullets = Group()

    #Create an ALien
    alien = Alien(screen, gs)

    #create a group for the aliens
    aliens = Group()

    #create fleet
    funcs.create_fleet(aliens, gs, screen, rocket)

    #set up game stats
    stats = GameStats(gs)

    #create play button
    play_button = Button(gs, screen, "Play Game", gs.green_button)

    #create play button
    game_over = Button(gs, screen, "Game Over", gs.red_button)

    #Create a Scoreboard
    SB = Scoreboard(gs, screen, stats)

    #start the main loop of the program
    while True:
        funcs.check_events(rocket, screen, bullets, gs, play_button, stats, SB, aliens, screen, sounds)
        if stats.game_active == True:
            rocket.update_position()

            #check if the bullets have gone off the screen
            funcs.update_bullets(bullets, aliens, screen, rocket, gs, stats, SB)

            #print(len(bullets))
            funcs.update_aliens(aliens, gs, rocket, bullets, screen, stats, SB, sounds)

        funcs.update_screen(screen, rocket, gs, bullets, aliens, play_button, stats, game_over, SB)

run_game()
