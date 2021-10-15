import pygame
from Castle import Castle
from Portal import Portal
from CastleText import CastleText

def load_assets():
    # group sprite
    castles = pygame.sprite.Group()
    castles.add(Castle(400,1,"Algebra"))
    castles.add(Castle(800,2,"Fractions"))

    castlesNames = pygame.sprite.Group()
    castlesNames.add(CastleText(400,"Algebra"))
    castlesNames.add(CastleText(800,"Fractions"))

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


