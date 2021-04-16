import pygame
import settings as s
from score import Score

class StatusBar(pygame.sprite.Sprite):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.image = pygame.image.load('images/status_bar_bg.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (s.DISPLAY_WIDTH, self.image.get_height() // 10))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (s.DISPLAY_WIDTH // 2, s.DISPLAY_HEIGHT)
        
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)

    def update(self):
        self.score_group.update()