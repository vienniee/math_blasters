
#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data
# import pygame, sys
# from pygame.locals import *
# import subject_chapter_selection
# import levelselect
# import Game
# import login
# import results
# import teacherDashboard
# from RegistrationMenu import Registration

# from .Login.login import Login
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from Login.login import Login
    else:
        from .Login.login import Login

# global variable like student gender and name

Login()
# Registration = Registration()
class States(Enum):
    login_or_registration = 1
    student_menu = 2
    teacher_menu = 3
    minigame =4
    quest_menu = 5

state = States.login_or_registration

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("CZ3003 pygame")

while True:
    if state == States.login_or_registration:
        pass
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


        
