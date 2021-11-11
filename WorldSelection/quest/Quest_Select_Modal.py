import pygame
from DatabaseControllers.QuestDB import QuestDB
import os
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
        action = False
        #getting mouse position
        pos = pygame.mouse.get_pos()
        # print(pos)

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print(pos)
                print('clicked')
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

class Quest_menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        quest_menu = pygame.image.load(os.path.join(os.path.dirname(__file__),"quest", 'quest_background.png')).convert_alpha()
        self.image = quest_menu
        self.rect = self.image.get_rect(center=(500, 300))

def load_asset(subject):
    
    questDatabase = QuestDB()

    if(subject == "math"):
        questData = questDatabase.get_quest()
        print(questData)

    elif(subject =="science"):
        questData = questDatabase.get_quest()
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

    return quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton

def quest_selection(screen,quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton):
    quest_menu.draw(screen)
    Quest1.draw(screen)
    Quest2.draw(screen)
    Quest3.draw(screen)
    prevButton.draw(screen)
    nextButton.draw(screen)
    backButton.draw(screen)



