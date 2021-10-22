import pygame
from sys import exit
from Player import Player
from subject_level import load_assets as load_assets_subject, subject_selection
from chapter_level import load_assets as load_assets_chapter, chapter_selection,check_backportal,check_castles
from enum import Enum


def subject_Chapter_selection(character_gender):
    class States(Enum):
        SUBJECT_LEVEL = 1
        MATH_SUBJ = 2
        SCI_SUBJ = 3

    def collision_sprite(group):
        if pygame.sprite.spritecollide(player.sprite,group,False):
            return True
        else:
            return False



    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("CZ3003 pygame")
    test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

    state = States.SUBJECT_LEVEL

    # load sky
    sky_surface = pygame.image.load('graphics/Sky.png').convert()
    ground_surface = pygame.image.load('graphics/ground.png').convert()

    sky_surface = pygame.transform.rotozoom(sky_surface, 0, 1.5)
    ground_surface = pygame.transform.rotozoom(ground_surface, 0, 1.5)

    player = pygame.sprite.GroupSingle()
    player.add(Player(character_gender))

    portals, portal_names = load_assets_subject()
    math_castles, math_castleName, math_backPortal = load_assets_chapter(
        "Fractions",2, "Algebra",3)
    sci_castles, sci_castleName, sci_backPortal = load_assets_chapter(
        "Science1",1, "Science2",3)

    teleportCooldownState = False
    teleportCooldownTimer = pygame.USEREVENT + 1


    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if(event.type) == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == teleportCooldownTimer:
                teleportCooldownState = False
                pygame.time.set_timer(teleportCooldownTimer, 0)
                print("teleportCooldownState False")

            if state == States.SUBJECT_LEVEL:
                
                if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and collision_sprite(portals):
                    print("teleport to chapter")
                    print(portal_names)
                    # state = States.CHAPTER_LEVEL
                    hits = pygame.sprite.spritecollide(
                        player.sprite, portals, False)
                    # print(hits)
                    for portal in hits:
                        print(portal.return_subject())
                    
                    if portal.return_subject() == 2:
                        state = States(2)
                    elif portal.return_subject() == 3:
                        state = States(3)
                    player.sprite.rect.x = 100


                    teleportCooldownState = True
                    pygame.time.set_timer(teleportCooldownTimer, 1000)
                    print("teleportCooldownState True")

            if state == States.MATH_SUBJ:
                if check_backportal(keys, math_backPortal, teleportCooldownState,player):
                    state = States.SUBJECT_LEVEL
                    teleportCooldownState = True

                if check_castles(keys, math_castles, teleportCooldownState, player) and state == States.MATH_SUBJ:
                    hits = pygame.sprite.spritecollide(
                        player.sprite, math_castles, False)
                    for castle in hits:
                        return castle.returnChapter()

            if state == States.SCI_SUBJ:

                if check_backportal(keys, sci_backPortal, teleportCooldownState,player):
                    state = States.SUBJECT_LEVEL
                    teleportCooldownState = True
                

                if check_castles(keys, sci_castles, teleportCooldownState, player) and state == States.SCI_SUBJ:
                    hits = pygame.sprite.spritecollide(
                        player.sprite, sci_castles, False)
                    for castle in hits:
                        return castle.returnChapter()


        

        # draw the screen background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 400))

        if state == States.SUBJECT_LEVEL:
            subject_selection(player= player, screen=screen, portal=portals,portal_names=portal_names)
        elif state == States.MATH_SUBJ:
            chapter_selection(player=player, screen=screen, castles=math_castles,
                              castleName=math_castleName, backPortal=math_backPortal)
        elif state == States.SCI_SUBJ:
            chapter_selection(player=player, screen=screen, castles=sci_castles,
                            castleName=sci_castleName, backPortal=sci_backPortal)
        print(state)
        print(teleportCooldownState)
        pygame.display.update()
        clock.tick(60)


subject_Chapter_selection("female")
