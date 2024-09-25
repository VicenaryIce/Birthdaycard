import pygame, sys
from pygame.locals import QUIT
import time

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Happy Birthday!')
cake = pygame.image.load('cake.jpg')#Load image
bcake = pygame.transform.scale(cake, (600,600))
baloons = pygame.image.load('baloons.jpg')
present = pygame.image.load('present.jpg')
bbaloons = pygame.transform.scale(baloons,(600,600))
bpresent = pygame.transform.scale(present,(600,600))
font = pygame.font.SysFont('Times New Roman',50)
happybirthday = font.render('Happy Birthday!',False,'black')
lotsoflove = font.render('Lots of Love!',False,'black')
goodday = font.render('Have a wonderful day!',False,'black')
while True:
    screen.blit(bcake,(0,0))
    screen.blit(happybirthday,(10,0))

    pygame.display.update()
    time.sleep(2)
    screen.blit(bbaloons,(0,0))
    screen.blit(lotsoflove,(170,270))

    pygame.display.update()
    time.sleep(2)
    screen.blit(bpresent,(0,0))
    screen.blit(goodday,(10,0))
    pygame.display.update()
    time.sleep(2)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()