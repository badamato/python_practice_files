# pygame template - skeleton for a new pygame project

import pygame
import random

WIDTH = 480
HEIGHT = 512
FPS = 30

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# game loop
running = True
while running:
    #keep running at the right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window - X in window
        if event.type == pygame.QUIT:
            running = False

    #Update


    #Draw/Render
    screen.fill((BLACK))
    #AFTER drawing everything, flip the display
    pygame.display.flip()


pygame.quit()