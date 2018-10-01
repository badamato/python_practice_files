import pygame
from chi import Player
from pygame.locals import *
from supplies import Item




width = 512
height = 480

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/Friends.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('NO TIME TO GLAMP!')


##opening images
tentImg = pygame.image.load('images/tent.gif').convert()
background = pygame.image.load('images/background.png').convert()
logsImg = 'images/logs.png'
fireImg = 'images/fire.png'
fishImg = 'images/fish.png'
waterImg = 'images/water.png'

##MAIN PLAYER (chihuahua)
player = Player(0, 0, 'images/chi.gif')
player.rect.x = 165
player.rect.y = 190
player_list = pygame.sprite.Group()
player_list.add(player)
player_speed = 15

##ITEMS TO COLLECT
items = pygame.sprite.Group()
logs = Item(350, 50, {'logs ': 1}, logsImg)
fire = Item(350, 125, {'fire ': 1}, fireImg)
fish = Item(340, 240, {'fish ': 1}, fishImg)
water = Item(350, 325, {'water ': 1}, waterImg)
items.add(logs, fire, fish, water)



##collected items score
def items_collected (screen, x, y, count):
    font = pygame.font.Font(None, 36)
    text = font.render("Items Collected: "+ str(count), True, white)
    screen.blit(text,(100, 350))
score = 0

##timer coundown
# def count_down (screen, x, y, count):
#     font = pygame.font.Font (None, 36)
#     text = 10, '10'.rjust(3)
#     pygame.time.set_timer(pygame.USEREVENT, 1000)



##game initialization
running = True
##hides the mouse cursor
pygame.mouse.set_visible(0)

##main game loop
while running:
    for event in pygame.event.get():
        #press escape key to quit game
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                raise SystemExit
            elif event.type == QUIT:
                running = False
                raise SystemExit

    #key has been pressed
    pressed_keys = pygame.key.get_pressed()

    # player.update(pressed_keys)
    player.update(pressed_keys)


    ##game display
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    screen.blit(tentImg, (width * 0.03, height * 0.35))
    player_list.draw(screen)
    items.draw(screen)
    items_collected(screen, 20, 20, score) 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()