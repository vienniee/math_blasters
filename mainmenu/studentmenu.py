import pygame
import pygame.freetype
import random
import os
from os import path
pygame.init()

#create display window
SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#load background image
background_surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'student_menu.png')).convert()

#load button images
play_img = pygame.image.load(os.path.join(os.path.dirname(__file__),  'play_button.png')).convert_alpha()
achievements_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'achievements_button.png')).convert_alpha()
leaderboard_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'leaderboard_button.png')).convert_alpha()
logout_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'logout_button.png')).convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #getting mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('clicked')
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

#create button instances
play_button = Button(SCREEN_WIDTH/2-160, 260, play_img, 1)
achievements_button = Button(SCREEN_WIDTH/2-160, 330, achievements_img, 1)
leaderboard_button = Button(SCREEN_WIDTH/2-160, 400, leaderboard_img, 1)
logout_button = Button(SCREEN_WIDTH/2-160,190,logout_img,0.32)

#game loop
def studentMenu():
    run = True
    while run:
        screen.fill((202, 228, 241))
        screen.blit(background_surface, (0, 0))

        #menu option select 
        if play_button.draw() == True:
            print('play selected')
            return 1
        if achievements_button.draw() == True:
            print('achievements selected')
            return 2
        if leaderboard_button.draw() == True:
            print('leaderboard selected')
            return 3
        if logout_button.draw() == True:
            print('logout selected')
            return 4
        
        

        #event handler
        for event in pygame.event.get():
            #quit game 
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    studentMenu()
    