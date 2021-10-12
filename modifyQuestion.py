import pygame, sys
import pygame_textinput
import question

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

def modifyQuestion(pageNum):
    running = True
    click = False
    background_surface = pygame.image.load("Image/modifyquestionselect_background.png").convert()
    buttonimage = pygame.image.load("Image/generatereportselect_img1.png").convert_alpha()
    nextpageimage = pygame.image.load("Image/generatereportselect_img8.png").convert_alpha()
    prevpageimage = pygame.image.load("Image/generatereportselect_img9.png").convert_alpha()

    names = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6","Question 7","Question 8","Question 9","Question 10"]

    while running:

        screen.blit(background_surface, (0, 0))
        pageNumText = smallfont.render(str(pageNum), True, (0, 0, 0))
        screen.blit(pageNumText, (920, 40))
        scale = 1
        button1pos = 155
        button6pos = 521
        button_1 = Button(button1pos, 123, buttonimage, scale)
        button_2 = Button(button1pos, 210, buttonimage, scale)
        button_3 = Button(button1pos, 297, buttonimage, scale)
        button_4 = Button(button1pos, 385, buttonimage, scale)
        button_5 = Button(button1pos, 472, buttonimage, scale)
        button_6 = Button(button6pos, 123, buttonimage, scale)
        button_7 = Button(button6pos, 210, buttonimage, scale)
        button_8 = Button(button6pos, 297, buttonimage, scale)
        button_9 = Button(button6pos, 385, buttonimage, scale)
        button_10 = Button(button6pos, 472, buttonimage, scale)
        button_11 = Button(885, 463, nextpageimage, 1)
        button_12 = Button(48, 463, prevpageimage, 1)

        nameText1 = smallfont.render(names[0], True, (0, 0, 0))
        nameText2 = smallfont.render(names[1], True, (0, 0, 0))
        nameText3 = smallfont.render(names[2], True, (0, 0, 0))
        nameText4 = smallfont.render(names[3], True, (0, 0, 0))
        nameText5 = smallfont.render(names[4], True, (0, 0, 0))
        nameText6 = smallfont.render(names[5], True, (0, 0, 0))
        nameText7 = smallfont.render(names[6], True, (0, 0, 0))
        nameText8 = smallfont.render(names[7], True, (0, 0, 0))
        nameText9 = smallfont.render(names[8], True, (0, 0, 0))
        nameText10 = smallfont.render(names[9], True, (0, 0, 0))

        if button_1.draw() == True and click:
            question.question(names[0])
        if button_2.draw() == True and click:
            question.question(names[1])
        if button_3.draw() == True and click:
            question.question(names[2])
        if button_4.draw() == True and click:
            question.question(names[3])
        if button_5.draw() == True and click:
            question.question(names[4])
        if button_6.draw() == True and click:
            question.question(names[5])
        if button_7.draw() == True and click:
            question.question(names[6])
        if button_8.draw() == True and click:
            question.question(names[7])
        if button_9.draw() == True and click:
            question.question(names[8])
        if button_10.draw() == True and click:
            question.question(names[9])
        if button_11.draw() == True and click:
            modifyQuestion(pageNum+1)
        if button_12.draw() == True and click:
            if (pageNum!=1):
                modifyQuestion(pageNum-1)

        screen.blit(nameText1, (button1pos+10, 128))
        screen.blit(nameText2, (button1pos+10, 215))
        screen.blit(nameText3, (button1pos+10, 302))
        screen.blit(nameText4, (button1pos+10, 390))
        screen.blit(nameText5, (button1pos+10, 477))
        screen.blit(nameText6, (button6pos+10, 128))
        screen.blit(nameText7, (button6pos+10, 215))
        screen.blit(nameText8, (button6pos+10, 302))
        screen.blit(nameText9, (button6pos+10, 390))
        screen.blit(nameText10, (button6pos+10, 477))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)