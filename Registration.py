import pygame
from sys import exit
from random import randint, choice
import os
import sys

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('MathBlasters')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)	
registration_page = pygame.image.load('Image/Registration.png').convert()
registration_page = pygame.transform.scale(registration_page , (int(registration_page .get_width()*1),int(registration_page .get_height()*1)))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                pygame.quit()
                exit()

        if game_active:
            screen.blit(registration_page, (0,0))


        pygame.display.update()
        clock.tick(60)

game_loop()

    