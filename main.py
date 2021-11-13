
from posixpath import ismount
from tkinter.constants import E, NONE
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
from DatabaseControllers.ScoresDB import ScoreDB
from collections import OrderedDict
from minigame.results import results
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Login.login import LoginUser
from Login.RegistrationMenu import Registration
from mainmenu.studentmenu import studentMenu
import mainmenu.teacherDashboard as teacherDashboard



# path_parent = os.path.dirname(os.getcwd())
# os.chdir(path_parent)

QuestionDB = QuestionDB()
ScoreDB = ScoreDB()
QuestDB =QuestDB()

teleportCooldownState = False
teleportCooldownTimer = pygame.USEREVENT + 1



# global variable like student gender and name
gender = None
studentID = None
level = None
STUDENT_DATA = None
subject = None #put to none 
username = None #change to username later
completion = None
questions = None
isMinigame= False
isQuest = False
questID=None
passingmark=None
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
    world_select = 7
    scorepage = 8
    achievement = 9
    leaderboard = 10
    difficulty_select = 11

state = States.login

while True:
    for event in pygame.event.get():
        if event.type == teleportCooldownTimer:
            teleportCooldownState = False
            pygame.time.set_timer(teleportCooldownTimer, 0)
            print("teleportCooldownState False")    

    print(state)
    if state == States.login:
        result, userID, gender_logined = LoginUser()
        if gender_logined != None:
            gender = gender_logined.lower()
            print("Gender: "+ gender)
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
        if result == 4:
            state = States.login
    elif state == States.teacher_menu:
        result = teacherDashboard.main_menu()
        if result == 1:
            state = States.login
        
    elif state == States.minigame:
        score, completion, passing_mark = Game(
            gender, username, questions, isMinigame)
        passingmark = passing_mark
        if completion:
            if isMinigame:
                # update scores for minigame
                ScoreDB.add_or_update_score(studentID,subject,level,score)
                
            if isQuest:
                print("update scores!!!")
                # update scores for quest
                print(score)
                QuestDB.update_quest_score(questID,studentID,score)
            state = States.scorepage
        else:
            # abandon
            state = States.difficulty_select
    elif state == States.world_select:
        print(gender)
        result, data = subject_Chapter_selection(gender, studentID)
        if result == 1:
            subject = data.lower()
            state = States.difficulty_select

        if result == 0:
            isQuest = True
            quest_data = data
            questID = quest_data["questID"]
            questions = get_quest_qns(quest_data["listofQuestionID"])
            state = States.minigame
        
        if result == 4:
            state = States.student_menu

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
            questions = QuestionDB.get_questions(subject, level)
            state = States.minigame

    elif state == States.scorepage:
        isMinigame=False
        cont = results(studentID,subject,level,score,passingmark)
        if cont:
            state=States.world_select
        
