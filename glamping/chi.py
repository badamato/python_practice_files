import pygame
# from block import Block


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        # x: starting x coordinate
        # y: starting y coordinate
        # image: image string
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/chi.gif").convert()
        self.timeTarget = 7
        self.timeNum = 0
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.left = False
        self.down = False
        self.moving = False
        self.inventory = {}












    def get_inventory(self):
        return self.inventory


    def update(self, movex, movey, items):
        # movex: number of pixels to move on x axis
        # movey: number of pixels to move on y axis
        # items: Sprite Group of items with pickUp method
        self.move_sprite(movex, movey)
        self.items_coll(items)
        self.render()

    def move_sprite(self, movex, movey):
        # moves sprite along x and y axis according to movex and movey
        # movex: number of pixels to move on x axis
        # movey: number of pixels to move on y axis
        oldX = self.rect.x
        oldY = self.rect.y
        self.rect.x +=movex
        self.rect.y +=movey
        self.move_check(oldX, oldY)

    def move_check(self, oldx, oldy):
        # checking for differences between oldx and oldy and self.rect.x and self.rect.y 
        # oldx: the old x to compare current x to 
        # oldy: the old y to compare current y to 
        if self.rect.x == oldx and self.rect.y == oldy:
            self.moving = False
        else:
            self.moving = True
            if self.rect.x > oldx:
                self.left = False
            elif self.rect.x < oldx:
                self.left = True
            if self.rect.y > oldy:
                self.down = True
            elif self.rect.y < oldy:
                self.down = False

    def render(self):
        # sets self.image
        self.image = self.image

    def items_coll(self, items):
        # checks if player collides with items in group
        # items: Sprite Group of items with pickup method
        collisionList = pygame.sprite.spritecollide(self, items, True)
        for collision in collisionList:
            item = collision.pick_up()
            self.update_inventory(item)

    def update_inventory(self, item):
        # adds items to inventory
        # item: a dict of key value pairs that will be added to self.inventory
        for key in item.keys():
            if key in self.inventory:
                self.inventory[key] += [key]
            else:
                self.inventory = dict(self.inventory.items() + item.items())
