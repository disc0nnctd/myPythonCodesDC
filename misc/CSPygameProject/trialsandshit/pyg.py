import pygame

import random
#Colors
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

rect = pygame.rect.Rect(0, 100, 50, 50)


FPS=30
width=800
height=600


 
pygame.init()

gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("Road")
pygame.display.update()

class Player(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image.fill(green)
            self.rect = self.image.get_rect()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
print all_sprites
def speedb(x):
    return x * 3
gameExit=False

x_coord=width/2
y_coord=height-10
x_speed=0
y_speed=0

block_size= 10

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                x_speed = -3

            elif event.key == pygame.K_RIGHT:

                x_speed = 3

            elif event.key == pygame.K_UP:

                y_speed = -3

            elif event.key == pygame.K_DOWN:

                y_speed = 3

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:

                x_speed = 0

            elif event.key == pygame.K_RIGHT:

                x_speed = 0

            elif event.key == pygame.K_UP:

                y_speed = 0

            elif event.key == pygame.K_DOWN:

                y_speed = 0

    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed


    move = (1,0)
    rect.move_ip(map(speedb,move))

#    gameDisplay.fill(black)
#    pygame.draw.rect(gameDisplay, blue, [x_coord,y_coord,block_size,block_size])
#    pygame.draw.rect(gameDisplay, white, rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
