import registration
import login
import tkinter as tk
from tkinter import *

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = login(self)
        p2 = registration(self)

        p1.show()

if __name__ == "__main__":
    window = Tk()
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.mainloop()