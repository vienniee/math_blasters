
#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data
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
# if __name__ == '__main__':
#     if __package__ is None:
#         import sys
#         from os import path
#         sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#         from Login.login import Login
#     else:
#         from .Login.login import Login

# global variable like student gender and name
gender = "male"
level = None
subject = 'algebra' #put to none
username = "Alex" #change to username later
completion = None
#Login()
# Registration = Registration()
class States(Enum):
    login_or_registration = 1
    student_menu = 2
    teacher_menu = 3
    minigame =4
    quest_menu = 5
    world_select = 6
    level_select = 7
    scorepage = 8

state = States.level_select

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000, 600))
# pygame.display.set_caption("CZ3003 pygame")

while True:
    print(state)
    if state == States.login_or_registration:
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


        
