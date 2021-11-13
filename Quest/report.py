import pygame, sys
import pygame_textinput
from DatabaseControllers.ScoresDB import ScoreDB


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

def report(name, studentid):
    running = True
    background_surface = pygame.image.load("graphics/teacher/report_background.png").convert()
    while running:
       
        screen.blit(background_surface, (0, 0))
        scores = ScoreDB.get_single_score(ScoreDB, studentid)

        algebra_lv1 = "NA"
        algebra_lv2 = "NA"
        algebra_lv3 = "NA"
        fraction_lv1 = "NA"
        fraction_lv2 = "NA"
        fraction_lv3 = "NA"
        chemistry_lv1 = "NA"
        chemistry_lv2 = "NA"
        chemistry_lv3 = "NA"
        physics_lv1 = "NA"
        physics_lv2 = "NA"
        physics_lv3 = "NA"

        try:
            algebra_lv1 =str(scores['algebra']['level 1'])
            algebra_lv2 = str(scores['algebra']['level 2'])
            algebra_lv3 = str(scores['algebra']['level 3'])
            fraction_lv1 = str(scores['fraction']['level 1'])
            fraction_lv2 = str(scores['fraction']['level 2'])
            fraction_lv3 = str(scores['fraction']['level 3'])
            chemistry_lv1 = str(scores['chemistry']['level 1'])
            chemistry_lv2 = str(scores['chemistry']['level 2'])
            chemistry_lv3 = str(scores['chemistry']['level 3'])
            physics_lv1 = str(scores['physics']['level 1'])
            physics_lv2 = str(scores['physics']['level 2'])
            physics_lv3 = str(scores['physics']['level 3'])
        except:
            pass


        studentName = name
        studentNameText = bigfont.render(studentName, True, (0, 0, 0))
        score1 = smallfont.render(algebra_lv1, True, (0, 0, 0))
        score2 = smallfont.render(algebra_lv2, True, (0, 0, 0))
        score3 = smallfont.render(algebra_lv3, True, (0, 0, 0))
        score4 = smallfont.render(fraction_lv1, True, (0, 0, 0))
        score5 = smallfont.render(fraction_lv2, True, (0, 0, 0))
        score6 = smallfont.render(fraction_lv3, True, (0, 0, 0))
        score7 = smallfont.render(chemistry_lv1, True, (0, 0, 0))
        score8 = smallfont.render(chemistry_lv2, True, (0, 0, 0))
        score9 = smallfont.render(chemistry_lv3, True, (0, 0, 0))
        score10 = smallfont.render(physics_lv1, True, (0, 0, 0))
        score11 = smallfont.render(physics_lv2, True,(0, 0, 0))
        score12 = smallfont.render(physics_lv3, True, (0, 0, 0))

        button1x = 300
        button7x = 750
        button1y = 220
        
        screen.blit(studentNameText, (100, 25))
        screen.blit(score1, (button1x, button1y))
        screen.blit(score2, (button1x, button1y+40))
        screen.blit(score3, (button1x, button1y+80))
        screen.blit(score4, (button1x, button1y+180))
        screen.blit(score5, (button1x, button1y+220))
        screen.blit(score6, (button1x, button1y+260))
        screen.blit(score7, (button7x,  button1y))
        screen.blit(score8, (button7x,  button1y+40))
        screen.blit(score9, (button7x, button1y+80))
        screen.blit(score10, (button7x,  button1y+180))
        screen.blit(score11, (button7x,  button1y+220))
        screen.blit(score12, (button7x,  button1y+260))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)