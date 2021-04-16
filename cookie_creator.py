import pygame
from cookie import Cookie
import settings as s
import random

class CookieCreator:
    def __init__(self):
        self.cookie_batch = pygame.sprite.Group()
        self.bake_timer = random.randrange(180, 240)
        self.cookies_allowed = 5
    
    def update(self):
        self.cookie_batch.update()
        for cookie in self.cookie_batch:
            if cookie.rect.y >= s.DISPLAY_HEIGHT:
                self.cookie_batch.remove(cookie)
        if self.bake_timer == 0:
            self.create_cookie()
            self.bake_timer = random.randrange(180, 240)
        else:
            self.bake_timer -= 1

    def create_cookie(self):
        new_cookie = Cookie()
        self.cookie_batch.add(new_cookie)

    def clear_cookies(self):
        for cookie in self.cookie_batch:
            cookie.kill()