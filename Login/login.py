from tkinter import *
import pyrebase

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
print('hi')
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login_clicked():
    print("Login Clicked")
    uniqueId1 = email.get()
    password1 = password.get()
    login(uniqueId1, password1)

def register_clicked():
    print("Register Clicked")

def login(email, password):
    try:
        print("Logging in")
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
    except:
        print("Invalid email or password")

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

background_img = PhotoImage(file = './Login/background.png')
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = './Login/img_textBox0.png')
entry0_bg = canvas.create_image(
    531.0, 267.0,
    image = entry0_img)

email = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

email.place(
    x = 434.0, y = 251,
    width = 194.0,
    height = 30)

entry1_img = PhotoImage(file = './Login/img_textBox1.png')
entry1_bg = canvas.create_image(
    531.0, 316.0,
    image = entry1_img)

password = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    show="*",
    width=20)

password.place(
    x = 434.0, y = 300,
    width = 194.0,
    height = 30)

img0 = PhotoImage(file = './Login/img0.png')
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login_clicked,
    relief = "flat")

b0.place(
    x = 491, y = 351,
    width = 145,
    height = 47)

img1 = PhotoImage(file = './Login/img1.png')
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = register_clicked,
    relief = "flat",
   )

b1.place(
    x = 320, y = 360,
    width = 138,
    height = 37)

window.resizable(False, False)
window.mainloop()
