import pygame
import settings as s

class AlertBox(pygame.sprite.Sprite):
    def __init__(self):
        super(AlertBox, self).__init__()
        self.font = pygame.font.Font(None, 80)
        self.color = (0, 0, 255)
        self.message = "Game Over"
        self.image = self.font.render(self.message, False, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (s.DISPLAY_WIDTH // 2, s.DISPLAY_HEIGHT // 2)
    
    def update(self):
        self.rect.center = (s.DISPLAY_WIDTH // 2, s.DISPLAY_HEIGHT // 2)

