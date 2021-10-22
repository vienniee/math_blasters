import pygame
from Castle import Castle
from Portal import Portal
from CastleText import CastleText


def load_assets(chap_1, chap_1_level, chap_2, chap_2_level):
    # group sprite
    castles = pygame.sprite.Group()
    castles.add(Castle(400, chap_1_level, chap_1))
    castles.add(Castle(800, chap_2_level, chap_2))

    castlesNames = pygame.sprite.Group()
    castlesNames.add(CastleText(400, chap_1))
    castlesNames.add(CastleText(800, chap_2))

    backPortal = pygame.sprite.GroupSingle()
    backPortal.add(Portal(100))

    return castles,castlesNames,backPortal

# def load_backPortal():
#     backPortal = pygame.sprite.GroupSingle()
#     backPortal.add(Portal(100))


#     return backPortal


def chapter_selection(player,screen, castles, castleName, backPortal):
    castles.draw(screen)
    castleName.draw(screen)
    backPortal.draw(screen)
    player.draw(screen)

    player.update()


