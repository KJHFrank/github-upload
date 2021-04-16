import pygame
import settings as s
from status_bar import StatusBar

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super(Monster, self).__init__()
        self.image = pygame.image.load('images/monster.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.x = s.DISPLAY_WIDTH // 2
        self.rect.y = s.DISPLAY_HEIGHT - self.rect.height * 1.5
        self.status_bar = StatusBar()
        self.status_bar_group = pygame.sprite.Group()
        self.status_bar_group.add(self.status_bar)      
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 2

    def update(self):
        self.status_bar_group.update()
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= s.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = s.DISPLAY_WIDTH - self.rect.width
    
