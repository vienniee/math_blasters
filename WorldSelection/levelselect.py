import pygame
import pygame.freetype
import os
import random
from pygame.locals import *

pygame.init()

#create display window
SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #getting mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('clicked')
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

def levelselect():
    #load background image
    # background_surface = pygame.image.load('image\levelselect.png').convert()
    background_surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'difficultyselect', 'levelselect.png')).convert()
    #load button images
    # lvl1_img = pygame.image.load("image\Castle_level_1.png").convert_alpha()
    # lvl2_img = pygame.image.load("image\Castle_level_2.png").convert_alpha()
    # lvl3_img = pygame.image.load("image\Castle_level_3.png").convert_alpha()
    # back_img = pygame.image.load("image/backbutton.png").convert_alpha()
    lvl1_img = pygame.image.load(os.path.join(os.path.dirname(__file__),  'difficultyselect', 'Castle_level_1.png')).convert_alpha()
    lvl2_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'difficultyselect', 'Castle_level_2.png')).convert_alpha()
    lvl3_img = pygame.image.load(os.path.join(os.path.dirname(__file__),  'difficultyselect', 'Castle_level_3.png')).convert_alpha()
    back_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'difficultyselect', 'backbutton.png')).convert_alpha()
    #load fonts
    #font style and size
    font1 = pygame.font.Font(None,18)
    font2 = pygame.font.Font(None,35)
    level1text = font1.render("LEVEL 1", True, [0,0,0])
    level2text = font1.render("LEVEL 2", True,[0,0,0])
    level3text = font1.render("LEVEL 3", True,[0,0,0])

    #create button instances
    level1_button = Button(258,143,lvl1_img,2.5)
    level2_button = Button(408,143,lvl2_img,2.5)
    level3_button = Button(558,143,lvl3_img,2.5)
    back_button = Button(888,542,back_img,0.2)
    #160,310,460

    #game loop
    run = True
    while run:
        screen.fill((202, 228, 241))
        screen.blit(background_surface, (0, 0))
        if back_button.draw():
            return True
        #difficulty select 
        if level1_button.draw() == True:
            print('level 1 selected')
            return 'level 1'
            #import Game
        if level2_button.draw() == True:
            print('level 2 selected')
            return 'level 2'
            #import Game
        if level3_button.draw() == True:
            print('level 3 selected')
            return 'level 3'

        screen.blit(level1text, (315,310))
        screen.blit(level2text, (465,310))
        screen.blit(level3text, (615,310))

    
    

        #event handler
        for event in pygame.event.get():
            #quit game (need to change to back button instead)
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

