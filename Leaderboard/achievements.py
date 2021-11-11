import pygame
import pygame.freetype

#Initialising pygame
pygame.init()

#create display window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

#create text for page
pygame.font.init()
myfont = pygame.font.SysFont('Pixeltype.ttf',30)
textsurface = myfont.render('Achievements', False, (0,0,0))

#create background image
background_image = pygame.image.load('Image/Standard_background.png').convert_alpha()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

#create on screen
screen.blit(background_image,(0,0))
screen.blit(textsurface,(440,20))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

pygame.quit()