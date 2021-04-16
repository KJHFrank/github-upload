import pygame
import settings as s
pygame.font.init()

class AlertBox(pygame.sprite.Sprite):
    def __init__(self):
        super(AlertBox, self).__init__()
        self.screen = pygame.display.set_mode(s.DISPLAY_SIZE)
        self.font = pygame.font.Font(None, 80)
        self.color = (0, 0, 255)
        self.message = "Game Over"
        self.image = self.font.render(self.message, False, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (s.DISPLAY_WIDTH // 2, s.DISPLAY_HEIGHT // 2)
    
    def update(self):
        self.rect.center = (s.DISPLAY_WIDTH // 2, s.DISPLAY_HEIGHT // 2)

import unittest
class TestAlertBox(unittest.TestCase):
    """Tests for the class AlertBox."""

    def test_rect_center(self):
        test_rect_center = AlertBox()
        test_rect_center.update()
        self.assertEqual(test_rect_center.rect.center, (350, 250))
    
if __name__ == '__main__':
    unittest.main()