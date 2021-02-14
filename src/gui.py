# gui.py
# This file will contain the source code for the GUI

from tkinter import *
from converter import *

# A function to create a Hello World GUI, pulling data from a converter.py function
def start_gui():
    window = Tk()
    window.title("Test")
    greeting = Label(window, text=hello_world())
    greeting.grid(column=0, row=0)
    window.mainloop()
