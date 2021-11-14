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
    newfont = pygame.font.SysFont('arialblack',20)
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

    #function for back button
    def backButton_clicked():
        print("Back Button Clicked")
        return True
    
    #To check the awards to be given out based on the student scores
    def reward_check(subject_scores):
        scoring_chart = []
        for subject in subject_scores:
            #To check if he falls under the bronze category for that subject
            if subject_scores[subject] < 15:
                scoring_chart.append((subject,0))
            #To check if he falls under the silver category for that subject
            elif 15 <= subject_scores[subject] < 28:
                scoring_chart.append((subject,1))
            else:
            #To check if he falls under the gold category for that subject
                scoring_chart.append((subject,2))
        return scoring_chart

    #Determine the reward picture to display and the position of the achievements on the page
    #input from reward_check
    def reward_display(scoring_chart):
        for i in range(len(scoring_chart)):
            display_position = (40,150)
            Message_position = (110,380)
            display_pic_size = (280,230)

            #Based on reward_check, retrieve relevant images to display as achievements
            if scoring_chart[i][1] == 1:
                display_pic = "achievement_silver.png"
                display_message = str(scoring_chart[i][0])
            elif scoring_chart[i][1] == 2:
                display_pic = "achievement_gold.png"
                display_message = str(scoring_chart[i][0])
            else:
                display_pic = "achievement_bronze.png"
                display_message = str(scoring_chart[i][0])

            #Determine the position of the achievement on the page depending on the subject
            display_position = ((display_position[0]+(i*220)),150)
            Message_position = ((Message_position[0]+(i*220)),380)

            #Loading of actual achievements on the page
            reward = pygame.image.load(os.path.join(os.path.dirname(
                     __file__), display_pic)).convert_alpha()
            reward = pygame.transform.scale(reward, display_pic_size)
            Message = newfont.render(display_message.upper(), False, (0,0,0))
            screen.blit(reward,display_position)
            screen.blit(Message,Message_position)


    scoreDB = ScoreDB()
    studentDB = StudentDB()

    #to be used to test
    #student ID (no subjects)
    #"-Mm8fShiNigSh-PCK--C" (4 subjects)
    #"-Mm8fTpbu4sZxWmEKBb4" (2 subjects)
    student_score = scoreDB.get_single_score(studentID)
    
    #if student has not attempted anything
    if student_score is None:
        Message = myfont.render("No Achievements Yet", False, (0,0,0))
        screen.blit(Message,(320,300))
    #if student has attempting some quizzes
    else:
        subject_scores = {}
        for subjects in student_score:
            total_score = 0
            for levels in student_score[subjects]:
                total_score += student_score[subjects][levels]
            subject_scores[subjects] = total_score
        
        scoring_chart = reward_check(subject_scores)
        reward_display(scoring_chart)

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
