import pygame
from sys import exit
from random import randint, choice
import os
import sys

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('MathBlasters')
clock = pygame.time.Clock()
base_font = pygame.font.Font('font/Pixeltype.ttf', 50)
user_text = ''
game_active = True
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)	
registration_page = pygame.image.load('Image/Registration.png').convert()

#input box for user input
#140 pixels wide, 32 pixels height
input_rect1 = pygame.Rect(450, 235, 180, 28)
input_rect2 = pygame.Rect(450, 285, 180, 28)
input_rect3 = pygame.Rect(450, 325, 180, 28)
input_rect4 = pygame.Rect(450, 375, 180, 28)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect1.collidepoint(event.pos):
                active = True
            else:
                active = False

        #check if any event was pressed 
        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            # else if event.key == pygame.K_ENTER:
                
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

    if game_active:
        screen.blit(registration_page, (0,0))
        color = color_active

    else:
        color = color_passive
                
    # draw rectangle and argument passed which should
    # be on screen
    for i in range(1, 5, 1):
        current_input_rect = 'input_rect%s' %i
        pygame.draw.rect(screen, color, current_input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect1.x+5, input_rect1.y+5))
    
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect1.w = max(180, text_surface.get_width()+10)

    pygame.display.update()
    clock.tick(60)


