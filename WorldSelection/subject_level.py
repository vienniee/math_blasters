import pygame
from pygame.transform import rotozoom

from WorldSelection.Portal import Portal
from WorldSelection.PortalText import PortalText


def load_assets():
    # group sprite
    portal = pygame.sprite.Group()
    portal.add(Portal(300,2))
    portal.add(Portal(800,3))

    portal_names = pygame.sprite.Group()
    portal_names.add(PortalText(300, "MATH"))
    portal_names.add(PortalText(800, "SCIENCE"))

    return portal,portal_names


def subject_selection(player,screen,portal,portal_names):
    portal.draw(screen)
    portal_names.draw(screen)

    # draw player
    player.draw(screen)
    player.update()
