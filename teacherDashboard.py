import pygame, sys
import pygame_textinput
from DatabaseControllers.StudentDB import StudentDB
import pandas as pd
import sys



# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

h = 600    
w = 1000

screen = pygame.display.set_mode((w,h))
font = pygame.font.SysFont(None, 20)
smallfont = pygame.font.SysFont('Corbel', 35)
bigfont = pygame.font.SysFont('Corbel', 60)




def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


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
                print(pos)
                print('clicked')
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

click = False


def main_menu():
    click = False
    
    #load background image
    background_surface = pygame.image.load("graphics/teacher/teacherdashboard_background.png").convert()
    buttonimage1 = pygame.image.load("graphics/teacher/teacherdashboard_img1.png").convert_alpha()
    buttonimage2 = pygame.image.load("graphics/teacher/teacherdashboard_img0.png").convert_alpha()
    buttonimage3 = pygame.image.load("graphics/teacher/teacherdashboard_img2.png").convert_alpha()

    button_1 = Button(w/2-160, 260, buttonimage1, 1)
    button_2 = Button(w/2-160, 330, buttonimage2, 1)
    button_3 = Button(w/2-160, 400, buttonimage3, 1)

    while True:
        screen.fill((255, 255, 255))
        screen.blit(background_surface, (0, 0))

        if button_1.draw() == True and click:
            import generateReport
            generateReport.generateReport(1)
        if button_2.draw() == True and click:
            import modifyQuestion
            modifyQuestion.modifyQuestion(1)  
        if button_3.draw() == True and click:
            import manageQuest
            manageQuest.manageQuest()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)

main_menu()
