
#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data
from enum import Enum
import pygame, sys
from pygame.locals import *


# import subject_chapter_selection
# import levelselect
# import Game
# import login
# import results
# import teacherDashboard
# from .Login.RegistrationMenu import Registration


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from Login.login import LoginUser
        from Login.RegistrationMenu import Registration
        from Login.characterSelect import characterSelect
    else:
        from Login.login import LoginUser
        from Login.RegistrationMenu import Registration
        from Login.characterSelect import characterSelect

# global variable like student gender and name


# Registration = Registration()
class States(Enum):
    login = 1
    register = 2
    character_select = 3
    student_menu = 4
    teacher_menu = 5
    minigame = 6
    quest_menu = 7

state = States.character_select
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("CZ3003 pygame")

while True:
    if state == States.login:
        LoginUser()
    elif state == States.register:
        Registration()
    elif state == States.character_select:
        characterSelect()
    elif state == States.student_menu:
        pass
    elif state == States.teacher_menu:
        pass
    elif state == States.minigame:
        pass
    elif state == States.quest_menu:
        pass

# login screen or register


# main menu or teacher Main menu

minigame = subject_chapter_selection.subject_Chapter_selection("male")
level = levelselect.levelselect() #'algebra'
score = Game.Game(minigame,level) #'algebra' #Game(questions,gender,name,quest/minigame*) #quest/minigames doesnt matter if main.py specify the logic
results.results(minigame,level,score)
teacherdashboard = teacherDashboard.main_menu()


        
