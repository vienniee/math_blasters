import pygame
from Castle import Castle
from Portal import Portal
from CastleText import CastleText
from Quest_House import Quest_House


def load_assets(chap_1, chap_1_level, chap_2, chap_2_level):
    # group sprite
    castles = pygame.sprite.Group()
    castles.add(Castle(400, chap_1_level, chap_1))
    castles.add(Castle(800, chap_2_level, chap_2))

    castlesNames = pygame.sprite.Group()
    castlesNames.add(CastleText(400, chap_1))
    castlesNames.add(CastleText(800, chap_2))

    backPortal = pygame.sprite.GroupSingle()
    backPortal.add(Portal(100,1))

    castlesNames.add(CastleText(1200, "Quest"))
    questHouse = pygame.sprite.GroupSingle()
    questHouse.add(Quest_House(1200))

    return castles,castlesNames,backPortal,questHouse

# def load_backPortal():
#     backPortal = pygame.sprite.GroupSingle()
#     backPortal.add(Portal(100))


#     return backPortal


def chapter_selection(player,screen, castles, castleName, backPortal, questHouse):
    castles.draw(screen)
    castleName.draw(screen)
    backPortal.draw(screen)
    questHouse.draw(screen)
    player.draw(screen)

    player.update()


def check_backportal(keys, backportal, teleportCooldownstate, player):
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and collision_sprite(player,backportal) and not teleportCooldownstate:
        print("teleport to subject")
        return True
        

def check_castles(keys, castles, teleportCooldownstate, player):
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and collision_sprite(player, castles) and not teleportCooldownstate:
        print("teleport to chapter")
        return True

def check_quest_house(keys, questHouse, teleportCooldownstate, player):
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and collision_sprite(player, questHouse) and not teleportCooldownstate:
        print("go to quest select")
        return True





def collision_sprite(player,group):
        if pygame.sprite.spritecollide(player.sprite, group, False):
            return True
        else:
            return False
