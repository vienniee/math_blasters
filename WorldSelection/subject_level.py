import pygame
from pygame.transform import rotozoom
import os
from WorldSelection.Portal import Portal
from WorldSelection.PortalText import PortalText

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self,screen):
        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

def load_assets():
    # group sprite
    exitButtonImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "quest", 'backButton.png')).convert_alpha()

    exitButton = Button(940,50,exitButtonImage,1)

    portal = pygame.sprite.Group()
    portal.add(Portal(400,2))
    portal.add(Portal(800,3))

    portal_names = pygame.sprite.Group()
    portal_names.add(PortalText(400, "MATH"))
    portal_names.add(PortalText(800, "SCIENCE"))

    return portal,portal_names,exitButton


def subject_selection(player,screen,portal,portal_names,exitButton):
    portal.draw(screen)
    portal_names.draw(screen)
    exitButton.draw(screen)

    # draw player
    player.draw(screen)
    player.update()
