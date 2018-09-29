import pygame
from chi import Player


def display_status(screen, player):
        font = pg.font.Font(None, 36)
        x = 10
        y = 10
        status = player.status_text + "\n" + player.backpack_text
        for line in status.splitlines():
            line_surface = font.render(line, 1, white)
            line_height = line_surface.get_height()
            screen.blit(line_surface, [x, y])
            y += line_height
            

def main():
    width = 512
    height = 480

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/Friends.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('NO TIME TO GLAMP!')
    clock = pygame.time.Clock()

    ##images
    tentImg = pygame.image.load('images/tent.gif').convert()
    background = pygame.image.load('images/background.png').convert()

    def tent(x, y):
        screen.blit(tentImg, (x, y))
    x = (width * 0.03)
    y = (height * 0.35)

    ##game initialization
    done = False
    while not done:
        if player.isDead():
            done = True

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


if '__name__' == '__main__':
    main()
