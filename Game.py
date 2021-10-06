import pygame
import random
from random import randrange


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
font = pygame.font.SysFont('Times New Roman',26)

#define colours
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)

#load images
#background images
background_img = pygame.image.load('Image/castlebackground.png').convert_alpha()
#panel image
panel_img = pygame.image.load('Image/panel.png').convert_alpha()
#button image
button_img = pygame.image.load('Image/button.png').convert_alpha()

#define gaming variables
current_turn = 1
total_turn = 2
action_cd = 0
action_wait_time = 90
game_over = 0 # 1 means player win, -1 player lost

#function to draw text
def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))

#load question list
#sample, first digit is the passing score
#questions with 4 options, last is answer
questionlist = ["2",["1 + 1 - ?", "1", "2", "3", "4", "2"], ["2 + 2 = ?", "1", "2", "3", "4"],["3 + 3 = ?", "2", "4", "6", "8"]]
question_list = questionlist[1:]
print(randrange(len(question_list)))

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
print(orderlist)








#function to draw bg
def draw_bg():
    screen.blit(background_img,(-200,-bottom_panel))

#function to draw panel
def draw_pnl():
    screen.blit(panel_img,(0,screen_height-bottom_panel))
    #show stats
    draw_text(f'{player.name} HP:{player.hp}', font, red, 210, screen_height - bottom_panel + 5)
    draw_text(f'{enemies.name} HP:{enemies.hp}', font, red, 560, screen_height - bottom_panel + 5)

#define button
#button class
class Button():
    def __init__(self, x, y, image, wscale, hscale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *wscale),int(height*hscale)))
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
                #test check, remove when complete
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

#create button instances
option1_button = Button(20,470,button_img,0.55,0.175)
option2_button = Button(440,470,button_img,0.55,0.175)
option3_button = Button(20,530,button_img,0.55,0.175)
option4_button = Button(440,530,button_img,0.55,0.175)
abandon_button = Button(850,490,button_img,0.18,0.175)


#define player
class character():
    def __init__(self, x, y, name, max_hp,scale):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.alive = True
        self.animation_list = []
        self.frame_index= 0
        #in progress pending for pixel arts
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
player = character(280,310,'player',len(questionlist)-1,3.5)
enemies = character(650,310,'enemies',len(questionlist)-1,2.5)

player_hp = healthbar(210,screen_height-bottom_panel+40,player.hp,player.max_hp)
enemies_hp = healthbar(560,screen_height-bottom_panel+40,enemies.hp,enemies.max_hp)

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

    #draw and update character animation
    player.update()
    player.draw()
    enemies.update()
    enemies.draw()

    #damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    #draw button
    if option1_button.draw() == True:
        #button action ~ player
        if player.alive:
            if current_turn == 1:
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    player.attack(enemies)
                    current_turn = 2
                    action_cd = 0
        else:
            game_over = -1


    if option2_button.draw() == True:
        # button action ~ enemies
        if enemies.alive:
            if current_turn == 2:
                while action_cd < action_wait_time:
                    action_cd += 1
                if action_cd >= action_wait_time:
                    enemies.attack(player)
                    current_turn = 1
                    action_cd = 0
        else:
            game_over = 1


    if option3_button.draw() == True:
        print('C')
    if option4_button.draw() ==True:
        print('D')
    if abandon_button.draw() ==True:
        print('Abandon')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


