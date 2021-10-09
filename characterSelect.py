from tkinter import *
import tkinter as tk
from PyQt5 import QtWidgets  
import sys, importlib
import firebase as FB
importlib.reload(sys.modules['firebase'])

PATH = "Image/characterSelect/"

class Window:

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 500
    BACKGROUND_COLOR = "#FFFFFF"

    def setInterface(self):
        self.window =  Tk()
        self.window.configure(bg = Window.BACKGROUND_COLOR)
        self.canvas = Canvas(
            self.window,
            bg = Window.BACKGROUND_COLOR,
            height = Window.WINDOW_HEIGHT,
            width = Window.WINDOW_WIDTH,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)


class CharacterSelect(Window):

    TEXT_ID=0
    CHAR_SELECT=None
    TEXT_CHARACTER_SELECTED = "Character Select"
    TEXT_DEMON_SELECTED = "Demon Selected"
    TEXT_WARRIOR_SELECTED = "Warrior Selected"
    TEXT_NO_OPTION_SELECTED = "Select a character to proceed!"

    

    TEMP_STUDENT_DATA = {"name":"student 1","age":15}
    TEMP_STUDENT_ID = "TESTID"


    def __init__(self):
        self.firebaseDatabase = FB.FirebaseDatabase()
        

    def Onclick_btn_demon(self):
        print("Demon has been selected")
        self.createText(CharacterSelect.TEXT_DEMON_SELECTED)
        CharacterSelect.CHAR_SELECT = "Demon"
    
    def OnClick_btn_warrior(self):
        print("Warrior has been selected")
        self.createText(CharacterSelect.TEXT_WARRIOR_SELECTED)
        CharacterSelect.CHAR_SELECT = "Warrior"

    
    def OnClick_btn_confirm(self):
        if(CharacterSelect.CHAR_SELECT == None):
            print("No character selected")
            self.createText(CharacterSelect.TEXT_NO_OPTION_SELECTED)
            #self.refresh()
            self.window.destroy()
            temporaryMenu = TemporaryMenu()
            temporaryMenu.placeInterface()      
        
        else:
            print("Confirm selected")
            CharacterSelect.TEMP_STUDENT_DATA['character'] = CharacterSelect.CHAR_SELECT
            self.firebaseDatabase.setStudentData(CharacterSelect.TEMP_STUDENT_ID,CharacterSelect.TEMP_STUDENT_DATA)
            print(self.firebaseDatabase.getStudentData(CharacterSelect.TEMP_STUDENT_ID))

    def buttonPlace(self,button:Button,position:tuple,shape:tuple):
        button.place(
        x = position[0], y = position[1],
        width = shape[0],
        height = shape[1])

    def createText(self,TEXT):
        if(self.getTextID() == 0):
            ID = self.canvas.create_text(
            410, 190,
            text = TEXT,
            fill = "#000000",
            font = ("Rowdies-Regular", int(16)))
            self.setTextID(ID)
        
        else:
            self.canvas.delete(self.getTextID())
            ID = self.canvas.create_text(
            410, 190,
            text = TEXT,
            fill = "#000000",
            font = ("Rowdies-Regular", int(16)))
            self.setTextID(ID)

    def getTextID(self):
        return CharacterSelect.TEXT_ID

    def setTextID(self,id):
        CharacterSelect.TEXT_ID = id

    def placeInterface(self):
        self.setInterface()
        self.loadAssets()
        background = self.canvas.create_image(
        400.0, 300.0,
        image=self.background_img)

        self.placeAssets()
        self.center_window()
        self.window.resizable(False, False)
        self.window.mainloop()

    def center_window(self,width=800, height=500):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def placeAssets(self):

        self.button_demon = Button(
        image = self.img_demon,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.Onclick_btn_demon,
        relief = "flat")

        self.button_warrior = Button(
            image = self.img_warrior,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.OnClick_btn_warrior,
            relief = "flat")


        self.button_confirm = Button(
            image = self.img_confirm,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.OnClick_btn_confirm,
            relief = "flat")

        self.createText(CharacterSelect.TEXT_CHARACTER_SELECTED)
        self.buttonPlace(self.button_demon,(297,216),(83,90))
        self.buttonPlace(self.button_warrior,(423,216),(83,90))
        self.buttonPlace(self.button_confirm,(358,331),(84,32))


    def loadAssets(self):
        self.background_img = PhotoImage(file = PATH+"background.png")
        self.img_demon = PhotoImage(file = PATH+"img0.png")
        self.img_warrior = PhotoImage(file = PATH+"img1.png")
        self.img_confirm = PhotoImage(file = PATH+"img2.png")

    
    def main(self):
        self.placeInterface()

    def refresh(self):
        self.window.destroy()
        self.main()
            

#This is a sample implementation: use window super class to set interface
class TemporaryMenu:
    def loadAssets(self):
        self.background_img = PhotoImage(file = PATH+"background.png")
        self.img_demon = PhotoImage(file = PATH+"img0.png")
        self.img_warrior = PhotoImage(file = PATH+"img1.png")
        self.img_confirm = PhotoImage(file = PATH+"img2.png")

    def placeInterface(self):
        self.window =  Tk()
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.loadAssets()
        background = self.canvas.create_image(
        400.0, 300.0,
        image=self.background_img)

        self.center_window()
        self.window.resizable(False, False)
        self.window.mainloop()

    def center_window(self,width=800, height=500):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))



#refer to OnClick_btn_confirm function for UI change
characterSelect = CharacterSelect()      
characterSelect.main()  


















