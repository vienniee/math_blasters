import pygame
import os

class Portal(pygame.sprite.Sprite):
    def __init__(self,xpos,subject):
        super().__init__()
        self.xpos = xpos
        # image imports
        # portal_image = pygame.image.load('graphics/portal.png').convert_alpha()
        portal_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'portal.png')).convert_alpha()
        self.subject = subject
        self.image = portal_image
        self.rect = self.image.get_rect(midbottom=(xpos, 400))

    def return_subject(self):
        print(self.subject)
        return self.subject

    def change_xpos(self, change):
        self.xpos += change
        self.rect = self.image.get_rect(midbottom=(self.xpos, 400))
