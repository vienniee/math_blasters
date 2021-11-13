
import pygame, sys,pygame_textinput
from pygame.locals import *

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from DatabaseControllers.StudentDB import StudentDB
from Login import assets
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
    background_surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characterselect_images', 'background.png')).convert()
    femaleImage = pygame.image.load(os.path.join(os.path.dirname(__file__),  'characterselect_images', 'female.png')).convert_alpha()
    maleImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characterselect_images', 'male.png')).convert_alpha()
    confirmImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characterselect_images', 'img2.png')).convert_alpha()

    TEXT_OPTION=TEXT_CHARACTER_SELECTED

    while running:
        screen.blit(background_surface, (0, 0))
        btn_male = assets.Button(screen=screen,id='Male',image=maleImage,scale=1,x=360,y=212)
        btn_female = assets.Button(screen=screen,id='Female',image=femaleImage,scale=1,x=520,y=212)
        btn_confirm = assets.Button(screen=screen,id='confirm',image=confirmImage,scale=1,x=460,y=338)

        
        #assets.create_text(screen,TEXT_OPTION,assets.SMALL_FONT,assets.COLOR_BLACK,430,185)

        for event in pygame.event.get():
            if btn_male.draw():
                TEXT_OPTION = TEXT_Male_SELECTED 
                CHAR_SELECT = "Male"
                
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if btn_female.draw():
                TEXT_OPTION = TEXT_Female_SELECTED 
                CHAR_SELECT = "Female"
                
            
            if(btn_confirm.draw()):
                if(CHAR_SELECT == None):
                    TEXT_OPTION = TEXT_NO_OPTION_SELECTED 
                else:
                    try:
                        STUDENT_DATA['character'] = CHAR_SELECT
                        a = StudentDB()
                        a.add_student(UUID,STUDENT_DATA)
                        # studentmenu.studentMenu()
                        return 1
                    except Exception as e:
                        print(e)
                        TEXT_OPTION = TEXT_ERROR 
                

        if TEXT_OPTION == TEXT_NO_OPTION_SELECTED:
            font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'font', 'Pixeltype.ttf'), 30)
            prompt_text = font.render("Please Select a Character!", False, (255, 0, 0))
            screen.blit(prompt_text, (400,200))
        
        elif TEXT_OPTION == TEXT_Female_SELECTED:
            font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'font', 'Pixeltype.ttf'), 30)
            prompt_text = font.render("Female Character Selected", False, (0, 0, 0))
            screen.blit(prompt_text, (400,200))
            
        elif TEXT_OPTION == TEXT_Male_SELECTED:
            font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'font', 'Pixeltype.ttf'), 30)
            prompt_text = font.render("Male Character Selected", False, (0, 0, 0))
            screen.blit(prompt_text, (400,200))

        pygame.display.update()
        mainClock.tick(60)

if __name__ == "__main__":
    characterSelect()

