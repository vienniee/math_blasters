import pygame
from sys import exit
from WorldSelection.Player import Player
from WorldSelection.subject_level import load_assets as load_assets_subject, subject_selection
from WorldSelection.chapter_level import load_assets as load_assets_chapter, chapter_selection,check_backportal,check_castles,check_quest_house
from WorldSelection.Quest_Select_Modal import load_asset as load_assets_quest, quest_selection
from enum import Enum
import os

class States(Enum):
        SUBJECT_LEVEL = 1
        MATH_SUBJ = 2
        SCI_SUBJ = 3
        QUEST_SELECT = 4

def subject_Chapter_selection(character_gender):
    

    def collision_sprite(group):
        if pygame.sprite.spritecollide(player.sprite,group,False):
            return True
        else:
            return False



    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("CZ3003 pygame")
    # test_font = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'Pixeltype.ttf', 50))
    

    state = States.SUBJECT_LEVEL

   #load sky
    
    sky_surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Sky.png')).convert_alpha()
    ground_surface = pygame.image.load(os.path.join(os.path.dirname(__file__),  'ground.png')).convert_alpha()


    

    sky_surface = pygame.transform.rotozoom(sky_surface, 0, 1.5)
    sky_pos = [0,0]
    ground_surface = pygame.transform.rotozoom(ground_surface, 0, 1.5)
    ground_pos = [0,400]

    player = pygame.sprite.GroupSingle()
    player.add(Player(character_gender))

    portals, portal_names = load_assets_subject()
    math_castles, math_castleName, math_backPortal, math_questHouse = load_assets_chapter(
        "Fractions",2, "Algebra",3)
    sci_castles, sci_castleName, sci_backPortal, sci_questHouse = load_assets_chapter(
        "Science1",1, "Science2",3)

    teleportCooldownState = False
    teleportCooldownTimer = pygame.USEREVENT + 1


    while True:
        keys = pygame.key.get_pressed()

        if state == States.MATH_SUBJ:

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                LEFT_X_CHANGE = -2

                if(sky_pos[0] == -800):
                    pass
                else:
                    print(sky_pos[0])
                    sky_pos[0] += LEFT_X_CHANGE
                    ground_pos[0] += LEFT_X_CHANGE

                    for castle in math_castles:
                        castle.change_xpos(LEFT_X_CHANGE)

                    for castle_text in math_castleName:
                        castle_text.change_xpos(LEFT_X_CHANGE)

                    for portal in math_backPortal:
                        portal.change_xpos(LEFT_X_CHANGE)
                    
                    for questHouse in math_questHouse:
                        questHouse.change_xpos(LEFT_X_CHANGE)

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                RIGHT_X_CHANGE = 2
                if(sky_pos[0] == 0):
                    pass
                else:
                    sky_pos[0] += RIGHT_X_CHANGE
                    ground_pos[0] += RIGHT_X_CHANGE

                    for castle in math_castles:
                        castle.change_xpos(RIGHT_X_CHANGE)

                    for castle_text in math_castleName:
                        castle_text.change_xpos(RIGHT_X_CHANGE)

                    for portal in math_backPortal:
                        portal.change_xpos(RIGHT_X_CHANGE)
                    
                    for questHouse in math_questHouse:
                        questHouse.change_xpos(RIGHT_X_CHANGE)
        
        if state == States.SCI_SUBJ:

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                LEFT_X_CHANGE = -2

                if(sky_pos[0] == -800):
                    pass
                else:
                    sky_pos[0] += LEFT_X_CHANGE
                    ground_pos[0] += LEFT_X_CHANGE

                    for castle in sci_castles:
                        castle.change_xpos(LEFT_X_CHANGE)

                    for castle_text in sci_castleName:
                        castle_text.change_xpos(LEFT_X_CHANGE)

                    for portal in sci_backPortal:
                        portal.change_xpos(LEFT_X_CHANGE)
                    
                    for questHouse in sci_questHouse:
                        questHouse.change_xpos(LEFT_X_CHANGE)

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                RIGHT_X_CHANGE = 2
                if(sky_pos[0] == 0):
                    pass
                else:
                    sky_pos[0] += RIGHT_X_CHANGE
                    ground_pos[0] += RIGHT_X_CHANGE

                    for castle in sci_castles:
                        castle.change_xpos(RIGHT_X_CHANGE)

                    for castle_text in sci_castleName:
                        castle_text.change_xpos(RIGHT_X_CHANGE)

                    for portal in sci_backPortal:
                        portal.change_xpos(RIGHT_X_CHANGE)
                    
                    for questHouse in sci_questHouse:
                        questHouse.change_xpos(RIGHT_X_CHANGE)


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
                        quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton = load_assets_quest("math")

                    elif portal.return_subject() == 3:
                        state = States(3)
                        quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton = load_assets_quest("science")
                    player.sprite.rect.x = 100


                    teleportCooldownState = True
                    pygame.time.set_timer(teleportCooldownTimer, 3000)
                    print("teleportCooldownState True")

            if state == States.MATH_SUBJ:
                if check_backportal(keys, math_backPortal, teleportCooldownState,player):
                    state = States.SUBJECT_LEVEL
                    teleportCooldownState = True

                if check_castles(keys, math_castles, teleportCooldownState, player):
                    hits = pygame.sprite.spritecollide(
                        player.sprite, math_castles, False)
                    for castle in hits:
                        return castle.returnChapter()
                
                if check_quest_house(keys, math_questHouse, teleportCooldownState, player):
                    state = States.QUEST_SELECT
                    print("questHouse Hit")
                
                

            if state == States.SCI_SUBJ:
                if check_backportal(keys, sci_backPortal, teleportCooldownState,player):
                    state = States.SUBJECT_LEVEL
                    teleportCooldownState = True
                

                if check_castles(keys, sci_castles, teleportCooldownState, player):
                    hits = pygame.sprite.spritecollide(
                        player.sprite, sci_castles, False)
                    for castle in hits:
                        return castle.returnChapter()

                if check_quest_house(keys, sci_questHouse, teleportCooldownState, player):
                    state = States.QUEST_SELECT
                    print("questHouse Hit")
                


        

        # draw the screen background
        screen.blit(sky_surface, (sky_pos[0], sky_pos[1]))
        screen.blit(ground_surface, (ground_pos[0], ground_pos[1]))
        screen.blit(sky_surface, (sky_pos[0]+800, sky_pos[1]))
        screen.blit(ground_surface, (ground_pos[0]+800, ground_pos[1]))

        if state == States.SUBJECT_LEVEL:
            subject_selection(player= player, screen=screen, portal=portals,portal_names=portal_names)
        elif state == States.MATH_SUBJ:
            chapter_selection(player=player, screen=screen, castles=math_castles,
                              castleName=math_castleName, backPortal=math_backPortal, questHouse=math_questHouse)
        elif state == States.SCI_SUBJ:
            chapter_selection(player=player, screen=screen, castles=sci_castles,
                            castleName=sci_castleName, backPortal=sci_backPortal, questHouse=sci_questHouse)
        elif state == States.QUEST_SELECT:
            quest_selection(screen=screen,quest_menu = quest_menu, Quest1=Quest1,Quest2=Quest2,Quest3=Quest3,prevButton=prevButton,nextButton=nextButton,backButton=backButton)
        # print(state)
        # print(teleportCooldownState)
        pygame.display.update()
        clock.tick(60)


