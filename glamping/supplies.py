import pygame
from pygame.locals import *



class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, itemType, image):
        super(Item, self).__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.itemType = itemType
        # self.loadSound(sound)

    def loadSound(self, sound):
        if sound != None:
            self.sound = pygame.mixer.Sound(sound)
        else:
            self.sound = None

    def playSound(self):
            if self.sound != None:
                self.sound.play()

    def pickUp(self):
            self.playSound()
            return self.itemType