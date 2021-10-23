
#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data
import pygame, sys
from pygame.locals import *
import subject_chapter_selection
import levelselect
import Game
import login
import results
import teacherDashboard
from RegistrationMenu import Registration
# global variable like student gender and name

login = login()
Registration = Registration()
# login screen or register

# main menu or teacher Main menu

minigame = subject_chapter_selection.subject_Chapter_selection("male")
level = levelselect.levelselect() #'algebra'
score = Game.Game(minigame,level) #'algebra'
results.results(minigame,level,score)
teacherdashboard = teacherDashboard.main_menu()
        