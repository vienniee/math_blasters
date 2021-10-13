import pygame, sys
import pygame_textinput
import question2


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


def question(qn):
    running = True
    click = False

    background_surface = pygame.image.load("Image/modifyquestion_background.png").convert()
    buttonimage = pygame.image.load("Image/generatereportselect_img1.png").convert_alpha()
    largebuttonimage = pygame.image.load("Image/modifyquestion_img0.png").convert_alpha()

    names = ["Option 1", "Option 2", "Option 3", "Option 4"]

    while running:
        screen.fill((255, 255, 255))
        screen.blit(background_surface, (0, 0))

        scale = 1
        button1pos = 155
        button6pos = 521
        button_1 = Button(154, 138, largebuttonimage, scale)
        button_3 = Button(button1pos, 400, buttonimage, scale)
        button_4 = Button(button1pos, 488, buttonimage, scale)
        button_8 = Button(button6pos, 400, buttonimage, scale)
        button_9 = Button(button6pos, 488, buttonimage, scale)

        nameText1 = smallfont.render(names[0], True, (0, 0, 0))
        nameText2 = smallfont.render(names[1], True, (0, 0, 0))
        nameText3 = smallfont.render(names[2], True, (0, 0, 0))
        nameText4 = smallfont.render(names[3], True, (0, 0, 0))
        nameText5 = bigfont.render(qn, True, (0, 0, 0))

        if button_1.draw() == True and click:
            question2.question2()
        if button_3.draw() == True and click:
            question2.question2()
        if button_4.draw() == True and click:
            question2.question2()
        if button_8.draw() == True and click:
            question2.question2()
        if button_9.draw() == True and click:
            question2.question2()

        screen.blit(nameText1, (button1pos+10, 405))
        screen.blit(nameText2, (button1pos+10, 493))
        screen.blit(nameText3, (button6pos+10, 405))
        screen.blit(nameText4, (button6pos+10, 493))
        screen.blit(nameText5, (180, 160))

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