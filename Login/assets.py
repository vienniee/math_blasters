
import pygame, sys
import pygame_textinput

FONT = pygame.font.SysFont(None, 20)
SMALL_FONT = pygame.font.SysFont('Rowdies-Regular', 30)
BIG_FONT = pygame.font.SysFont('Corbel', 60)

COLOR_BLACK = "#000000"


class Button():
    def __init__(self,screen,id,image,scale,x, y):
        self.id = id
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    

    def draw(self):
        action = False
        #getting mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('clicked: {}'.format(self.id))
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

def create_text(screen,text, font, color, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)