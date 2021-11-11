import pygame
import os

class Quest_House(pygame.sprite.Sprite):
    def __init__(self,xpos):
        super().__init__()
        self.xpos = xpos
        # image imports
        # quest_house_image = pygame.image.load('graphics/quest/quest_house.png').convert_alpha()
        quest_house_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'quest', 'quest_house.png')).convert_alpha()
        self.image = quest_house_image
        self.rect = self.image.get_rect(midbottom=(xpos, 420))

    def change_xpos(self, change):
        self.xpos += change
        self.rect = self.image.get_rect(midbottom=(self.xpos, 420))