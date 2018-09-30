import pygame
from chi import Player
# from supplies import Supplies




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

##opening character (chihuahua)
player = Player(0, 0, 'images/chi.gif')
player.rect.x = 165
player.rect.y = 190
player_list = pygame.sprite.Group()
player_list.add(player)
player_speed = 15

# items_group = pygame.sprite.Group()
# items_group.add(Items())



##add timer and display

def items_collected (screen, x, y, count):
    font = pygame.font.Font(None, 36)
    text = font.render("Items Collected: "+str(count), True, white)
    screen.blit(text,(120, 350))







##game initialization - MAIN PROGRAM LOOP
done = False

##set player score base
score = 0

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 300
y_coord = 1


##hides the mouse cursor
pygame.mouse.set_visible(0)


while not done:
    ##event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -player_speed
            elif event.key == pygame.K_RIGHT:
                x_speed = player_speed
            elif event.key == pygame.K_UP:
                y_speed = -player_speed
            elif event.key == pygame.K_DOWN:
                y_speed = player_speed

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0




    ##game display
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    screen.blit(tentImg, (width * 0.03, height * 0.35))
    player_list.draw(screen)
    items_collected(screen, 20, 20, score) 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()