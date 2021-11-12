import pygame, sys
import pygame_textinput
import Quest.selectQuest2 as selectQuest2
from DatabaseControllers.QuestionDB import QuestionDB
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from DatabaseControllers.QuestionDB import QuestionDB
    else:
        from ..DatabaseControllers.QuestionDB import QuestionDB



mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

h = 600    
w = 1000

screen = pygame.display.set_mode((w,h))
font = pygame.font.SysFont(None, 20)
smallfont = pygame.font.SysFont('Corbel', 25)
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

def assignQuestion(pageNum):
    running = True
    click = False
    background_surface = pygame.image.load("graphics/teacher/assignquestion_background.png").convert()
    buttonimage = pygame.image.load("graphics/teacher/questionbutton.png").convert_alpha()
    nextpageimage = pygame.image.load("graphics/teacher/right.png").convert_alpha()
    prevpageimage = pygame.image.load("graphics/teacher/left.png").convert_alpha()

    names = []
    questionid = []
    questions = QuestionDB.get_all_questions(QuestionDB)
    count=0

    for i in questions:
        names.append(questions[i]['questionText'])
        questionid.append(i)
        count+=1

    while running:
        screen.blit(background_surface, (0, 0))
        pageNumText = smallfont.render(str(pageNum), True, (0, 0, 0))
        screen.blit(pageNumText, (920, 40))
        scale = 1
        button1pos = 138
        button6pos = 521
        button_1 = Button(button1pos, 110, buttonimage, scale)
        button_2 = Button(button1pos, 224, buttonimage, scale)
        button_3 = Button(button1pos, 339, buttonimage, scale)
        button_4 = Button(button1pos, 450, buttonimage, scale)
        button_11 = Button(885, 463, nextpageimage, 1)
        button_12 = Button(48, 463, prevpageimage, 1)
        pageIterator = (pageNum-1) * 4
        try:
            nameText1 = smallfont.render(names[0+pageIterator], True, (0, 0, 0))
            nameText2 = smallfont.render(names[1+pageIterator], True, (0, 0, 0))
            nameText3 = smallfont.render(names[2+pageIterator], True, (0, 0, 0))
            nameText4 = smallfont.render(names[3+pageIterator], True, (0, 0, 0))
        except:
            pass


        if button_1.draw() == True and click:
            import Quest.selectQuest2
            selectQuest2.selectQuest2(1,questionid[0+pageIterator])
        if button_2.draw() == True and click:
            import Quest.selectQuest2
            selectQuest2.selectQuest2(1,questionid[1+pageIterator])
        if button_3.draw() == True and click:
            import Quest.selectQuest2
            selectQuest2.selectQuest2(1,questionid[2+pageIterator])
        if button_4.draw() == True and click:
            import Quest.selectQuest2
            selectQuest2.selectQuest2(1,questionid[3+pageIterator]) 
        if button_11.draw() == True and click:
            if (count - (pageNum * 4) > 0):
                assignQuestion(pageNum+1)
        if button_12.draw() == True and click: 
            if (pageNum!=1):
                assignQuestion(pageNum-1)
        try:
            screen.blit(nameText1, (button1pos+10, 130))
            screen.blit(nameText2, (button1pos+10, 224+20))
            screen.blit(nameText3, (button1pos+10, 339+20))
            screen.blit(nameText4, (button1pos+10, 450+20))
        except:
            pass

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    import Quest.manageQuest as manageQuest
                    manageQuest.manageQuest()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)

        pygame.display.update()
        mainClock.tick(60)
