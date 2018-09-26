import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
FPS = 60
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('NO TIME TO GLAMP!')



# CLASSES---------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        # x: starting x coordinate
        # y: starting y coordinate
        # image: image string
        pygame.sprite.Sprite.__init__(self)
        self.load_image(image)
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

    def load_image(self, image):
        self.image = pygame.image.load("images/chi.gif").convert()

    def update(self, movex, movey, items):
        # movex: number of pixels to move on x axis
        # movey: number of pixels to move on y axis
        # items: Sprite Group of items with pickUp method
        self.move_sprite(movex, movey)
        self.items_coll(items)
        self.render()

    def draw(self, Surface):
        # blits Chi to the surface
        # Surface: the surface in which self.image will be blited
        Surface.blit(self.image,(self.rect.x,self.rect.y))

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


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, itemType, image):
        # x: x coordinate
        # y: y coordinate
        # itemType: a dict with one key value pair {"item_name":quantity}
        # image: image string
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("i").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.itemType = itemType

# IMAGES----------------------------------
bg_img = pygame.image.load("images/background.png").convert()
chi_img = ("images/chi.gif")
tent_img = pygame.image.load("images/tent.gif").convert()
logs_img = pygame.image.load("images/logs.gif").convert()
fire_img = pygame.image.load("images/fire.gif").convert()
fish_img = pygame.image.load("images/fish.gif").convert()
player = Player(140, 256, chi_img)

# SPRITE GROUP (items collected) ---------
items = pygame.sprite.Group()
tent = Item(120, 256, itemType, tent_img)
logs = Item(360, 384, itemType, logs_img)
fire = Item(360, 200, itemType, fire_img)
fish = Item(360, 90, itemType, fish_img)
items.add(tent, logs, fire, fish)

# GAME LOOP-------------------------------
def level():
    moveX, moveY = 0,0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        # move Player in direction of arrow by 2 pixels
        if keyinput [pg.K_LEFT]:
            sprite_

        SCREEN.blit(bg_image, (0,0))
        SCREEN.blit(tent_image, (5, 150))
        player.update(moveX, moveY, items)
        player.draw(SCREEN)
        tent.draw(SCREEN)
        items.draw(SCREEN)
        FPSCLOCK.tick(FPS)
        pygame.display.update()

level()