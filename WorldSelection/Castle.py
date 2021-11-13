import pygame
import os

class Castle(pygame.sprite.Sprite):
    def __init__(self, xpos,level,chapter):
        super().__init__()
        # image imports
        self.xpos = xpos
        chapter = chapter.lower()
        if int(level) == 1:
            
            castle_image = pygame.image.load(os.path.join(os.path.dirname(
                __file__),  "castle", "castle_level1.png")).convert_alpha()
            castle_image = pygame.transform.rotozoom(castle_image, 0, 5)
        elif int(level) == 2:
            castle_image = pygame.image.load(os.path.join(os.path.dirname(
                __file__), "castle", "castle_level2.png")).convert_alpha()
            castle_image = pygame.transform.rotozoom(castle_image, 0, 5)
        elif int(level) == 3:
            castle_image = pygame.image.load(os.path.join(os.path.dirname(
                __file__),  "castle", "castle_level3.png")).convert_alpha()
            castle_image = pygame.transform.rotozoom(castle_image, 0, 5)
        
        self.chapter= chapter
        self.image = castle_image
        self.rect = self.image.get_rect(midbottom=(xpos, 400))

    def change_xpos(self,change):
        self.xpos += change
        self.rect = self.image.get_rect(midbottom=(self.xpos, 400))


    def returnChapter(self):
        print(self.chapter)
        return self.chapter
