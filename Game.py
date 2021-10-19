import pygame
import random
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
fps = 60

#game width
bottom_panel = 200
screen_width = 1000
screen_height = 400 +bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

#define fonts
bigfont = pygame.font.SysFont('Times New Roman',40)
font = pygame.font.SysFont('Times New Roman',26)

#define colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
gray = (220,220,220)
white = (0,0,0)

#define gaming variables

clicked = False



def Game(topic,level,gender,name):

    #define gaming variables
    action_cd = 0
    action_wait_time = 90
    score = 0
    charselect = gender
    charname = name
    game_over = 0

    #load images
    #background images
    background_img = pygame.image.load('Image/castlebackground.png').convert_alpha()
    #panel image
    panel_img = pygame.image.load('Image/panel.png').convert_alpha()
    #button image
    button_img = pygame.image.load('Image/button.png').convert_alpha()
    #victory and defeat image
    victory_img = pygame.image.load('Image/victory.png').convert_alpha()
    defeat_img = pygame.image.load('Image/defeat.png').convert_alpha()

    #function to draw text
    def draw_text(text,font,text_col,x,y):
        img = font.render(text, True, text_col)
        screen.blit(img,(x,y))

    #load question list
    #sample, first digit is the passing score
    #questions with 4 options, last is answer
    questionlist = ["2",["1 + 1 = ?", "1", "2", "3", "4", "2"], ["2 + 2 = ?", "2", "1", "4", "3","4"],["3 + 3 = ?", "2", "4", "6", "8", "6"]]
    question_list = questionlist[1:]
    passingmark = int(questionlist[0])

    #function to randomise the question order
    def createRandomSortedList(num, start, end):
        arr = []
        tmp = random.randint(start, end)
        for x in range(num):
            while tmp in arr:
                tmp = random.randint(start, end)
            arr.append(tmp)
        return arr

    orderlist = createRandomSortedList(len(question_list),0,len(question_list)-1)

    reorderQlist = []
    for i in orderlist:
        reorderQlist.append(question_list[i])


    #function to draw bg
    def draw_bg():
        screen.blit(background_img,(-200,-bottom_panel))

    #function to draw panel
    def draw_pnl():
        screen.blit(panel_img,(0,screen_height-bottom_panel))
        #show stats
        draw_text(f'{charname} HP:{player.hp}', font, red, 210, screen_height - bottom_panel + 5)
        draw_text(f'{enemies.name} HP:{enemies.hp}', font, red, 560, screen_height - bottom_panel + 5)

    #Question panel
    class questionpanel():
        text_col = black
        def __init__(self, x, y,width,height, text):
            self.x = x
            self.y = y
            self.text = text
            self.width = width
            self.height = height

        def draw(self):

            # create pygame Rect object for the label
            label_rect = Rect(self.x, self.y, self.width, self.height)

            pygame.draw.rect(screen, (229, 229, 229) , label_rect)

            # add shading to label
            pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

            # add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y+5))



    #create button/label instances/answer_list
    questionbuttonlist1 = []
    questionbuttonlist2 = []
    questionbuttonlist3 = []
    questionbuttonlist4 = []
    questions = []
    answers = []
    for i in range(len(reorderQlist)):
        questionbuttonlist1.append(button(20,470,380,40,reorderQlist[i][1]))
        questionbuttonlist2.append(button(440,470,380,40,reorderQlist[i][2]))
        questionbuttonlist3.append(button(20,530,380,40,reorderQlist[i][3]))
        questionbuttonlist4.append(button(440,530,380,40,reorderQlist[i][4]))
        questions.append(questionpanel(260,100,450,80,reorderQlist[i][0]))
        answers.append(reorderQlist[i][5])
    #end of questions
    questionbuttonlist1.append(button(20, 470, 380, 40,'-'))
    questionbuttonlist2.append(button(440, 470, 380, 40, '-'))
    questionbuttonlist3.append(button(20, 530, 380, 40, '-'))
    questionbuttonlist4.append(button(440, 530, 380, 40, '-'))

    abandon_button = button(850,490,140,40,"ABANDON")
    next_button = button(430,180,100,45,"NEXT")

    #define curse sprite
    class curselogo():
        def __init__(self, x, y, scale):
            self.animation_list = []
            self.frame_index= 0
            self.update_time = pygame.time.get_ticks()
            #load curse logo
            for i in range(15):
                img = pygame.image.load(f'Image/curse/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
                self.animation_list.append(img)
            self.image = self.animation_list[self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

        def update(self):
            animation_cooldown = 150
            # update animation
            self.image = self.animation_list[self.frame_index]
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0

        def draw(self):
            screen.blit(self.image, self.rect)


    #define curse
    class curse():
        def __init__(self, x, y, scale):
            self.animation_list = []
            self.frame_index= 0
            self.update_time = pygame.time.get_ticks()
            #load ignite images
            for i in range(14):
                img = pygame.image.load(f'Image/ignite/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
                self.animation_list.append(img)
            self.image = self.animation_list[self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

        def update(self):
            animation_cooldown = 150
            #update animation
            self.image = self.animation_list[self.frame_index]
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >= len(self.animation_list):
                self.frame_index = len(self.animation_list) - 1


        def draw(self):
            screen.blit(self.image,self.rect)

    #create curse instance
    playercurse = curse(280,290,2.5)
    enemiescurse = curse(650,290,2.5)
    logo = curselogo(670,45,0.2)

    #define player
    class character():
        def __init__(self, x, y, name, max_hp,scale):
            self.name = name
            self.max_hp = max_hp
            self.hp = max_hp
            self.alive = True
            self.animation_list = []
            self.frame_index= 0
            self.action = 0#0:idle, 1:attack, 2:hurt, 3:death, if player answer question wrong, the enemies will attack
            self.update_time = pygame.time.get_ticks()
            #load idle images
            temp_list = []
            for i in range(4):
                img = pygame.image.load(f'Image/{self.name}/idle/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            #load attack images
            temp_list = []
            for i in range(4):
                img = pygame.image.load(f'Image/{self.name}/attack/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            #load hurt images
            temp_list = []
            for i in range(4):
                img = pygame.image.load(f'Image/{self.name}/hurt/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            #load death images
            temp_list = []
            for i in range(4):
                img = pygame.image.load(f'Image/{self.name}/death/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            self.image = self.animation_list[self.action][self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

        def update(self):
            animation_cooldown = 150
            #update animation
            self.image = self.animation_list[self.action][self.frame_index]
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            #if the animation has run out then reset to idle state
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action ==3:
                    self.frame_index = len(self.animation_list[self.action]) -1
                else:
                    self.idle()

        def attack(self,target):
            #deal damage
            damage = 1
            target.hp -= damage
            #run hurt animation
            target.hurt()
            #check death
            if target.hp < 1:
                target.hp = 0
                target.alive = False
                target.death()
            damage_text = DamageText(target.rect.centerx, 230, str(damage), red)
            damage_text_group.add(damage_text)
            #set variables to attack
            self.action = 1
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def idle(self):
            # set variables to attack
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def hurt(self):
            # set variables to attack
            self.action = 2
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def death(self):
            # set variables to attack
            self.action = 3
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def draw(self):
            screen.blit(self.image,self.rect)

    #define healthbar
    class healthbar():
        def __init__(self,x,y,hp,max_hp):
            self.x =x
            self.y =y
            self.hp = hp
            self.max_hp = max_hp

        def draw(self,hp):
            #update with new health
            self.hp = hp
            healthratio = self.hp / self.max_hp
            pygame.draw.rect(screen,red,(self.x,self.y,150,20))
            pygame.draw.rect(screen, green, (self.x, self.y, 150*healthratio, 20))

    class progressbar():
        def __init__(self,x,y,current,totalprogress):
            self.x = x
            self.y = y
            self.current = current
            self.totalprogress = totalprogress

        def draw(self,current):
            #update with new health
            self.current = current
            ratio = self.current / self.totalprogress
            if ratio >= 1:
                ratio = 1
            pygame.draw.rect(screen,gray,(self.x, self.y,300,20))
            pygame.draw.rect(screen, blue, (self.x, self.y, 300*ratio, 20))

    class DamageText(pygame.sprite.Sprite):
        def __init__(self, x, y, damage, colour):
            pygame.sprite.Sprite.__init__(self)
            self.image = font.render(damage, True, colour)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.counter = 0

        def update(self):
            #move damage text up
            self.rect.y -= 1
            #delete the text after a few seconds
            self.counter += 1
            if self.counter > 30:
                self.kill()

    damage_text_group = pygame.sprite.Group()

    #create character instance
    if charselect == "male":
        player = character(280, 310, charselect, len(questionlist) - 1, 3.5)
    else:
        player = character(280, 310, charselect, len(questionlist) - 1, 3.5)
    enemies = character(650,310,'enemies',len(questionlist)-1,2.5)

    player_hp = healthbar(210,screen_height-bottom_panel+40,player.hp,player.max_hp)
    enemies_hp = healthbar(560,screen_height-bottom_panel+40,enemies.hp,enemies.max_hp)

    progress_bar = progressbar(screen_width/3,40,enemies.max_hp-enemies.hp,passingmark)

    questionnum = 0


    def pause():
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        print("change to castle screen")
                        pygame.quit() # change to castle screen
                        quit()

            screen.fill(gray)
            draw_text("Are you going to abandon the mission?", bigfont, black, 200, 200)
            draw_text("Press C to Continue, Q to Quit",font,black,350,320)
            pygame.display.update()
            clock.tick(15)




    run = True
    while run:

        clock.tick(fps)
        #draw background
        draw_bg()
        #draw panel
        draw_pnl()
        #draw hp
        player_hp.draw(player.hp)
        enemies_hp.draw(enemies.hp)
        #draw progress bar/curse
        progress_bar.draw(enemies.max_hp-enemies.hp)
        logo.update()
        logo.draw()

        #draw and update character animation
        player.update()
        player.draw()
        enemies.update()
        enemies.draw()

        #damage text
        damage_text_group.update()
        damage_text_group.draw(screen)



        if enemies.alive == False:
            game_over = 1
            enemiescurse.update()
            enemiescurse.draw()
            screen.blit(victory_img,(350,100))
            if next_button.draw():
                print("return score portion")
                return score

        if player.alive == False:
            game_over = 1
            playercurse.update()
            playercurse.draw()
            screen.blit(defeat_img,(370,100))
            if next_button.draw():
                print("return score portion")
                return score


        #load question
        if game_over == 0:
            questions[questionnum].draw()

        #draw button
        if questionbuttonlist1[questionnum].draw() == True and game_over == 0:
            currentanswer = answers[questionnum]
            if currentanswer == reorderQlist[questionnum][1]:
                score += 1
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    player.attack(enemies)
                    action_cd = 0
            else:
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    enemies.attack(player)
                    action_cd = 0
            questionnum += 1
            if questionnum >= len(question_list):
                if score >= passingmark:
                    enemies.hp = 0
                    enemies.alive = False
                    enemies.death()
                else:
                    player.hp = 0
                    player.alive = False
                    player.death()

        if questionbuttonlist2[questionnum].draw() == True and game_over == 0:
            currentanswer = answers[questionnum]
            if currentanswer == reorderQlist[questionnum][2]:
                score += 1
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    player.attack(enemies)
                    action_cd = 0
            else:
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    enemies.attack(player)
                    action_cd = 0
            questionnum += 1
            if questionnum >= len(question_list):
                if score >= passingmark:
                    enemies.hp = 0
                    enemies.alive = False
                    enemies.death()
                else:
                    player.hp = 0
                    player.alive = False
                    player.death()

        if questionbuttonlist3[questionnum].draw() == True and game_over == 0:
            currentanswer = answers[questionnum]
            if currentanswer == reorderQlist[questionnum][3]:
                score += 1
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    player.attack(enemies)
                    action_cd = 0
            else:
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    enemies.attack(player)
                    action_cd = 0
            questionnum += 1
            if questionnum >= len(question_list):
                if score >= passingmark:
                    enemies.hp = 0
                    enemies.alive = False
                    enemies.death()

                else:
                    player.hp = 0
                    player.alive = False
                    player.death()

        if questionbuttonlist4[questionnum].draw() == True and game_over == 0:
            currentanswer = answers[questionnum]
            if currentanswer == reorderQlist[questionnum][4]:
                score += 1
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    player.attack(enemies)
                    action_cd = 0
            else:
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    enemies.attack(player)
                    action_cd = 0
            questionnum += 1
            if questionnum >= len(question_list):
                if score >= passingmark:
                    enemies.hp = 0
                    enemies.alive = False
                    enemies.death()
                else:
                    player.hp = 0
                    player.alive = False
                    player.death()


        if abandon_button.draw() == True and game_over == 0:
            pause()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        
    pygame.quit()
    

#define button
#button class
class button():
    # colours for button and text
    button_col = (229, 229, 229)
    hover_col = (153, 153, 153)
    click_col = (191, 191, 191)
    text_col = black


    def __init__(self, x, y,width,height, text):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height

    def draw(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y+5))
        return action

Game("math",2,"male","Alex")