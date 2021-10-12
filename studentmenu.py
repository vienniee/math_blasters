import pygame
import pygame.freetype
import random

pygame.init()

#create display window
SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#load background image
background_surface = pygame.image.load('image\level_select.png').convert()

#load button images
play_img = pygame.image.load('Image/button.png').convert_alpha()
achievements_img = pygame.image.load('Image/button.png').convert_alpha()
leaderboard_img = pygame.image.load('Image/button.png').convert_alpha()

#load fonts
#font style and size
font1 = pygame.font.Font(None,18)
font2 = pygame.font.Font(None,35)
menu1text = font1.render("PLAY", True, [0,0,0])
menu2text = font1.render("ACHIEVEMENTS", True,[0,0,0])
menu3text = font1.render("LEADERBOARD", True,[0,0,0])
menuheading = font2.render("STUDENT MAIN MENU", True,[0,0,0])


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
play_button = Button(258,220,play_img,2.5)
achievements_button = Button(408,220,achievements_img,2.5)
leaderboard_button = Button(558,220,leaderboard_img,2.5)


#game loop
run = True
while run:
    screen.fill((202, 228, 241))
    screen.blit(background_surface, (0, 0))

    #menu option select 
    if play_button.draw() == True:
        print('play selected')
    if achievements_button.draw() == True:
        print('achievements selected')
    if leaderboard_button.draw() == True:
        print('leaderboard selected')

    screen.blit(menuheading, (373,200))
    screen.blit(menu1text, (315,390))
    screen.blit(menu2text, (465,390))
    screen.blit(menu3text, (615,390))

    
    

    #event handler
    for event in pygame.event.get():
        #quit game 
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
