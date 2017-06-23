import pygame
from pygame.locals import *
from sys import exit
 
background_image = 'road.png'
sheep = 'sheep.png'

#cars=()
car1= 'Car1.png'
pygame.init()
height=500
width=500
screen = pygame.display.set_mode((height,width))

pygame.display.set_caption("Crossy")
background = pygame.image.load(background_image).convert()
player = pygame.image.load(sheep).convert_alpha()
 
x, y = 240, 400
MOVE_RIGHT = 1
MOVE_LEFT = 2
MOVE_UP=3
MOVE_DOWN=4
direction = 0
while True:
    
    for event in pygame.event.get():
         
        if event.type == QUIT:
            exit()
             
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = MOVE_LEFT
            elif event.key == K_RIGHT:
                direction = MOVE_RIGHT
            if event.key == K_UP:
                direction = MOVE_UP
            elif event.key == K_DOWN:
                direction = MOVE_DOWN
                 
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN :
                direction = 0
         
    if(direction == MOVE_LEFT):
        x-=0.25
    elif(direction == MOVE_RIGHT):
        x+=0.25
    if (direction == MOVE_UP):
        y-=0.25
    elif(direction == MOVE_DOWN):
        y+=0.25
    screen.blit(background, (0, 0))
    screen.blit(player, (x, y))
    pygame.display.update()