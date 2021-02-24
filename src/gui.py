# gui.py
# This file will contain the source code for the GUI

import tkinter as tk
from tkinter import ttk
from converter import *


# app class that displays the different pages of the GUI
class app(tk.Tk):

    # Constructor for the app class
    def __init__(self, *args, **kwargs):
        # Constructor for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Create a container
        container = tk.Frame(self, bg="white")
        tk.Tk.geometry(self, "500x500")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create empty dictionary of app pages
        self.frames = {}

        # Fill the dictionary with the app pages
        for F in (LandingPage, StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LandingPage)

    # Display the current page
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# The Landing Page
class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Change background colour
        self.configure(bg="white")

        # Welcome Message
        greeting = ttk.Label(self, text="HAR - CSV to JSON", font=("Arial", 20, "bold"))
        greeting.place(relx=0.5, anchor="center")
        greeting.config(background="white", foreground="black")
        greeting.pack(padx=0, pady=(50, 0))

        # Explanation
        info = ttk.Label(self, text="A CSV to JSON conversion tool for creating animations from HAR datasets",
                         font=("Arial", 9))
        info.place(relx=0.5, anchor="center")
        info.config(background="white", foreground="gray")
        info.pack(padx=0, pady=(50, 0))

        # Get Started Button
        button_style = ttk.Style()
        button_style.configure("B.TButton", font=("Arial", 12))

        button = ttk.Button(self, text="Get Started", style="B.TButton", width=20,
                            command=lambda: controller.show_frame(StartPage))
        button.place(relx=0.5, anchor="center")
        button.pack(padx=0, pady=(100, 0))


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1")
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2")
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# This function creates an instance of the app class and displays the GUI
def start_gui():
    gui = app()
    gui.mainloop()
