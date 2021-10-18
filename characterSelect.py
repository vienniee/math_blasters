import pygame, sys,pygame_textinput
from pygame.locals import *
from DatabaseControllers.StudentDB import StudentDB

import assets as assets
import studentmenu


mainClock = pygame.time.Clock()
pygame.init()

SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


TEXT_CHARACTER_SELECTED = "Character Select"
TEXT_DEMON_SELECTED = "Demon Selected"
TEXT_WARRIOR_SELECTED = "Warrior Selected"
TEXT_NO_OPTION_SELECTED = "Invalid Selection"
TEXT_ERROR = 'FB Access Failed'

TEMP_STUDENT_DATA = {"name":"TEST_USER1","email":"TEST_USER@gmail.com","class":"Mathematics"}


def characterSelect(pageNum):
    CHAR_SELECT=None
    running = True
    click = False
    background_surface = pygame.image.load("Image/characterSelect/background.png").convert()
    demonImage = pygame.image.load("Image/characterSelect/img0.png").convert_alpha()
    warriorImage = pygame.image.load("Image/characterSelect/img1.png").convert_alpha()
    confirmImage = pygame.image.load("Image/characterSelect/img2.png").convert_alpha()

    TEXT_OPTION=TEXT_CHARACTER_SELECTED

    while running:
        screen.blit(background_surface, (0, 0))
        btn_warrior = assets.Button(screen=screen,id='warrior',image=warriorImage,scale=1,x=550,y=212)
        btn_demon = assets.Button(screen=screen,id='demon',image=demonImage,scale=1,x=390,y=218)
        btn_confirm = assets.Button(screen=screen,id='confirm',image=confirmImage,scale=1,x=460,y=331)

        
        assets.create_text(screen,TEXT_OPTION,assets.SMALL_FONT,assets.COLOR_BLACK,430,185)

        for event in pygame.event.get():
            if btn_warrior.draw():
                TEXT_OPTION = TEXT_WARRIOR_SELECTED 
                CHAR_SELECT = "Warrior"
                
                
            
            if btn_demon.draw():
                TEXT_OPTION = TEXT_DEMON_SELECTED 
                CHAR_SELECT = "Demon"
                
            
            if(btn_confirm.draw()):
                if(CHAR_SELECT == None):
                    TEXT_OPTION = TEXT_NO_OPTION_SELECTED 
                else:
                    try:
                        TEMP_STUDENT_DATA['character'] = CHAR_SELECT
                        StudentDB.add_student(TEMP_STUDENT_DATA)
                        studentmenu.studentMenu()
                    except Exception as e:
                        print(e)
                        TEXT_OPTION = TEXT_ERROR 
                

        

        pygame.display.update()
        mainClock.tick(60)


characterSelect(1)

