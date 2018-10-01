import pygame
from pygame.locals import *



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/chi.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 165
        self.rect.y = 190

        # self.inventory = {}

    # def update(self, movex, movey, items):
    #     self.moveSprite(movex, movey)
    #     self.itemsCollision(items)
    #     self.render()

    def itemsCollision(self, items):
        pygame.sprite.spritecollide(self, items, True)
