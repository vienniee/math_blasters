import pygame
import os
class Sky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image imports
        # quest_menu = pygame.image.load('graphics/Sky.png').convert_alpha()
        quest_menu = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Sky.png')).convert_alpha()

    


