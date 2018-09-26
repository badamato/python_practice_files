import pygame

width = 512
height = 480

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('NO TIME TO GLAMP!')
clock = pygame.time.Clock()

##images
tentImg = pygame.image.load('images/tent.gif').convert()
background = pygame.image.load('images/background.png').convert()
chi = pygame.image.load('images/chi.gif').convert()


def tent(x, y):
    screen.blit(tentImg, (x, y))

x = (width * 0.03)
y = (height * 0.35)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    tent(x, y)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
