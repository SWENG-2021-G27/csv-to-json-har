# gui.py

from tkinter import *
from converter import *


def start_gui():
    window = Tk()
    window.title("Test")
    greeting = Label(window, text=hello_world())
    greeting.grid(column=0, row=0)
    window.mainloop()
