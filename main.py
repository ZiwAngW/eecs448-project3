import pygame

import sys
import os
from player import Player
from obstacle import ObstacleM
from buttom import buttom

worldx =960
worldy =720
fps = 60



pygame.init()
clock = pygame.time.Clock()
#images
back ='image/backbord.jpg'
shark = 'image/icon.png'
intro_backg ='image/WechatIMG14.png'
intro_backg2='image/introb.jpeg'
#screen set up
screen = pygame.display.set_mode((worldx,worldy))
#background set up



#title 
pygame.display.set_caption("Shark")
icon=pygame.image.load('fishincon.png')
pygame.display.set_icon(icon)


#loding 
def pre_intro(width,height):
    fade=pygame.Surface((width,height))
    fade.fill((255,255,255))
    for i in range(0,300):
        fade.set_alpha(i)
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(10)

#game intro

def game_intro():

    intro=True
    buttom1=buttom(430,225,100,50,(255,255,255),'Start')
    buttom2=buttom(430,355,100,50,(255,255,255),'Quit')
    
    intro_scp=pygame.image.load(intro_backg2).convert()
    x=0
    while intro:
        
        for event in pygame.event.get():
            position=pygame.mouse.get_pos()
            #click=pygame.mouse.get_pressed()
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.MOUSEMOTION:
                if buttom1.ontop(position):
                    buttom1.color=(255,255,0)
                else:
                    buttom1.color=(255,255,255)
                
                if buttom2.ontop(position):
                    buttom2.color=(255,255,0)
                else:
                    buttom2.color=(255,255,255)
            if event.type ==pygame.MOUSEBUTTONDOWN and buttom1.ontop(position):
                intro=False
            if event.type ==pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.quit()
                sys.exit()
                
        
        rel_x=x % intro_scp.get_rect().height
        screen.blit(intro_scp,(0,rel_x - intro_scp.get_rect().height))
        if rel_x<worldy:
            screen.blit(intro_scp,(0,rel_x))
        x-=1
        
        clock.tick(fps)
        
        buttom1.draw(screen)
        buttom2.draw(screen)
        pygame.display.update()

   
#game loop


def game_loop():
    background = pygame.image.load(back).convert()
    background = pygame.transform.scale(background,(worldx,worldy),screen)
    player =Player(background,200,200,shark)
    om = ObstacleM(background)
    mx =0
    my =0
    main=True
    while main:
        
        background = pygame.image.load(back).convert()
        background = pygame.transform.scale(background, (worldx, worldy), screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    mx =-2
                if event.key == ord('w'):
                    my = -2
                if event.key == ord('d'):
                    mx =2
                if event.key == ord('s'):
                    my = 2
            if event.type == pygame.KEYUP:
                if event.key == ord('a'):
                    if mx ==-2:
                        my =0
                if event.key == ord('w'):
                    if my == -2:
                        mx = 0
                if event.key == ord('d'):
                    if mx == 2:
                        my = 0
                if event.key == ord('s'):
                    if my ==2:
                        mx =0
        om.number()
        om.update()
        om.draw()
        
        player.move(mx,my)
        player.draw()
    
        clock.tick(fps)
        
        pygame.display.update()

#pre_intro(worldx,worldy)
game_intro()
game_loop()
pygame.quit()
