import pygame, sys,importlib
import pygame_textinput
import firebase as FB
importlib.reload(sys.modules['firebase'])
from pygame.locals import *

import assets as assets

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

h = 500    
w = 800

screen = pygame.display.set_mode((w,h))


TEXT_CHARACTER_SELECTED = "Character Select"
TEXT_DEMON_SELECTED = "Demon Selected"
TEXT_WARRIOR_SELECTED = "Warrior Selected"
TEXT_NO_OPTION_SELECTED = "Invalid Selection"

TEMP_STUDENT_DATA = {"name":"student 1","age":15}
TEMP_STUDENT_ID = "MATH-BLASTER-USR"

def characterSelect(pageNum):
    CHAR_SELECT=None
    running = True
    click = False
    background_surface = pygame.image.load("Image/characterSelect/background.png").convert()
    demonImage = pygame.image.load("Image/characterSelect/img0.png").convert_alpha()
    warriorImage = pygame.image.load("Image/characterSelect/img1.png").convert_alpha()
    confirmImage = pygame.image.load("Image/characterSelect/img2.png").convert_alpha()

    firebaseDatabase = FB.FirebaseDatabase()

    TEXT_OPTION=TEXT_CHARACTER_SELECTED

    while running:
        screen.blit(background_surface, (0, 0))
        btn_warrior = assets.Button(screen=screen,id='warrior',image=warriorImage,scale=1,x=423,y=216)
        btn_demon = assets.Button(screen=screen,id='demon',image=demonImage,scale=1,x=297,y=216)
        btn_confirm = assets.Button(screen=screen,id='confirm',image=confirmImage,scale=1,x=358,y=331)

        
        assets.create_text(screen,TEXT_OPTION,assets.SMALL_FONT,assets.COLOR_BLACK,330,185)

        for event in pygame.event.get():
            if btn_warrior.draw():
                TEXT_OPTION = TEXT_WARRIOR_SELECTED 
                CHAR_SELECT = "Warrior"
                import studentmenu
                
            
            if btn_demon.draw():
                TEXT_OPTION = TEXT_DEMON_SELECTED 
                CHAR_SELECT = "Demon"
                import studentmenu
            
            if(btn_confirm.draw()):
                if(CHAR_SELECT == None):
                    TEXT_OPTION = TEXT_NO_OPTION_SELECTED 
                else:
                    TEMP_STUDENT_DATA['character'] = CHAR_SELECT
                    firebaseDatabase.setStudentData(TEMP_STUDENT_ID,TEMP_STUDENT_DATA)
                    print(firebaseDatabase.getStudentData(TEMP_STUDENT_ID))
                    
                    #NEXT SCREEN HERE

        

        pygame.display.update()
        mainClock.tick(60)


characterSelect(1)

