import pygame
import pygame.freetype
import random

pygame.init()

#create display window
SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#load background image
sky_surface = pygame.image.load('image\sky1.png').convert()
ground_surface = pygame.image.load('image\ground1.png').convert()

#load button images
lvl1_img = pygame.image.load("image\Castle_level_1.png").convert_alpha()
lvl2_img = pygame.image.load("image\Castle_level_2.png").convert_alpha()
lvl3_img = pygame.image.load("image\Castle_level_3.png").convert_alpha()

lvl1_img_rect = lvl1_img.get_rect()
lvl2_img_rect = lvl1_img.get_rect()
lvl3_img_rect = lvl1_img.get_rect()

#load fonts
#font style and size
font = pygame.font.Font(None,18)
level1text = font.render("LEVEL 1", True, [0,0,0])
level2text = font.render("LEVEL 2", True,[0,0,0])
level3text = font.render("LEVEL 3", True,[0,0,0])


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

print(lvl1_img_rect)

#create button instances
level1_button = Button(160,150,lvl1_img,2.5)
level2_button = Button(310,150,lvl2_img,2.5)
level3_button = Button(460,150,lvl3_img,2.5)

#game loop
run = True
while run:
    screen.fill((202, 228, 241))
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    #difficulty select
    
    if level1_button.draw() == True:
        print('level 1')
    if level2_button.draw() == True:
        print('level 2')
    if level3_button.draw() == True:
        print('level 3')

    screen.blit(level1text, (215,320))
    screen.blit(level2text, (415,320))
    screen.blit(level3text, (615,320))

    
    

    #event handler
    for event in pygame.event.get():
        #quit game (need to change to back button instead)
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()



