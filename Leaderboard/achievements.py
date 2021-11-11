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
    
    def reward_check(subject,points):
        if subject == "algebra" or subject == "fractions":
            if points <= 20:
                return 0 #bronze
            elif 20 < points <= 40:
                return 1 #silver
            else:
                return 2 #gold

        #total score computation
        else:
            if points <= 30:
                return 0 #bronze
            elif 30 < points <= 50:
                return 1 #silver
            else:
                return 2 #gold
    
    def reward_display(subject,tier):
        if tier == 1:
            display_pic = "achievement_silver.png"
            display_message = "Silver Tier"
        elif tier == 2:
            display_pic = "achievement_gold.png"
            display_message = "Gold Tier"
        else:
            display_pic = "achievement_bronze.png"
            display_message = "Bronze Tier"
        display_pic_size = (300,230)
        
        if subject == "algebra":
            display_position = (70,150)
            Message_position = (100,380)
        elif subject == "fraction":
            display_position = (340,150)
            Message_position = (380,380)
        else:
            display_position = (610,150)
            Message_position = (660,380)
        
        
        reward = pygame.image.load(os.path.join(os.path.dirname(
                     __file__), display_pic)).convert_alpha()
        reward = pygame.transform.scale(reward, display_pic_size)
        Message = myfont.render(display_message, False, (0,0,0))
        screen.blit(reward,display_position)
        screen.blit(Message,Message_position)

    #call function to draw top players from firestore
    scoreDB = ScoreDB()
    studentDB = StudentDB()
    result = scoreDB.get_all_score()
    positions = []
    for key in result:
        student_scores = result[key]
        student_info = studentDB.get_single_student(key)
        total_score = 0
        
        #get total score for all subjects
        for subjects in student_scores:
            total_score += list(student_scores[subjects].values())[0]

        #get score for specific subjects
        algebra = list(student_scores["algebra"].values())[0]
        fractions = list(student_scores["fraction"].values())[0]

        #add to list with all different types of scores to be sorted
        positions.append((key,student_info["name"], total_score, algebra, fractions))
    positions.sort(key=lambda x:(-x[-1],x[2]))


    #check if student has hit the score needed for achievements to be unlocked
    #default trophy is bronze
    algebra_award = 0
    fraction_award = 0
    totalScore_award = 0

    found = 0
    for i in range(len(positions)):
        if positions[i][0] == "-Mm8fShiNigSh-PCK--C": #replace hardcoded ID with studentID field later
            found = 1
            totalScore_award = reward_check("total",positions[i][2])
            algebra_award = reward_check("algebra",positions[i][3])
            fraction_award = reward_check("fractions",positions[i][4])

            reward_display("Total",totalScore_award)
            reward_display("algebra",algebra_award)
            reward_display("fraction",fraction_award)
            break
    
    if found == 0:
        text = myfont.render("No Achievements Yet", False, (0,0,0))
        screen.blit(text,(500,300))

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