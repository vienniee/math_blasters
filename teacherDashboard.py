import pygame, sys
import pygame_textinput

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
    background_surface = pygame.image.load("Image/teacherdashboard_background.png").convert()
    buttonimage1 = pygame.image.load("Image/teacherdashboard_img0.png").convert_alpha()
    buttonimage2 = pygame.image.load("Image/teacherdashboard_img1.png").convert_alpha()
    buttonimage3 = pygame.image.load("Image/teacherdashboard_img2.png").convert_alpha()

    button_1 = Button(w/2-160, 260, buttonimage1, 1)
    button_2 = Button(w/2-160, 330, buttonimage2, 1)
    button_3 = Button(w/2-160, 400, buttonimage3, 1)

    while True:
        screen.fill((255, 255, 255))
        screen.blit(background_surface, (0, 0))

        if button_1.draw() == True and click:
            generateReport(1)
        if button_2.draw() == True and click:
            modifyQuestion(1)  
        if button_3.draw() == True and click:
            assignQuest(1)
        
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


def generateReport(pageNum):
    running = True
    click = False
    background_surface = pygame.image.load("Image/generatereportselect_background.png").convert()
    buttonimage = pygame.image.load("Image/generatereportselect_img1.png").convert_alpha()
    nextpageimage = pygame.image.load("Image/generatereportselect_img8.png").convert_alpha()
    prevpageimage = pygame.image.load("Image/generatereportselect_img9.png").convert_alpha()

    names = ["Name 1", "Name 2", "Name 3", "Name 4", "Name 5", "Name 6","Name 7","Name 8","Name 9","Name 10"]

    while running:
        screen.blit(background_surface, (0, 0))
        scale = 1
        button1pos = 155
        button6pos = 521

        pageNumText = smallfont.render(str(pageNum), True, (0, 0, 0))
        screen.blit(pageNumText, (920, 40))

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
            report(names[0])
        if button_2.draw() == True and click:
            report(names[1])
        if button_3.draw() == True and click:
            report(names[2])
        if button_4.draw() == True and click:
            report(names[3])
        if button_5.draw() == True and click:
            report(names[4])
        if button_6.draw() == True and click:
            report(names[5])
        if button_7.draw() == True and click:
            report(names[6])
        if button_8.draw() == True and click:
            report(names[7])
        if button_9.draw() == True and click:
            report(names[8])
        if button_10.draw() == True and click:
            report(names[9])
        if button_11.draw() == True and click:
            generateReport(pageNum+1)
        if button_12.draw() == True and click:
            if (pageNum!=1):
                generateReport(pageNum-1)

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
            question(names[0])
        if button_2.draw() == True and click:
            question(names[1])
        if button_3.draw() == True and click:
            question(names[2])
        if button_4.draw() == True and click:
            question(names[3])
        if button_5.draw() == True and click:
            question(names[4])
        if button_6.draw() == True and click:
            question(names[5])
        if button_7.draw() == True and click:
            question(names[6])
        if button_8.draw() == True and click:
            question(names[7])
        if button_9.draw() == True and click:
            question(names[8])
        if button_10.draw() == True and click:
            question(names[9])
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
            question2()
        if button_3.draw() == True and click:
            question2()
        if button_4.draw() == True and click:
            question2()
        if button_8.draw() == True and click:
            question2()
        if button_9.draw() == True and click:
            question2()

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

def question2():
    running = True
    click = False

    textinput = pygame_textinput.TextInputVisualizer()

    background_surface = pygame.image.load("Image/modifyquestion2_background.png").convert()

    while running:
        screen.fill((225, 225, 225))
        screen.blit(background_surface, (0, 0))

        events = pygame.event.get()

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (100, 300))

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN and event.key == K_RETURN:
                print(f"User pressed enter! Input so far: {textinput.value}")

        pygame.display.update()
        mainClock.tick(60)

def report(name):
    running = True
    background_surface = pygame.image.load("Image/report_background.png").convert()
    while running:
       
        screen.blit(background_surface, (0, 0))
        algebra_lv1 =str(1)
        algebra_lv2 = str(1)
        algebra_lv3 = str(1)
        fraction_lv1 = str(1)
        fraction_lv2 = str(1)
        fraction_lv3 = str(1)
        chemistry_lv1 = str(1)
        chemistry_lv2 = str(1)
        chemistry_lv3 = str(1)
        physics_lv1 = str(1)
        physics_lv2 = str(1)
        physics_lv3 = str(1)
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


def assignQuest(pageNum):
    running = True
    click = False
    background_surface = pygame.image.load("Image/assignquestselect_background.png").convert()
    buttonimage = pygame.image.load("Image/generatereportselect_img1.png").convert_alpha()
    nextpageimage = pygame.image.load("Image/generatereportselect_img8.png").convert_alpha()
    prevpageimage = pygame.image.load("Image/generatereportselect_img9.png").convert_alpha()

    names = ["Name 1", "Name 2", "Name 3", "Name 4", "Name 5", "Name 6","Name 7","Name 8","Name 9","Name 10"]

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
            selectQuest(1,names[0])
        if button_2.draw() == True and click:
            selectQuest(1,names[1])
        if button_3.draw() == True and click:
            selectQuest(1,names[2])
        if button_4.draw() == True and click:
            selectQuest(1,names[3])
        if button_5.draw() == True and click:
            selectQuest(1,names[4])
        if button_6.draw() == True and click:
            selectQuest(1,names[5])
        if button_7.draw() == True and click:
            selectQuest(1,names[6])
        if button_8.draw() == True and click:
            selectQuest(1,names[7])
        if button_9.draw() == True and click:
            selectQuest(1,names[8])
        if button_10.draw() == True and click:
            selectQuest(1,names[9])
        if button_11.draw() == True and click:
            assignQuest(pageNum+1)
        if button_12.draw() == True and click: 
            if (pageNum!=1):
                assignQuest(pageNum-1)

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

def selectQuest(pageNum,name):
    running = True
    click = False
    background_surface = pygame.image.load("Image/assignquestselect2_background.png").convert()
    buttonimage = pygame.image.load("Image/generatereportselect_img1.png").convert_alpha()
    nextpageimage = pygame.image.load("Image/generatereportselect_img8.png").convert_alpha()
    prevpageimage = pygame.image.load("Image/generatereportselect_img9.png").convert_alpha()

    names = ["Quest 1", "Quest 2", "Quest 3", "Quest 4", "Quest 5", "Quest 6","Quest 7","Quest 8","Quest 9","Quest 10"]

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
            main_menu()
        if button_2.draw() == True and click:
            main_menu()
        if button_3.draw() == True and click:
            main_menu()
        if button_4.draw() == True and click:
            main_menu()
        if button_5.draw() == True and click:
            main_menu()
        if button_6.draw() == True and click:
            main_menu()
        if button_7.draw() == True and click:
            main_menu()
        if button_8.draw() == True and click:
            main_menu()
        if button_9.draw() == True and click:
            main_menu()
        if button_10.draw() == True and click:
            main_menu()
        if button_11.draw() == True and click:
            selectQuest(pageNum+1, name)
        if button_12.draw() == True and click:
            if (pageNum!=1):
                selectQuest(pageNum-1, name)
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

main_menu()
