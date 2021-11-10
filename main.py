# import pygame, sys
# from pygame.locals import *
#from WorldSelection.subject_chapter_selection import subject_Chapter_selection
from WorldSelection.levelselect import levelselect
from enum import Enum
from minigame.Game import Game
from minigame.filter import Questionfilter
import os
# import login
# import results
# import teacherDashboard
# from RegistrationMenu import Registration
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)


# from .Login.login import Login
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from Login.login import LoginUser
        from Login.RegistrationMenu import Registration
    else:
        from .Login.login import LoginUser
        from .Login.RegistrationMenu import Registration

# global variable like student gender and name
gender = "male"
level = None
subject = 'algebra' #put to none
username = "Alex" #change to username later
completion = None
#Login()
# Registration = Registration()
class States(Enum):
    login = 1
    register = 2
    character_select = 3
    student_menu = 4
    teacher_menu = 5
    minigame =6
    quest_menu = 7
    world_select = 8
    level_select = 9
    scorepage = 10

state = States.register

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000, 600))
# pygame.display.set_caption("CZ3003 pygame")

while True:
    print(state)
    if state == States.login:
        LoginUser()

    elif state == States.register:
        Registration = Registration()

    elif state == States.character_select:
        pass
    elif state == States.student_menu:
        pass
    elif state == States.teacher_menu:
        pass
    elif state == States.minigame:
        score, completion = Game(gender,username,questions)
        if completion:
            state = States.scorepage
        else:
            state = States.level_select
    elif state == States.quest_menu:
        pass
    elif state == States.level_select:
        level = levelselect()
        questions = Questionfilter(subject,level)
        #level = 'test' #in database data change level to integer 1,2,3
        state = States.minigame

    elif state == States.world_select:
        #subject = subject_Chapter_selection(gender)
        subject = 'algebra'

# login screen or register


# main menu or teacher Main menu
# minigame = subject_chapter_selection.subject_Chapter_selection("male")
# level = levelselect.levelselect() #'algebra'
# score = Game.Game(minigame,level) #'algebra' #Game(questions,gender,name,quest/minigame*) #quest/minigames doesnt matter if main.py specify the logic
# results.results(minigame,level,score)
# teacherdashboard = teacherDashboard.main_menu()


        
