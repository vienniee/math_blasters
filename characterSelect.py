
import pygame, sys,pygame_textinput
from pygame.locals import *
from DatabaseControllers.StudentDB import StudentDB

import assets as assets
import studentmenu
import os

mainClock = pygame.time.Clock()
pygame.init()

SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


TEXT_CHARACTER_SELECTED = "Character Select"
TEXT_Male_SELECTED = "Male Selected"
TEXT_Female_SELECTED = "Female Selected"
TEXT_NO_OPTION_SELECTED = "Invalid Selection"
TEXT_ERROR = 'FB Access Failed'




def characterSelect(STUDENT_DATA):
    UUID = os.environ['USER']
    print(UUID,STUDENT_DATA)
    CHAR_SELECT=None
    running = True
    click = False
    background_surface = pygame.image.load("Image/characterSelect/background.png").convert()
    femaleImage = pygame.image.load("Image/characterSelect/female.png").convert_alpha()
    maleImage = pygame.image.load("Image/characterSelect/male.png").convert_alpha()
    confirmImage = pygame.image.load("Image/characterSelect/img2.png").convert_alpha()

    TEXT_OPTION=TEXT_CHARACTER_SELECTED

    while running:
        screen.blit(background_surface, (0, 0))
        btn_male = assets.Button(screen=screen,id='Male',image=maleImage,scale=1,x=360,y=212)
        btn_female = assets.Button(screen=screen,id='Female',image=femaleImage,scale=1,x=520,y=212)
        btn_confirm = assets.Button(screen=screen,id='confirm',image=confirmImage,scale=1,x=460,y=338)

        
        assets.create_text(screen,TEXT_OPTION,assets.SMALL_FONT,assets.COLOR_BLACK,430,185)

        for event in pygame.event.get():
            if btn_male.draw():
                TEXT_OPTION = TEXT_Male_SELECTED 
                CHAR_SELECT = "Male"
                
                
            
            if btn_female.draw():
                TEXT_OPTION = TEXT_Female_SELECTED 
                CHAR_SELECT = "Female"
                
            
            if(btn_confirm.draw()):
                if(CHAR_SELECT == None):
                    TEXT_OPTION = TEXT_NO_OPTION_SELECTED 
                else:
                    try:
                        STUDENT_DATA['character'] = CHAR_SELECT
                        StudentDB.add_student(UUID,STUDENT_DATA)
                        studentmenu.studentMenu()
                    except Exception as e:
                        print(e)
                        TEXT_OPTION = TEXT_ERROR 
                


        pygame.display.update()
        mainClock.tick(60)

if __name__ == "__main__":
    characterSelect()

