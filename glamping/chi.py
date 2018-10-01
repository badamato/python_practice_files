import pygame
from pygame.locals import *



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/chi.gif").convert()
        self.rect = self.image.get_rect()
        # self.inventory = {}

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 512:
            self.rect.right = 512
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 480:
            self.rect.bottom = 480
