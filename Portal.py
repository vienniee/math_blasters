import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self,xpos):
        super().__init__()
        # image imports
        portal_image = pygame.image.load('graphics/portal.png').convert_alpha()
        self.image = portal_image
        self.rect = self.image.get_rect(midbottom=(xpos, 400))
