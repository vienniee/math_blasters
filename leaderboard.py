from DatabaseControllers.ScoresDB import ScoreDB
import pygame
import pygame.freetype
import tkinter as tk
from tkinter import *
import os

#Initialising pygame
pygame.init()

#create display window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

#create text for page
pygame.font.init()
myfont = pygame.font.SysFont('Pixeltype.ttf',60)
namefont = pygame.font.SysFont('Pixeltype.ttf',50)
textsurface = myfont.render('Leaderboard', False, (0,0,0))

#create background image
background_image = pygame.image.load('Image/leaderboard1.png').convert_alpha()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

#create on screen
screen.blit(background_image,(0,0))
screen.blit(textsurface,(360,30))

#call function to draw top players from firestore
scoreDB = ScoreDB()
result = scoreDB.get_score()
positions = []
for key in result:
    student_scores = result[key]
    total_score = 0
    for subjects in student_scores:
        total_score += list(student_scores[subjects].values())[0]
    positions.append((key,total_score))
positions.sort(key=lambda x:(-x[-1],x[1]))

for i in range(len(positions)):
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
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

pygame.quit()