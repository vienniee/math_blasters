import pygame, sys

# from pyrebase.pyrebase import Firebase

import shelve
import os

# from firebase import FirebaseDatabase


# if __name__ == '__main__':
    # if __package__ is None:
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from DatabaseControllers.StudentDB import StudentDB
from DatabaseControllers import firebase 
from Login import assets
    # else:
        # from ..DatabaseControllers.StudentDB import StudentDB
        # from DatabaseControllers import firebase as fb
        # import assets
        
      


# from teacherDashboard import main_menu
# from studentmenu import studentMenu

def LoginUser():
    mainClock = pygame.time.Clock()
    pygame.init()

    h = 600    
    w = 1000

    # But more customization possible: Pass your own font object
    font = pygame.font.SysFont("Consolas", 24)
    # Create own manager with custom input validator

    isLoginError = False
    white = (255, 255, 255)
    black = (0, 0, 0)
    slategrey = (112,128,144)

    SAVE_DATA = shelve.open("Save Data")
    SAVE_DATA['email'] = ""
    SAVE_DATA['password'] = ""
    FirebaseDatabase = firebase.FirebaseDatabase()
    screen = pygame.display.set_mode((w,h))

    email = ""
    password = ""
    emailActive = False
    passwordActive = False

    running = True
    background_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'login_images', 'background.png')).convert()
    loginImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'login_images', 'img0.png')).convert_alpha()
    registrationImage = pygame.image.load(
        os.path.join(os.path.dirname(__file__), 'login_images', 'img1.png')).convert_alpha()

    
    def register_clicked():
        print("Register Clicked")
        return True
        
    
    def login(email, password):
        
        try:
            print("Logging in")
            # print(password)
            if password != "":
                # print("ABCDE")
                result = FirebaseDatabase.auth.sign_in_with_email_and_password(email, password)
                # print(result)
                # print("FGHJK")
                if result['email']:
                    studentDB = StudentDB()
                    studentList =  studentDB.get_student()
                    studentFound = False
                    for key in studentList:
                        if studentList[key]["email"] == email:
                            studentFound = True
                            gender=studentList[key]["character"]
                            print("Successfully logged in for student!")
                            break
                    if studentFound == True:
                        # studentMenu()
                        print("go to Student Main Menu")
                        return 2, key, gender
                    else: 
                        # main_menu()
                        print("go to Teacher Main Menu")
                        return 3, None, None
            else:
                print("Invalid email or password")
                
                
                # test_font = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'font', 'Pixeltype.ttf'), 50)
                # invalid_login_text = test_font.render("Invalid Email/Password", False, (0, 0, 0))
                # # invalidLogin = font.render("Invalid Email/Password", True, (255,255,255))
                # screen.blit(invalid_login_text, (100, 100))
                return 4, None, None
        except:
            print("Invalid email or password")
            
            
            return 4, None, None

    while running:
        screen.blit(background_img, (0, 0))
        btn_login = assets.Button(screen=screen,id='buttonLogin',image=loginImage,scale=1,x=500,y=338)
        btn_registration = assets.Button(screen=screen,id='buttonRegistration',image=registrationImage,scale=1,x=340,y=348)
       
        emailSurface = font.render(email, True, black)
        passwordSurface = font.render('*'*len(password), True, black)
        # Create the border around the text box with .Rect
        # left, top, width, height
        emailBorder = pygame.Rect(((w - emailSurface.get_width()) / 2) +25, h * .42,
                                     emailSurface.get_width() + 10, 30)
        passwordBorder = pygame.Rect(((w - passwordSurface.get_width()) / 2) +25, h * .5,
                                     passwordSurface.get_width() + 10, 30)
        # This is the text surface when the user types in their name
        screen.blit(emailSurface, ((w - emailSurface.get_width()) / 2 +25, h * .42))
        screen.blit(passwordSurface, ((w - passwordSurface.get_width()) / 2 +25, h * .5))  
        #Printing login status on the screen
        # assets.create_text(screen,TEXT_OPTION,assets.SMALL_FONT,assets.COLOR_BLACK,330,100)

        for event in pygame.event.get():
            if btn_registration.draw():
                if register_clicked():
                    return 1, 0, None

            if btn_login.draw():
                print(SAVE_DATA['email'])
                print(SAVE_DATA['password'])
                a,b,gender = login(SAVE_DATA['email'], SAVE_DATA['password'])
                print(a, b)
                if a!=4:
                    return a,b,gender
                else:
                    isLoginError = True
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Mouse and Keyboard events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if emailBorder.collidepoint(event.pos):
                    emailActive = True
                    passwordActive = False

                elif passwordBorder.collidepoint(event.pos):
                    passwordActive = True
                    emailActive = False
                else:
                    emailActive = False
                    passwordActive = False

            if event.type == pygame.KEYDOWN:
                if emailActive:
                    passwordActive = False
                    if event.key == pygame.K_BACKSPACE:
                        email = email[:-1]
                    else:
                        email += event.unicode
                if passwordActive:
                    emailActive = False
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode        

        if emailActive:
            pygame.draw.rect(screen, white, emailBorder, 1)
        else:
            pygame.draw.rect(screen, slategrey, emailBorder, 2)

        if passwordActive:
            pygame.draw.rect(screen, white, passwordBorder, 1)
        else:
            pygame.draw.rect(screen, slategrey, passwordBorder, 2)    

   

        if btn_login:
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
        # print(isLoginError)
        if isLoginError:
            test_font = pygame.font.Font(os.path.join(
                os.path.dirname(__file__), 'font', 'Pixeltype.ttf'), 30)
            invalid_login_text = test_font.render(
                "Invalid Email/Password", False, (255, 0, 0))
            screen.blit(invalid_login_text, (400, 225))

           
        pygame.display.update()
        mainClock.tick(60)