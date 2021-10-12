from tkinter import *
import pyrebase
from tkinter import messagebox
import firebase as FB

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




class Window:
    def setInterface(self):
        self.window = Tk()
        self.window.geometry("1000x600")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

class Login(Window):

    def __init__(self):
            self.firebaseDatabase = FB.FirebaseDatabase()

    def placeInterface(self):
        self.setInterface()
        self.loadAssets()
        
        background = self.canvas.create_image(
        500.0, 300.0,
        image=self.background_img)
        
        entry0_bg = self.canvas.create_image(
            531.0, 267.0,
            image = self.entry0_img)

        entry1_bg = self.canvas.create_image(
            531.0, 316.0,
            image = self.entry1_img)

        self.placeAssets()
        self.window.resizable(False, False)
        self.window.mainloop()

    def loadAssets(self):
        self.entry0_img = PhotoImage(file = './Login/img_textBox0.png')
        self.entry1_img = PhotoImage(file = './Login/img_textBox1.png')
        self.img0 = PhotoImage(file = './Login/img0.png')
        self.img1 = PhotoImage(file = './Login/img1.png')
        self.background_img = PhotoImage(file = './Login/background.png')

    def placeAssets(self):
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.login_clicked,
            relief = "flat")

        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.register_clicked,
            relief = "flat")

        self.email = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.email.place(
            x = 434.0, y = 251,
            width = 194.0,
            height = 30)

        self.password = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0,
            show="*",
            width=20)

        self.password.place(
            x = 434.0, y = 300,
            width = 194.0,
            height = 30)

        self.b0.place(
            x = 491, y = 351,
            width = 145,
            height = 47)

        self.b1.place(
            x = 320, y = 360,
            width = 138,
            height = 37)

    def login_clicked(self):
        print("Login Clicked")
        self.uniqueId1 = self.email.get()
        self.password1 = self.password.get()
        self.login(self.uniqueId1, self.password1)

    def register_clicked(self):
        print("Register Clicked")

    def login(self, email, password):
        try:
            print("Logging in")
            auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in!")
        except:
            print("Invalid email or password")
            # self.messagebox.showerror("Error", "Invalid email or password")

    def main(self):
        self.placeInterface()
    
Login().main()
