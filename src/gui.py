# gui.py
# This file will contain the source code for the GUI

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from converter import *


# app class that displays the different pages of the GUI
class app(tk.Tk):

    # Constructor for the app class
    def __init__(self, *args, **kwargs):
        # Constructor for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Set title of window
        self.title("HAR - CSV to JSON")

        # Create a container
        container = tk.Frame(self, bg="white")
        tk.Tk.geometry(self, "500x500")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create empty dictionary of app pages
        self.frames = {}

        # Fill the dictionary with the app pages
        for F in (LandingPage, ConfigurationPage):
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

        # Configure the weight of the empty rows for spacing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(5, weight=2)
        self.grid_columnconfigure(0, weight=1)

        # Change background colour
        self.configure(bg="white")

        # Welcome Message
        greeting = ttk.Label(self, text="HAR - CSV to JSON", font=("Arial", 20, "bold"))
        greeting.config(background="white", foreground="black")
        greeting.grid(row=1, column=0)

        # Explanation Message
        info = ttk.Label(self, text="A CSV to JSON conversion tool for creating animations from HAR datasets",
                         font=("Arial", 9))
        info.config(background="white", foreground="gray")
        info.grid(row=2, column=0)

        # Get Started Button
        get_started_button_style = ttk.Style()
        get_started_button_style.configure("GetStarted.TButton", font=("Arial", 11))
        button = ttk.Button(self, text="Get Started", style="GetStarted.TButton", width=20,
                            command=lambda: controller.show_frame(ConfigurationPage))
        button.grid(row=4, column=0)


selected_file = ""
selected_format = ""
format_options = [
    "Please Select a Dataset",
    "One",
    "Two",
    "Three"
]


# The Conversion Configuration Page
class ConfigurationPage(tk.Frame):
    def select_file(self):
        global selected_file
        selected_file = filedialog.askopenfilename()
        to_display = selected_file[0:50] + "..."
        self.file_var.set(to_display)

    def submit_file(self):
        global selected_format
        selected_format = self.format_var.get()
        print(selected_format)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Variables to store what the user has selected
        self.file_var = StringVar()
        self.file_var.set(selected_file)
        self.format_var = StringVar()
        self.format_var.set(format_options[0])

        # Configure the weight of the rows and columns for spacing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(5, weight=10)

        # Change background colour
        self.configure(bg="white")

        # Create List Labels
        list_one = ttk.Label(self, text="1", font=("Arial", 20, "bold"))
        list_one.config(background="white", foreground="#40c3f7")
        list_one.grid(row=1, column=1, sticky="W")
        list_two = ttk.Label(self, text="2", font=("Arial", 20, "bold"))
        list_two.config(background="white", foreground="#40c3f7")
        list_two.grid(row=3, column=1, sticky="W")

        # List Messages
        upload_file_message = ttk.Label(self, text="Upload File:", font=("Arial", 20, "bold"))
        upload_file_message.config(background="white", foreground="black")
        upload_file_message.grid(row=1, column=2, sticky="W")

        file = ttk.Label(self, textvariable=self.file_var, font=("Arial", 9))
        file.config(background="white", foreground="black")
        file.grid(row=2, column=2, sticky="W", columnspan=3)

        select_format_message = ttk.Label(self, text="Select format:", font=("Arial", 20, "bold"))
        select_format_message.config(background="white", foreground="black")
        select_format_message.grid(row=3, column=2, sticky="W")

        # Buttons and Dropdowns
        button_style = ttk.Style()
        button_style.configure("B.TButton", font=("Arial", 9))
        upload_file_button = ttk.Button(self, text="Browse Files...", style="B.TButton", width=15,
                                        command=self.select_file)
        upload_file_button.grid(row=1, column=3, sticky="W")

        dropdown_style = ttk.Style()
        dropdown_style.configure("TMenubutton", font=("Arial", 9))
        dropdown = ttk.OptionMenu(self, self.format_var, *format_options)
        dropdown.grid(row=4, column=2, sticky="EW", columnspan=3)

        submit_button = ttk.Button(self, text="Submit for conversion", style="B.TButton", command=self.submit_file)
        submit_button.grid(row=5, column=2, columnspan=3)


# This function creates an instance of the app class and displays the GUI
def start_gui():
    gui = app()
    gui.mainloop()
