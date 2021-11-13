import math
import pygame
from sys import exit
from WorldSelection.Player import Player
from WorldSelection.subject_level import load_assets as load_assets_subject, subject_selection
from WorldSelection.chapter_level import load_assets as load_assets_chapter, chapter_selection,check_backportal,check_castles,check_quest_house
from WorldSelection.Quest_Select_Modal import load_asset as load_assets_quest, quest_selection
from enum import Enum
import os
from DatabaseControllers.ScoresDB import ScoreDB

class States(Enum):
        SUBJECT_LEVEL = 1
        MATH_SUBJ = 2
        SCI_SUBJ = 3
        QUEST_SELECT = 4

def subject_Chapter_selection(character_gender,studentID):
    

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

    portals, portal_names,exitButton = load_assets_subject()

    score_db = ScoreDB()
    student_score = score_db.get_single_score(studentID)

    subject_level = {}

    try:

        for subject in student_score:
            for level in student_score[subject]:
                
                if student_score[subject][level] > 5:
                    if level == "level 1":
                        level = 1
                    elif level == "level 2":
                        level = 2
                    elif level == "level 3":
                        level = 3
                    if level == 3:
                        subject_level[subject] = level
                    else:
                        subject_level[subject] = level + 1
    except:
        print("student score not in database")
    if "fractions" not in subject_level:
        subject_level["fractions"] = 1
    if "algebra" not in subject_level:
        subject_level["algebra"] = 1
    if "physics" not in subject_level:   
        subject_level["physics"] = 1
    if "chemistry" not in subject_level:
        subject_level["chemistry"] = 1
                

    math_castles, math_castleName, math_backPortal, math_questHouse, math_exitButton = load_assets_chapter(
        "Fractions", subject_level["fractions"], "Algebra", subject_level["algebra"])
    sci_castles, sci_castleName, sci_backPortal, sci_questHouse, sci_exitButton = load_assets_chapter(
        "Physics", subject_level["physics"], "Chemistry", subject_level["chemistry"])

    teleportCooldownState = False
    teleportCooldownTimer = pygame.USEREVENT + 1
    currentdata = []
    current_page = 1
    

    while True:
        keys = pygame.key.get_pressed()

        if state == States.MATH_SUBJ:

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                LEFT_X_CHANGE = -2

                if(sky_pos[0] == -800):
                    pass
                else:
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

                pos = pygame.mouse.get_pos()
                if exitButton.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    print("go to student main menu")
                    return 4, None
                
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
                        subject_selected = "math"

                    elif portal.return_subject() == 3:
                        state = States(3)
                        subject_selected = "science"
                    player.sprite.rect.x = 100


                    teleportCooldownState = True
                    pygame.time.set_timer(teleportCooldownTimer, 3000)
                    print("teleportCooldownState True")

            if state == States.MATH_SUBJ:
                pos = pygame.mouse.get_pos()
                if math_exitButton.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    print("go to student main menu")
                    return 4, None

                if check_backportal(keys, math_backPortal, teleportCooldownState,player):
                    state = States.SUBJECT_LEVEL
                    teleportCooldownState = True

                if check_castles(keys, math_castles, teleportCooldownState, player):
                    hits = pygame.sprite.spritecollide(
                        player.sprite, math_castles, False)
                    for castle in hits:
                        return 1,castle.returnChapter() 
                
                if check_quest_house(keys, math_questHouse, teleportCooldownState, player):
                    state = States.QUEST_SELECT
                    quest_data, quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton = load_assets_quest("math",studentID)
                
                

            if state == States.SCI_SUBJ:
                pos = pygame.mouse.get_pos()
                if sci_exitButton.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    print("go to student main menu")
                    return 4, None

                if check_backportal(keys, sci_backPortal, teleportCooldownState,player):
                    state = States.SUBJECT_LEVEL
                    teleportCooldownState = True
                

                if check_castles(keys, sci_castles, teleportCooldownState, player):
                    hits = pygame.sprite.spritecollide(
                        player.sprite, sci_castles, False)
                    for castle in hits:
                        return 1,castle.returnChapter()

                if check_quest_house(keys, sci_questHouse, teleportCooldownState, player):
                    state = States.QUEST_SELECT
                    quest_data, quest_menu,Quest1,Quest2,Quest3,prevButton,nextButton,backButton = load_assets_quest("science",studentID)

            if state == States.QUEST_SELECT:
                
                total_pages = math.ceil(len(quest_data)/3)
                pos = pygame.mouse.get_pos()
                if backButton.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    if subject_selected == "math":
                        state = States.MATH_SUBJ
                    if subject_selected == "science":
                        state = States.SCI_SUBJ

                if prevButton.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    if(current_page == 1):
                        current_page = 1
                    else:
                        current_page -= 1
                if nextButton.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    if(current_page == total_pages):
                        current_page = total_pages
                    else:
                        current_page +=1
                
                if Quest1.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    return 0, currentdata[0] 
                    
                if Quest2.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    return 0, currentdata[1]
                if Quest3.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                    return 0, currentdata[2]
        

        # draw the screen background
        screen.blit(sky_surface, (sky_pos[0], sky_pos[1]))
        screen.blit(ground_surface, (ground_pos[0], ground_pos[1]))
        screen.blit(sky_surface, (sky_pos[0]+800, sky_pos[1]))
        screen.blit(ground_surface, (ground_pos[0]+800, ground_pos[1]))

        if state == States.SUBJECT_LEVEL:
            subject_selection(player= player, screen=screen, portal=portals,portal_names=portal_names,exitButton=exitButton)
        elif state == States.MATH_SUBJ:
            chapter_selection(player=player, screen=screen, castles=math_castles,
                              castleName=math_castleName, backPortal=math_backPortal, questHouse=math_questHouse, exitButton=math_exitButton)
        elif state == States.SCI_SUBJ:
            chapter_selection(player=player, screen=screen, castles=sci_castles,
                            castleName=sci_castleName, backPortal=sci_backPortal, questHouse=sci_questHouse, exitButton=sci_exitButton)
        elif state == States.QUEST_SELECT:
            currentdata = quest_selection(quest_data=quest_data,screen=screen,quest_menu = quest_menu, Quest1=Quest1,Quest2=Quest2,Quest3=Quest3,prevButton=prevButton,nextButton=nextButton,backButton=backButton,current_page=current_page)
        # print(state)
        # print(teleportCooldownState)
        pygame.display.update()
        clock.tick(60)


