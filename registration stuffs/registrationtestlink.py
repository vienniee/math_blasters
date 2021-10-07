from tkinter import *
import pyrebase
import logintestlink
import linkingpages

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

def registration(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = window.Label(self, text="Registration Page")
        label.pack(side="top", fill="both", expand=True)
    window = Tk()
    window.title('MathBlasters')

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

    registration_img = PhotoImage(file = './Registration/background.png')
    background = canvas.create_image(
        500.0, 300.0,
        image=registration_img)

    entry0_img = PhotoImage(file = './Registration/img_textBox0.png')
    entry0_bg = canvas.create_image(
        539.0, 237.0,
        image = entry0_img)

    username = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    username.place(
        x = 442.0, y = 221,
        width = 194.0,
        height = 30)

    entry1_img = PhotoImage(file = './Registration/img_textBox1.png')
    entry1_bg = canvas.create_image(
        539.0, 284.0,
        image = entry1_img)


    email = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    email.place(
        x = 442.0, y = 268,
        width = 194.0,
        height = 30)

    entry2_img = PhotoImage(file = './Registration/img_textBox3.png')
    entry2_bg = canvas.create_image(
        543.0, 331.5,
        image = entry2_img)

    classLevel = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    classLevel.place(
        x = 446.0, y = 315,
        width = 194.0,
        height = 31)

    entry3_img = PhotoImage(file = './Registration/img_textBox2.png')
    entry3_bg = canvas.create_image(
        543.0, 378.5,
        image = entry3_img)

    password = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        show="*",
        width=20)

    password.place(
        x = 446.0, y = 363,
        width = 194.0,
        height = 29)


    img0 = PhotoImage(file = './Registration/img0.png')

    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = linkingpages.MainView.p1.show,
        relief = "flat",

        )

    b0.place(
        x = 388, y = 402,
        width = 190,
        height = 54)



    window.resizable(False, False)
    window.mainloop()



def signup(email, password):
    try:
      user = auth.create_user_with_email_and_password(email, password)
      print("Successfully created")
    
    except:
      print("Email already exist")


def btn_clicked():
    print("Button Clicked")
    uniqueId1 = registration.email.get()
    password1 = registration.password.get()
    signup(uniqueId1, password1)
    



