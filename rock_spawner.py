import pygame
from rock import Rock
import settings as s
import random

class RockSpawner:
    def __init__(self):
        self.rocks = pygame.sprite.Group()
        self.spawn_timer = random.randrange(120, 180)
    
    def update(self):
        self.rocks.update()
        for rock in self.rocks:
            if rock.rect.y >= s.DISPLAY_HEIGHT:
                self.rocks.remove(rock)
        if self.spawn_timer == 0:
            self.spawn_rock()
            self.spawn_timer = random.randrange(120, 180)
        else:
            self.spawn_timer -= 1

    def spawn_rock(self):
        new_rock = Rock()
        self.rocks.add(new_rock)

    def clear_rocks(self):
        for rock in self.rocks:
            rock.kill()