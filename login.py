import pygame, sys,importlib
import firebase as FB
importlib.reload(sys.modules['firebase'])
from pygame.locals import *
import assets as assets
import shelve


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

screen = pygame.display.set_mode((w,h))

def Login():
    email = ""
    password = ""
    emailActive = False
    passwordActive = False

    running = True
    click = False
    background_img = pygame.image.load("Login/background.png").convert()
    loginImage = pygame.image.load("Login/studentLogin.png").convert_alpha()
    registrationImage = pygame.image.load("Login/Registration.png").convert_alpha()
    teacherLoginImage = pygame.image.load("Login/teacherLogin.png").convert_alpha()

    firebaseDatabase = FB.FirebaseDatabase()


    def register_clicked():
        print("Register Clicked")
        import Registration

    def login(email, password):
        try:
            print("Logging in")
            firebaseDatabase.auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in!")
            import characterSelect
        except:
            print("Invalid email or password")

    def loginTeacher(email, password):
        try:
            print("Logging in")
            firebaseDatabase.auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in!")
            import teacherDashboard
        except:
            print("Invalid email or password")

    while running:
        screen.blit(background_img, (0, 0))
        # email_txtbox = assets.Button(screen=screen,id='emailTextbox',image=email_txtbox,scale=1,x=531,y=267)
        # password_txtbox = assets.Button(screen=screen,id='passwordTextbox',image=password_txtbox,scale=1,x=531,y=316)
        btn_login = assets.Button(screen=screen,id='buttonLogin',image=loginImage,scale=1,x=503,y=338)
        btn_teacherLogin = assets.Button(screen=screen,id='buttonTeacherLogin',image=teacherLoginImage,scale=1,x=317,y=338)
        btn_registration = assets.Button(screen=screen,id='buttonRegistration',image=registrationImage,scale=1,x=434,y=392)
       
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
        for event in pygame.event.get():
           
            if btn_registration.draw():
                register_clicked() 

            if btn_login.draw():
                print(SAVE_DATA['email'])
                print(SAVE_DATA['password'])
                login(SAVE_DATA['email'], SAVE_DATA['password'])

            if btn_teacherLogin.draw():
                print(SAVE_DATA['email'])
                print(SAVE_DATA['password'])
                loginTeacher(SAVE_DATA['email'], SAVE_DATA['password'])
                
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

        # screen.blit(userNamePrompt, ((w - userNamePrompt.get_width()) / 2,
        #                              (h * .20) + userNameSurface.get_height()))

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

        if btn_teacherLogin:
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

Login()



    
        

    
    

