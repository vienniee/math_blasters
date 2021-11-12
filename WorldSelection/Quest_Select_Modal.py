import pygame
from DatabaseControllers.QuestDB import QuestDB
import os
import math

from WorldSelection.questText import QuestText 
# if __name__ == '__main__':
#     if __package__ is None:
#         import sys
#         from os import path
#         sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#         from DatabaseControllers.QuestDB import QuestDB
#     else:
#         from ..DatabaseControllers.QuestDB import QuestDB

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self,screen):
        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

class Quest_menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        quest_menu = pygame.image.load(os.path.join(os.path.dirname(__file__),"quest", 'quest_background.png')).convert_alpha()
        self.image = quest_menu
        self.rect = self.image.get_rect(center=(500, 300))

def load_asset(subject,studentID):
    
    questDatabase = QuestDB()
    questData = questDatabase.get_quest_by_subject_studentID(subject,studentID)
    print(questData)
    
    quest_menu = pygame.sprite.GroupSingle()
    quest_menu.add(Quest_menu())

    questButtonImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "quest", 'assignquestselect_img1.png')).convert_alpha()
    backButtonImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "quest", 'assignquestselect_img0.png')).convert_alpha()
    nextButtonImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "quest", 'assignquestselect_img8.png')).convert_alpha()
    prevButtonImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "quest", 'assignquestselect_img9.png')).convert_alpha()

    Quest1 = Button(500,250,questButtonImage,1)
    Quest2 = Button(500,350,questButtonImage,1)
    Quest3 = Button(500,450,questButtonImage,1)
    prevButton = Button(250,450,prevButtonImage,1)
    nextButton = Button(720,450,nextButtonImage,1)
    backButton = Button(271,165,backButtonImage,1)

    return questData,quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton

def quest_selection(quest_data, screen,quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton, current_page):
    currentdata = []
    numberOfDataPerPage = 3
    teacherNameGroup = pygame.sprite.Group()

    if(len(quest_data) <=3):
        currentdata = quest_data
        # print(currentdata)
    elif(len(quest_data) == 0):
        print("no quest")
    else:
        startIndex = (current_page-1)*numberOfDataPerPage
        total_pages = math.ceil(len(quest_data)/3)
        if(current_page == total_pages):
            reminder = len(quest_data)%3
            for i in range(startIndex, startIndex+reminder):
                currentdata.append(quest_data[i])
        else:
            for i in range(startIndex, startIndex+numberOfDataPerPage):
                currentdata.append(quest_data[i])

        # print("length of quest data" + str(len(quest_data)))
        # print("current page: " + str(current_page))
        # print("start index: " +str(startIndex))
    quest_menu.draw(screen)
    prevButton.draw(screen)
    nextButton.draw(screen)
    backButton.draw(screen)

    if(len(currentdata) == 0):
        
        # teacherNameGroup.add("No Quest Assigned",350)
        # teacherNameGroup.draw(screen)
        test_font = pygame.font.Font(os.path.join(
            os.path.dirname(__file__), 'font', 'Pixeltype.ttf'), 50)
        invalid_login_text = test_font.render(
            "NO QUESTS", False, (0, 0, 0))
        screen.blit(invalid_login_text, (400, 300))

    elif(len(currentdata) == 1):
        Quest1.draw(screen)
        
        teacherNameGroup.add(QuestText(currentdata[0]["createdBy"]+"'s Quest",250))
        teacherNameGroup.draw(screen)
    elif(len(currentdata) == 2):
        Quest1.draw(screen)
        Quest2.draw(screen)

        teacherNameGroup.add(QuestText(currentdata[0]["createdBy"]+"'s Quest",250))
        teacherNameGroup.add(QuestText(currentdata[1]["createdBy"]+"'s Quest",350))
        teacherNameGroup.draw(screen)
    elif(len(currentdata) == 3):
        Quest1.draw(screen)
        Quest2.draw(screen)
        Quest3.draw(screen)

        teacherNameGroup.add(QuestText(currentdata[0]["createdBy"]+"'s Quest",250))
        teacherNameGroup.add(QuestText(currentdata[1]["createdBy"]+"'s Quest",350))
        teacherNameGroup.add(QuestText(currentdata[2]["createdBy"]+"'s Quest",450))
        teacherNameGroup.draw(screen)

    return currentdata
    
    



