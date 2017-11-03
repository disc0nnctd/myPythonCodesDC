"""This is for my CS class project."""
import pygame
import msvcrt
from datetime import datetime
import random
import time
WHITE=(255, 255, 255)
BLACK=(0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Reaction Time")
font = pygame.font.SysFont('Calibri', 25, True, False)
l=[]
for x in range(5): # repeat 5 times

    screen.fill(BLACK)

    pygame.display.flip()
    o=random.randint(2,4)
    p=0
    while p<>o:
        time.sleep(1) #wait time
        p+=1
        while msvcrt.kbhit():  #This resets the keyboard
            msvcrt.getwch()    #after the time ticking to prevent cheating

    screen.fill(GREEN)

    pygame.display.flip()

    rct_start = datetime.now()

    press = False #key press wait
    while not press:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 rct_end = datetime.now()
                 press = True
    
    rctime=rct_end-rct_start
    s=str(rctime)[5:13]
    l.append(float(s))

#----
scoredisplay=[2,20]
screen.fill(WHITE)
scoretext= "Your reaction times(in seconds) are as follows:"
scoretextd=font.render(scoretext,True,BLUE)

screen.blit(scoretextd,[0,0])
for i in l:
    displayrct=font.render(str(i),True,BLACK)
    screen.blit(displayrct,scoredisplay)
    scoredisplay[1]+=20

avg=sum(l)/len(l)
avgscore=font.render(("Average: %s"%(avg)),True,BLACK)
screen.blit(avgscore,scoredisplay)

txt = font.render("PRESS ANY KEY TO EXIT", 0, RED)
text_rect = txt.get_rect(center=screen.get_rect().center)#move text to center of screen
screen.blit(txt, text_rect)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            pygame.quit()
            exit()
