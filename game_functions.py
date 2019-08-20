import pygame
import sys
from bullet import Bullet
from aliens import Alien
import time


def update_aliens(aliens, settings, rocket, bullets, screen, stats, scoreboard):
    #if any alien in the fleet is at the edges then update the Direction
    check_fleet(aliens, settings)
    #check for collisions with the rocket
    check_end_of_game(aliens, bullets, screen, rocket, settings, stats, scoreboard)
    aliens.update()

def check_end_of_game(aliens, bullets, screen, rocket, settings, stats, scoreboard):
    if check_rocket_alien_collison(aliens, rocket) or check_alien_position(aliens, settings):
        ship_hit(aliens, bullets, screen, rocket, stats, settings, scoreboard)


def ship_hit(aliens, bullets, screen, rocket, stats, settings, scoreboard):
    #reser the game
    aliens.empty()
    bullets.empty()
    screen_rect = screen.get_rect()
    rocket.rect.centerx = screen_rect.centerx
    stats.ships_left -= 1
    time.sleep(1)
    if stats.ships_left == 0:
        check_high_score(stats, scoreboard)
        game_over(stats, settings, scoreboard)
    else:
        #draw new fleet
        create_fleet(aliens, settings, screen, rocket)


def check_high_score(stats, scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
    #print("High Score: ", stats.high_score)

def game_over(stats, settings, scoreboard):
    print("End of game")
    stats.game_active = False
    stats.game_over = True
    #reset the ship limits
    #stats.reset_stats()
    #reset socrevoard levelpygame.mixer.music.load('foo.mp3')
    #print(stats.level)
    #scoreboard.prep_level()
    pygame.mouse.set_visible(True)
    #speed settings back to the default to start at level one
    settings.resest_dynamic_settings()

def check_rocket_alien_collison(aliens, rocket):
    if pygame.sprite.spritecollideany(rocket, aliens):
        print("rocket Hit")
        return True
    else:
        return False

def check_alien_position(aliens, settings):
    check = False
    for alien in aliens.sprites():
        if alien.rect.bottom >= settings.screen_heigh:
            check = True
            print("End of the Line")
            break
        else:
            check = False
    return check

def check_fleet(aliens, settings):
    for alien in aliens.sprites():
        if alien.check_edge():
            fleet_direction_change(aliens, settings)
            break

def fleet_direction_change(aliens, settings):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction = settings.fleet_direction * -1


def update_bullets(bullets, aliens, screen, rocket, settings, stats, scoreboard):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
    check_for_collisions(bullets, aliens, stats, settings, scoreboard)
    check_if_no_aliens(aliens, settings, screen, rocket, bullets, stats, scoreboard)

def check_for_collisions(bullets, aliens, stats, settings, scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    stats.score = stats.score + (len(collisions) * settings.alien_points)
    scoreboard.prep_score()

    #print(len(bullets))
def check_if_no_aliens(aliens, settings, screen, rocket, bullets, stats, scoreboard):
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(aliens, settings, screen, rocket)
        #print("No Aliens")
        #update the settings for the next level
        settings.increase_speed()
        stats.level += 1
        #increase level on Scoreboard
        scoreboard.prep_level()
        #print("Level: ", stats.level)

def number_of_rows(rocket, settings, screen):
    #get the height of the aliens
    alien = Alien(screen, settings)
    alien_height = alien.alien_height
    available_height = settings.screen_heigh - rocket.rocket_height - alien_height
    rows = int(available_height / (2 * alien_height))
    #create abit more empty space
    rows = rows - 1
    return rows


def create_fleet(aliens, settings, screen, rocket):
    number_of_aliens = get_number_aliens(settings, screen)
    num_of_rows = number_of_rows(rocket, settings, screen)
    for row in range(num_of_rows):
        for num in range(number_of_aliens):
        #add an offset to not cross scoreboard
            offset_y = 30
            create_alien(aliens, screen, settings, num, row, offset_y)


def create_alien(aliens, screen, settings, num, row, offset_y):
    #create alien
    new_alien = Alien(screen, settings)
    #modify its position
    #Its X position
    new_alien.x = (new_alien.alien_width + (2 * num * new_alien.alien_width))
    new_alien.rect.x = new_alien.x
    #Its Y position
    new_alien.y = (new_alien.alien_height + (2 * row * new_alien.alien_height))
    new_alien.rect.y = new_alien.y + offset_y
    aliens.add(new_alien)


def get_number_aliens(settings, screen):
    #create an alien
    alien = Alien(screen, settings)
    #print(settings.screen_width)
    #print(type(settings))
    alien_width = alien.alien_width
    screen_width = settings.screen_width
    #determine the number of aliens per row
    num_per_row = int(screen_width / ( 2 * alien_width))
    to_loop = num_per_row - 1
    return to_loop

def check_events(rocket, window, bullets, settings, button, stats, scoreboard, aliens, screen, sounds):
    #get windows rect
    window_rect = window.get_rect()

    #wait for an escape event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Escaping the Game")
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(rocket, event, bullets, settings, window, sounds)

        elif event.type == pygame.KEYUP:
            check_keyup_event(rocket, event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()
            check_button_press(stats, button, x_mouse_pos, y_mouse_pos, scoreboard, aliens, bullets, settings, screen, rocket)

def check_button_press(stats, button, x, y, scoreboard, aliens, bullets, settings, screen, rocket):
    if x > button.rect.left and x < button.rect.right:
        if y > button.rect.top and y < button.rect.bottom:
            stats.game_active = True
            #make mouse pointer invisible
            pygame.mouse.set_visible(False)
            setup_new_game(stats, scoreboard, aliens, bullets, settings, screen, rocket)

def setup_new_game(stats, scoreboard, aliens, bullets, settings, screen, rocket):
    #reset the stats
    stats.reset_stats()
    #reset scoreboard
    scoreboard.prep_score()
    scoreboard.prep_high_score()
    scoreboard.prep_level()
    #clear aliens and bullets
    aliens.empty()
    bullets.empty()
    #create a fleet
    create_fleet(aliens, settings, screen, rocket)



def update_screen(screen, object, settings, bullets, aliens, start_button, stats, game_over_msg, scoreboard):

        #Make the most recently drawn screen visible
        if stats.game_over == True:
            flash_button(stats, settings, game_over_msg, screen)
        elif stats.game_active == False:
            screen.fill(settings.bg_color)
            start_button.draw_button()
        else:
            #Redraw the screen
            screen.fill(settings.bg_color)
            object.blitme()
            #draw fleet
            for alien in aliens.sprites():
                #print("Alien Pos: ", alien.x)
                alien.blitme()

            #display the bullets
            #sprites function gives a list of all the bullet objects
            for bullet in bullets.sprites():
                bullet.draw_bullet()
            #display the scoreboard
            scoreboard.show_score()
        pygame.display.flip()

def flash_button(stats, settings, msg, screen):
    num = 0
    display = True
    while num < 9:
        #print (num)
        time.sleep(0.4)
        display = not display
        screen.fill(settings.bg_color)
        if display == True:
            msg.draw_button()
        pygame.display.flip()
        num += 1
    stats.game_over = False


def check_keydown_event(rocket, event, bullets, settings, window, sounds):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
        #print("right down")
    elif event.key == pygame.K_LEFT:
        #print("left down")
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        #crate a new bullet
        fire_bullet(bullets, settings, window, rocket, sounds)


def check_keyup_event(rocket, event):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
        #print("right up")
    elif event.key == pygame.K_LEFT:
        #print("left up")
        rocket.moving_left = False


def fire_bullet(bullets, settings, window, rocket, sounds):
    if len(bullets) < settings.bullets_allowed:
        sounds.playSoundEffort()
        new_bullet = Bullet(settings, window, rocket)
        bullets.add(new_bullet)
