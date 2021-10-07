from tkinter import *
import pyrebase
from tkinter import messagebox
import linkingpages
import registrationtestlink 

firebaseConfig = {
  'apiKey': "AIzaSyBEOlShI29lUu4NhonKtqFH-NSt85ZvGVI",
  'authDomain': "math-blasters.firebaseapp.com",
  'projectId': "math-blasters",
  'storageBucket': "math-blasters.appspot.com",
  'messagingSenderId': "1022427765658",
  'appId': "1:1022427765658:web:f5319e28731afca5783823",
  'measurementId': "G-L2L2H64FDN",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = window.Label(self, text="Registration Page")
        label.pack(side="top", fill="both", expand=True)

    window = Tk()

    window.geometry("1000x600")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    login_img = PhotoImage(file = './Login/background.png')
    background = canvas.create_image(
        500.0, 300.0,
        image=login_img)

    entry0_img = PhotoImage(file = './Login/img_textBox0.png')
    entry0_bg = canvas.create_image(
        531.0, 267.0,
        image = entry0_img)

    email = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0).place(x = 434.0, y = 251,width = 194.0,height = 30)

    entry1_img = PhotoImage(file = './Login/img_textBox1.png')
    entry1_bg = canvas.create_image(
        531.0, 316.0,
        image = entry1_img)

    password = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        show="*",
        width=20).place(x = 434.0, y = 300,width = 194.0,height = 30)

    img0 = PhotoImage(file = './Login/img0.png')
    loginButton = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = login_clicked,
        relief = "flat").place(x = 491, y = 351,width = 145,height = 47)

    img1 = PhotoImage(file = './Login/img1.png')

    registerButton = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = linkingpages.MainView.show,
        relief = "flat",
    ).place( x = 320, y = 360, width = 138, height = 37)

    window.resizable(False, False)
    window.mainloop()

def login_clicked():
    print("Login Clicked")
    uniqueId1 = login.email.get()
    password1 = login.password.get()
    login(uniqueId1, password1)

def register_clicked():
    print("Register Clicked")

def login(email, password):
    try:
        print("Logging in")
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        #used to test logic, can just add the linking function here
        # window.destroy()
        
    except:
        print("Invalid email or password")
        messagebox.showerror("Error", "Invalid email or password")

