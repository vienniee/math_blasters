from DatabaseControllers.ScoresDB import ScoreDB
import pygame
import pygame.freetype
import tkinter as tk
from tkinter import *
from Login import assets
import os

from StudentDB import StudentDB

def Leaderboard():
    #Initialising pygame
    pygame.init()

    #create display window
    screen_width = 1000
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))

    #create text for page
    pygame.font.init()
    # myfont = pygame.font.SysFont('Pixeltype.ttf',60)
    myfont = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'Pixeltype.ttf'), 60)
    # namefont = pygame.font.SysFont('Pixeltype.ttf',50)
    namefont = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'Pixeltype.ttf'), 50)
    textsurface = myfont.render('Leaderboard', False, (0,0,0))

    #create background image
    # background_image = pygame.image.load('Image/leaderboard1.png').convert_alpha()
    background_image = pygame.image.load(os.path.join(os.path.dirname(
                    __file__), "leaderboard1.png")).convert_alpha()
    back_img = pygame.image.load(os.path.join(os.path.dirname(
                    __file__), "backButton copy.png")).convert_alpha()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    #create on screen
    screen.blit(background_image,(0,0))
    screen.blit(textsurface,(360,30))
    backButton = assets.Button(screen=screen,id='buttonRegistration',image=back_img,scale=1,x=20,y=20)

    def backButton_clicked():
        print("Back Button Clicked")
        return True

    #call function to draw top players from firestore
    scoreDB = ScoreDB()
    studentDB = StudentDB()
    result = scoreDB.get_all_score()
    positions = []

    #Iterating through the scores of all students
    #Summing the total score of each student from all subjects
    for key in result:
        student_scores = result[key]
        student_info = studentDB.get_single_student(key)
        total_score = 0
        for subjects in student_scores:
            level_scores = list(student_scores[subjects].values())
            # print(level_scores)
            for level in range(0,len(level_scores)):
                # print(level)
                total_score += level_scores[level]
        #Holding the student info and total scores in a list
        positions.append((student_info["name"], total_score))
    #Sorting the list in descending oder to be displayed
    positions.sort(key=lambda x:(-x[-1],x[1]))

    #Selecting the top 5 students in the list to be displayed
    for i in range(5):
        #convert data to string to be displayed
        student_names = namefont.render(str(positions[i][0]),False,(0,0,0))
        ranking = myfont.render(str(i+1),False,(0,0,0))
        scores = myfont.render(str(positions[i][1]),False,(0,0,0))
        
        #display on screen at fixed positions
        screen.blit(student_names,(265,85*i+150))
        screen.blit(ranking,(170,85*i+150))
        screen.blit(scores,(730,85*i+150))

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
