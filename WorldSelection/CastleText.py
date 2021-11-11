import pygame
import os
class CastleText(pygame.sprite.Sprite):
    def __init__(self, xpos, text):
        self.xpos = xpos
        super().__init__()
        # image imports
        # test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
        test_font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'font', 'Pixeltype.ttf'), 50)
        portal_name = test_font.render(str(text), False, (0, 0, 0))
        self.image = portal_name
        self.rect = self.image.get_rect(midbottom=(xpos, 100))

    def change_xpos(self, change):
        self.xpos += change
        self.rect = self.image.get_rect(midbottom=(self.xpos, 100))
