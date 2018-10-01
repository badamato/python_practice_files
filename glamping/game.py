import pygame
from chi import Player
from pygame.locals import *
from supplies import Item

width = 512
height = 480



# COLOR DEFINITIONS ------------------
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# INITIALIZE GAME SQUARE & BACKGROUND MUSIC ----------------
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/Friends.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('NO TIME TO GLAMP!')


# OPENING IMAGES --------------------------------
tentImg = pygame.image.load('images/tent.gif').convert()
background = pygame.image.load('images/background.png').convert()
logsImg = 'images/logs.png'
fireImg = 'images/fire.png'
fishImg = 'images/fish.png'
waterImg = 'images/water.png'

# MAIN PLAYER (chihuahua) & ITEM SPRITES ----------------
all_sprites = pygame.sprite.Group()

player = Player(0, 0, 'images/chi.gif')
player.rect.x = 165
player.rect.y = 190
player_speed = 15
logs = Item(350, 50, {'logs ': 1}, logsImg)
fire = Item(350, 125, {'fire ': 1}, fireImg)
fish = Item(340, 240, {'fish ': 1}, fishImg)
water = Item(350, 325, {'water ': 1}, waterImg)

all_sprites.add(player, logs, fire, fish, water)

# SCORING & COLLECTION ---------------
def items_collected (screen, x, y, count):
    font = pygame.font.Font(None, 36)
    text = font.render("Items Collected: "+ str(count), True, white)
    screen.blit(text,(100, 350))
score = 0

## TIMER ---------------------------
# def count_down (screen, x, y, count):
#     font = pygame.font.Font (None, 36)
#     text = 10, '10'.rjust(3)
#     pygame.time.set_timer(pygame.USEREVENT, 1000)


# MAIN GAME LOOP _________________
running = True
while running:
    for event in pygame.event.get():
        #check for closing window
        if event.type == QUIT:
            running = False
            raise SystemExit
        #check for escape key click
        if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                raise SystemExit

    #move player around if arrow key pressed
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        player.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        player.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        player.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        player.rect.move_ip(5, 0)

    #Keep player on the screen
    if player.rect.left < 0:
        player.rect.left = 0
    elif player.rect.right > 512:
        player.rect.right = 512
    if player.rect.top <= 0:
        player.rect.top = 0
    elif player.rect.bottom >= 480:
        player.rect.bottom = 480

    # UPDATE ------------------
    all_sprites.update()
    

    # DRAWING / RENDERING ON SCREEN -----------------------
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    screen.blit(tentImg, (width * 0.03, height * 0.35))
    all_sprites.draw(screen)
    items_collected(screen, 20, 20, score) 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()