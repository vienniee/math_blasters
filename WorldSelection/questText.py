import pygame
import os
class QuestText(pygame.sprite.Sprite):
    def __init__(self, text, ypos):
        super().__init__()

        test_font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'font', 'Pixeltype.ttf'), 40)
        questText = test_font.render(str(text), False, (0, 0, 0))
        self.image = questText
        self.rect = self.image.get_rect(center=(500, ypos))
