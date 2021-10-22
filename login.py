import pygame, sys,importlib
import firebase as FB
from studentmenu import studentMenu
importlib.reload(sys.modules['firebase'])
from pygame.locals import *
import assets as assets
import shelve
from DatabaseControllers.StudentDB import StudentDB
from DatabaseControllers.TeacherDB import TeacherDB

from teacherDashboard import main_menu
from studentmenu import studentMenu

def Login():
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
    screen = pygame.display.set_mode((w,h))

    email = ""
    password = ""
    emailActive = False
    passwordActive = False

    running = True
    click = False
    background_img = pygame.image.load("Login/background.png").convert()
    loginImage = pygame.image.load("Login/img0.png").convert_alpha()
    registrationImage = pygame.image.load("Login/img1.png").convert_alpha()


    firebaseDatabase = FB.FirebaseDatabase()


    def register_clicked():
        print("Register Clicked")
        import Registration

    # def login(email, password):
    #     try:
    #         print("Logging in")
    #         result = firebaseDatabase.auth.sign_in_with_email_and_password(email, password)
    #         email1 = result["email"]
            
    #         teacherdb = TeacherDB()
    #         teacherList =  teacherdb.get_teacher()

    #         for teacher in teacherList:
    #             if teacher[email] == email1:
    #                 print("Successfully logged in!")
    #                 import teacherDashboard
    #             else:
    #                 print("Successfully logged in!")
    #                 import characterSelect
    #     except:
    #         print("Invalid email or password TRY AGAIN")
    #         invalidLogin = font.render("Invalid Email/Password", True, (255,255,255))
    #         screen.blit(invalidLogin, (100, 100))

    def login(email, password):
        try:
            print("Logging in")
            print(password)
            if password != "":
                result = firebaseDatabase.auth.sign_in_with_email_and_password(email, password)
                if result['email']:
                    studentDB = StudentDB()
                    studentList =  studentDB.get_student()
                    print(studentList)
                    studentFound = False
                    for key in studentList:
                        if studentList[key]["email"] == email:
                            studentFound = True
                            print("Successfully logged in for student!")
                            break
                    if studentFound == True:
                        studentMenu()
                    else: 
                        main_menu()
            
        except:
            print("Invalid email or password")
            invalidLogin = font.render("Invalid Email/Password", True, (255,255,255))
            screen.blit(invalidLogin, (100, 100))


    TEXT_OPTION=""
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
        assets.create_text(screen,TEXT_OPTION,assets.SMALL_FONT,assets.COLOR_BLACK,330,100)

        for event in pygame.event.get():
            if btn_registration.draw():
                register_clicked() 

            if btn_login.draw():
                print(SAVE_DATA['email'])
                print(SAVE_DATA['password'])
                login(SAVE_DATA['email'], SAVE_DATA['password'])
                
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Mouse and Keyboard events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if emailBorder.collidepoint(event.pos):
                    emailActive = True

                elif passwordBorder.collidepoint(event.pos):
                    passwordActive = True
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

           
        pygame.display.update()
        mainClock.tick(60)

if __name__ == '__main__':
    Login()



    
        

    
    

