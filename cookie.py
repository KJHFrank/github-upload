import pygame
import settings as s
import random

class Cookie(pygame.sprite.Sprite):
    def __init__(self):
        super(Cookie, self).__init__()
        self.image = pygame.image.load('images/cookies.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, s.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.vel_x = 0
        self.vel_y = random.randrange(3, 5)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
