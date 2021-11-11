import pygame
import os

class Sky(pygame.sprite.Sprite):
    def __init__(self, xpos):
        super().__init__()
        self.xpos = xpos
        # image imports
        # portal_image = pygame.image.load('graphics/Sky.png').convert_alpha()
        quest_house_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Sky.png')).convert_alpha()
        self.image = portal_image
        self.rect = self.image.get_rect(midbottom=(xpos, 400))

    def change_xpos(self, change):
        self.xpos += change
        self.rect = self.image.get_rect(midbottom=(self.xpos, 400))
