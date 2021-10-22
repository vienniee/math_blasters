import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self,xpos,subject):
        super().__init__()
        # image imports
        portal_image = pygame.image.load('graphics/portal.png').convert_alpha()
        self.subject = subject
        self.image = portal_image
        self.rect = self.image.get_rect(midbottom=(xpos, 400))

    def return_subjec(self):
        print(self.subject)
        return self.subject
