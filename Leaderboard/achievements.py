from DatabaseControllers.ScoresDB import ScoreDB
import pygame
import pygame.freetype
import tkinter as tk
from tkinter import *
from Login import assets
import os

from StudentDB import StudentDB

def Achievements(studentID):

    #Initialising pygame
    pygame.init()

    #create display window
    screen_width = 1000
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))

    #create text for page
    pygame.font.init()
    myfont = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'Pixeltype.ttf'), 60)
    textsurface = myfont.render('Achievements', False, (0,0,0))

    #create background image
    background_image = pygame.image.load(os.path.join(os.path.dirname(
                    __file__), "Standard_background.png")).convert_alpha()
    back_img = pygame.image.load(os.path.join(os.path.dirname(
                    __file__), "backButton copy.png")).convert_alpha()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    #create on screen
    screen.blit(background_image,(0,0))
    screen.blit(textsurface,(380,20))
    backButton = assets.Button(screen=screen,id='buttonRegistration',image=back_img,scale=1,x=20,y=20)

    def backButton_clicked():
        print("Back Button Clicked")
        return True
    
    #call function to draw top players from firestore
    scoreDB = ScoreDB()
    studentDB = StudentDB()
    result = scoreDB.get_all_score()
    positions = []
    for key in result:
        student_scores = result[key]
        student_info = studentDB.get_single_student(key)
        total_score = 0
        for subjects in student_scores:
            total_score += list(student_scores[subjects].values())[0]
        positions.append((key,student_info["name"], total_score))
    positions.sort(key=lambda x:(-x[-1],x[1]))


    #check if student has hit the score needed for achievements to be unlocked
    # found = 0
    # for i in range(len(positions)):
    #     if positions[i][0] == "-Mm8fShiNigSh-PCK--C":
    #         found = 1
    #         if positions[i][2] < 30:
    #             bronze = pygame.image.load(os.path.join(os.path.dirname(
    #                 __file__), "achievement_bronze.png")).convert_alpha()
    #             bronze = pygame.transform.scale(bronze, (300, 230))
    #             bronzeMessage = myfont.render('Bronze Tier', False, (0,0,0))
    #             screen.blit(bronze,(340,150))
    #             screen.blit(bronzeMessage,(370,380))
    #         elif 30 <= positions[i][2] < 50:
    #             silver = pygame.image.load(os.path.join(os.path.dirname(
    #                 __file__), "achievement_silver.png")).convert_alpha()
    #             silver = pygame.transform.scale(silver, (300, 60))
    #             silverMessage = myfont.render('Silver Tier', False, (0,0,0))
    #             screen.blit(silver,(280,180))
    #             screen.blit(silverMessage,(200,100))
    #         elif positions[i][2] >= 50:
    #             gold = pygame.image.load(os.path.join(os.path.dirname(
    #                 __file__), "achievement_gold.png")).convert_alpha()
    #             gold = pygame.transform.scale(gold, (300, 60))
    #             goldMessage = myfont.render('Gold Tier', False, (0,0,0))
    #             screen.blit(gold,(280,180))
    #             screen.blit(goldMessage,(200,100))
    # if found == 0:
    #     noAchievement = myfont.render('No Achievements Yet', False, (0,0,0))
    #     screen.blit(noAchievement,(330,100))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if backButton.draw():
                if backButton_clicked():
                    return 1
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

    pygame.quit()