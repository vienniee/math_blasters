from posixpath import ismount
from tkinter.constants import E
from pyasn1.codec.ber.decoder import SetDecoder
import pygame, sys
# from pygame.locals import *
#from WorldSelection.subject_chapter_selection import subject_Chapter_selection
from Login.characterSelect import characterSelect
from WorldSelection.levelselect import levelselect
from enum import Enum
from WorldSelection.subject_chapter_selection import subject_Chapter_selection
from minigame.Game import Game
from WorldSelection.Player import Player
from minigame.filter import Questionfilter
from Leaderboard.leaderboard import Leaderboard
from Leaderboard.achievements import Achievements
import os
from DatabaseControllers.QuestionDB import QuestionDB
from DatabaseControllers.QuestDB import QuestDB
from collections import OrderedDict

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

QuestionDB = QuestionDB()
# QuestDB =QuestDB()

teleportCooldownState = False
teleportCooldownTimer = pygame.USEREVENT + 1


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from Login.login import LoginUser
        from Login.RegistrationMenu import Registration
        from mainmenu.studentmenu import studentMenu
        import mainmenu.teacherDashboard as teacherDashboard
        
    else:
        from .Login.login import LoginUser
        from .Login.RegistrationMenu import Registration

# global variable like student gender and name
gender = "male"
studentID = "hDhNkZR4CSct81bQA6oX6drdZHo2"
level = None
STUDENT_DATA = None
subject = 'algebra' #put to none
username = "Alex" #change to username later
completion = None
questions = None
isMinigame= False
#Login()
# Registration = Registration()


def get_quest_qns(quest_quetions_id):
    temp = OrderedDict()
    questions_dict = QuestionDB.get_all_questions()

    for i in quest_quetions_id:
        try:
            temp[i] = questions_dict[i]
        except:
            print("questionid does not exist in question database")

    return temp


class States(Enum):
    login = 1
    register = 2
    character_select = 3
    student_menu = 4
    teacher_menu = 5
    minigame =6
    quest_menu = 7
    world_select = 8
    scorepage = 9
    achievement = 10
    leaderboard = 11
    difficulty_select = 12

state = States.student_menu

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000, 600))
# pygame.display.set_caption("CZ3003 pygame")

while True:
    for event in pygame.event.get():
        if event.type == teleportCooldownTimer:
            teleportCooldownState = False
            pygame.time.set_timer(teleportCooldownTimer, 0)
            print("teleportCooldownState False")    
    print(state)
    if state == States.login:
        result, userID = LoginUser()
        teleportCooldownState = True
        pygame.time.set_timer(teleportCooldownTimer, 3000)
        print("teleportCooldownState True")
        print(result, userID)
        if result == 1:
            state = States.register
        if result == 2:
            state = States.student_menu
            studentID = userID
            print("STUDENT IDDDDDDDDDDDDDDDDDDD", studentID)
        if result == 3:
            state = States.teacher_menu
    elif state == States.register:
        result, studentDict = Registration()
        if result == 1:
            state = States.login
        if result == 2:
            STUDENT_DATA = studentDict
            state = States.character_select
    elif state == States.character_select:
        result = characterSelect(STUDENT_DATA)
        if result == 1:
            state = States.login
    elif state == States.student_menu:
        result = studentMenu()
        if result == 1:
            state = States.world_select
        if result == 2:
            state = States.achievement
        if result == 3:
            state = States.leaderboard
    elif state == States.teacher_menu:
        teacherDashboard.main_menu()
        
    elif state == States.minigame:
        score, completion = Game(gender,username,questions,isMinigame)
        if completion:
            state = States.scorepage
        else:
            state = States.difficulty_select
    elif state == States.quest_menu:
        pass
    elif state == States.world_select:
        result, data = subject_Chapter_selection(gender, studentID)
        if result == 1:
            subject = data
            state = States.difficulty_select

        if result == 0:
            quest_data = data
            questions = get_quest_qns(quest_data["listofQuestionID"])
            state = States.minigame

    elif state == States.leaderboard:
        outcome = Leaderboard()
        if outcome == 1:
            state = States.student_menu
    elif state == States.achievement:
        outcome = Achievements(studentID)
        if outcome == 1:
            state = States.student_menu

    elif state == States.difficulty_select:
        level = levelselect()
        if level == True:
            state = States.world_select
        else:
            isMinigame = True
            questions = QuestionDB.get_questions("algebra", level)
            state = States.minigame

    elif state == States.scorepage:
        isMinigame=False
        pass



# login screen or register


# main menu or teacher Main menu
# minigame = subject_chapter_selection.subject_Chapter_selection("male")
# level = levelselect.levelselect() #'algebra'
# score = Game.Game(minigame,level) #'algebra' #Game(questions,gender,name,quest/minigame*) #quest/minigames doesnt matter if main.py specify the logic
# results.results(minigame,level,score)
# teacherdashboard = teacherDashboard.main_menu()


        
