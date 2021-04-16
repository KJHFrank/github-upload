import sys
import pygame
from monster import Monster
import settings as s
from cookie_creator import CookieCreator
from rock_spawner import RockSpawner
from alert_box import AlertBox

# Font Initialization
pygame.font.init()

# Display Setup
screen = pygame.display.set_mode(s.DISPLAY_SIZE)
pygame.display.set_caption("Cookie Monster")
fps = 60
clock = pygame.time.Clock()

# Object Setup
monster = Monster()
monster_group = pygame.sprite.Group()
monster_group.add(monster)

cookie_creator = CookieCreator()
rock_spawner = RockSpawner()
alert_box_group = pygame.sprite.Group()


active = True
player_is_alive = True
while active:
    # Tick the Clock
    clock.tick(fps)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                monster.vel_x = -monster.speed
            elif event.key == pygame.K_RIGHT:
                monster.vel_x = monster.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                monster.vel_x = 0
            elif event.key == pygame.K_RIGHT:
                monster.vel_x = 0

    # Update all the objects (memory states)  
    monster.update()  
    cookie_creator.update()
    rock_spawner.update()
    alert_box_group.update()

    # Check for points
    eaten = pygame.sprite.groupcollide(monster_group, cookie_creator.cookie_batch, False, True)
    for monster, cookie in eaten.items():
        monster.status_bar.score.update_score(1)

    # Check for game over
    collided = pygame.sprite.groupcollide(monster_group, rock_spawner.rocks, True, False)
    if collided:
        alert_box = AlertBox()
        alert_box_group.add(alert_box)
        cookie_creator.clear_cookies()
        rock_spawner.clear_rocks()
        player_is_alive = False

    # Render the screen
    screen.fill(s.BG_COLOR)
    monster_group.draw(screen)
    if player_is_alive:
        cookie_creator.cookie_batch.draw(screen)
        rock_spawner.rocks.draw(screen)
    monster.status_bar_group.draw(screen)
    monster.status_bar.score_group.draw(screen)
    alert_box_group.draw(screen)
    pygame.display.update()