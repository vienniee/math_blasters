
import pygame, sys,importlib
import DatabaseControllers.FirebaseConfig as firebaseDatabase
from pygame.locals import *
import assets as assets
import shelve
import characterSelect as characterselect
import os

def Registration():
    mainClock = pygame.time.Clock()
    pygame.init()

    h = 600    
    w = 1000

    # But more customization possible: Pass your own font object
    font = pygame.font.SysFont("Consolas", 24)
    # Create own manager with custom input validator

    white = (255, 255, 255)
    black = (0, 0, 0)
    slategrey = (112,128,144)

    SAVE_DATA = shelve.open("Save Data")
    SAVE_DATA['email'] = ""
    SAVE_DATA['password'] = ""
    SAVE_DATA['name'] = ""
    SAVE_DATA['classNum'] = ""
    screen = pygame.display.set_mode((w,h))

    name = ""
    email = ""
    classNum = ""
    password = ""
    nameActive = False
    emailActive = False
    classNumActive = False
    passwordActive = False

    running = True
    background_img = pygame.image.load("Registration/background.png").convert()
    registrationImage = pygame.image.load("Registration/img0.png").convert_alpha()
    back_img = pygame.image.load("Registration/backButton.png").convert_alpha()

    
    def backButton_clicked():
        print("Back Button Clicked")

    def signup(name, email, classNum, password):
        try:
            print("Registering...")
            print(email)
            print(password)
            user = firebaseDatabase.auth.create_user_with_email_and_password(email, password)
            uuid = user['localId']
            print(uuid)
            os.environ['USER'] = uuid
            STUDENT_DATA={}
            STUDENT_DATA['email']= email
            STUDENT_DATA['name']= name
            STUDENT_DATA['classNum']= classNum
            print("Successfully created!")
            characterselect.characterSelect(STUDENT_DATA)
        except Exception as e:
            print(e)
                        

           
    while running:
        screen.blit(background_img, (0, 0))
        
        btn_registration = assets.Button(screen=screen,id='buttonRegistration',image=registrationImage,scale=1,x=388,y=402)
        backButton = assets.Button(screen=screen,id='buttonRegistration',image=back_img,scale=1,x=20,y=20)
        nameSurface = font.render(name, True, black)
        emailSurface = font.render(email, True, black)
        classNumSurface = font.render(classNum, True, black)
        passwordSurface = font.render('*'*len(password), True, black)
        # Create the border around the text box with .Rect
        # left, top, width, height

        nameBorder = pygame.Rect(((w - nameSurface.get_width()) / 2) +25, h * .36,
                                     nameSurface.get_width() + 10, 30)
        emailBorder = pygame.Rect(((w - emailSurface.get_width()) / 2) +25, h * .44,
                                     emailSurface.get_width() + 10, 30)                             
        classNumBorder = pygame.Rect(((w - classNumSurface.get_width()) / 2) +25, h * .52,
                                     classNumSurface.get_width() + 10, 30)
        passwordBorder = pygame.Rect(((w - passwordSurface.get_width()) / 2) +25, h * .6,
                                     passwordSurface.get_width() + 10, 30)
        # This is the text surface when the user types in their name
        screen.blit(nameSurface, ((w - nameSurface.get_width()) / 2 +25, h * .36))
        screen.blit(emailSurface, ((w - emailSurface.get_width()) / 2 +25, h * .44))
        screen.blit(classNumSurface, ((w - classNumSurface.get_width()) / 2 +25, h * .52))
        screen.blit(passwordSurface, ((w - passwordSurface.get_width()) / 2 +25, h * .6))  
        for event in pygame.event.get():
           
            if btn_registration.draw():
                signup(SAVE_DATA['name'], SAVE_DATA['email'], SAVE_DATA['classNum'], SAVE_DATA['password'])
                
            if backButton.draw():
                backButton_clicked()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Mouse and Keyboard events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nameBorder.collidepoint(event.pos):
                    nameActive = True
                elif emailBorder.collidepoint(event.pos):
                    emailActive = True
                elif classNumBorder.collidepoint(event.pos):
                    classNumActive = True
                elif passwordBorder.collidepoint(event.pos):
                    passwordActive = True
                else:
                    nameActive = False
                    emailActive = False
                    classNumActive = False
                    passwordActive = False

            if event.type == pygame.KEYDOWN:
                if nameActive:
                    emailActive = False
                    classNumActive = False
                    passwordActive = False
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
                if emailActive:
                    nameActive = False
                    classNumActive = False
                    passwordActive = False
                    if event.key == pygame.K_BACKSPACE:
                        email = email[:-1]
                    else:
                        email += event.unicode
                if classNumActive:
                    nameActive = False
                    emailActive = False
                    passwordActive = False
                    if event.key == pygame.K_BACKSPACE:
                        classNum = classNum[:-1]
                    else:
                        classNum += event.unicode
                if passwordActive:
                    nameActive = False
                    emailActive = False
                    classNumActive = False
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode        

        if nameActive:
            pygame.draw.rect(screen, white, nameBorder, 1)
        else:
            pygame.draw.rect(screen, slategrey, nameBorder, 2)
        if emailActive:
            pygame.draw.rect(screen, white, emailBorder, 1)
        else:
            pygame.draw.rect(screen, slategrey, emailBorder, 2)
        if classNumActive:
            pygame.draw.rect(screen, white, classNumBorder, 1)
        else:
            pygame.draw.rect(screen, slategrey, classNumBorder, 2)    
        if passwordActive:
            pygame.draw.rect(screen, white, passwordBorder, 1)
        else:
            pygame.draw.rect(screen, slategrey, passwordBorder, 2)    

        if btn_registration:
            if email != "":
                email = email
                SAVE_DATA['email'] = email
            else:
                pass
            if password != "":
                password = password
                SAVE_DATA['password'] = password
            else:
                pass
            if name != "":
                name = name
                SAVE_DATA['name'] = name
            else:
                pass
            if classNum != "":
                classNum = classNum
                SAVE_DATA['classNum'] = classNum
            else:
                pass
           
        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    Registration()



    
        

    
    

