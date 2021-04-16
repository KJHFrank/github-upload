import pygame
from rock import Rock
import settings as s
import random

class RockSpawner:
    def __init__(self):
        self.screen = pygame.display.set_mode(s.DISPLAY_SIZE)
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

import unittest
class TestRockSpawner(unittest.TestCase):
    """Tests for the class CookieCreator."""

    def test_rocks_are_created(self):
        test_rock = RockSpawner()
        test_rock.spawn_rock()
        self.assertTrue(len(test_rock.rocks) != 0)

    def test_rocks_are_cleared(self):
        test_rock = RockSpawner()
        test_rock.spawn_rock()
        test_rock.clear_rocks()
        self.assertTrue(len(test_rock.rocks) == 0)

if __name__ == '__main__':
    unittest.main()