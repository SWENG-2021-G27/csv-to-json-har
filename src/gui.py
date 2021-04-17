# gui.py
# This file will contain the source code for the GUI

from main import error
from configuration import Configuration
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
import threading
import sys
from converter import *
from main import *

shut_off = False


# app class that displays the different pages of the GUI
class App(tk.Tk):

    # Constructor for the app class
    def __init__(self, *args, **kwargs):
        # Constructor for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Set title of window
        self.title("HAR - CSV to JSON")

        # Create a container
        container = tk.Frame(self, bg="white")
        tk.Tk.geometry(self, "600x600")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create empty dictionary of app pages
        self.frames = {}

        # Fill the dictionary with the app pages
        for F in (LandingPage, ConfigurationPage, ConvertPage, ConclusionPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LandingPage)
        self.th = threading.Thread(target=self.submit_file)

    # Display the current page
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == ConvertPage:
            self.th.start()

    # Submit file to be converted
    def submit_file(self):
        global shut_off
        global config
        global input_folder
        global output_folder
        x = Configuration(config)
        # Convert all csv files in the input directory
        if x.config["Structure"] == "Vertical":
            os.chdir(input_folder)
            recursive_convert_vertical('.', output_folder, x)
        elif x.config["Structure"] == "NTU":
            os.chdir(input_folder)
            recursive_convert_ntu('.', output_folder, x)
        else:
            error("No Structure provided in config.json. Possible Structure values are: \"Vertical\", \"NTU\"")
        self.show_frame(ConclusionPage)


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
        greeting = ttk.Label(self, text="HAR - CSV to JSON",
                             font=("Arial", 20, "bold"))
        greeting.config(background="white", foreground="black")
        greeting.grid(row=1, column=0)

        # Explanation Message
        info = ttk.Label(self, text="A CSV to JSON conversion tool for creating animations from HAR datasets",
                         font=("Arial", 9))
        info.config(background="white", foreground="gray")
        info.grid(row=2, column=0)

        # Get Started Button
        get_started_button_style = ttk.Style()
        get_started_button_style.configure(
            "GetStarted.TButton", font=("Arial", 11))
        button = ttk.Button(self, text="Get Started", style="GetStarted.TButton", width=20,
                            command=lambda: controller.show_frame(ConfigurationPage))
        button.grid(row=4, column=0)


# The Conversion Configuration Page
class ConfigurationPage(tk.Frame):
    def select_folder(self):
        self.error.config(background="white", foreground="black")
        self.error_message.set("")
        self.folder_var.set("")
        self.folder_to_display.set("")
        folder = filedialog.askdirectory()
        if os.path.isdir(folder):
            self.folder_var.set(folder)
            self.folder_to_display.set(self.folder_var.get()[0:50] + "...")
        else:
            self.error.config(background="indian red", foreground="black")
            if len(folder) < 50:
                self.error_message.set("  " + folder + " is not valid a folder  ")
            else:
                self.error_message.set("  " + folder[0:50] + "... is not valid a folder  ")

    def select_config(self):
        self.error.config(background="white", foreground="black")
        self.error_message.set("")
        self.file_var.set("")
        self.file_to_display.set("")
        config1 = filedialog.askopenfile()
        if os.path.isfile(config1.name) and config1.name.endswith(".json"):
            self.file_var.set(config1.name)
            self.file_to_display.set(self.file_var.get()[0:50] + "...")
        elif not config1.name.endswith(".json"):
            self.error.config(background="indian red", foreground="black")
            if len(config1.name) < 50:
                self.error_message.set("  " + config1.name + " is not valid a json file  ")
            else:
                self.error_message.set("  " + config1.name[0:50] + "... is not json file  ")
        else:
            self.error.config(background="indian red", foreground="black")
            if len(config1.name) < 50:
                self.error_message.set("  " + config1.name + " is not valid a file  ")
            else:
                self.error_message.set("  " + config1.name[0:50] + "... is not valid a file  ")

    def select_output(self):
        self.error.config(background="white", foreground="black")
        self.error_message.set("")
        self.output_var.set("")
        self.output_to_display.set("")
        folder = filedialog.askdirectory()
        if os.path.isdir(folder):
            self.output_var.set(folder)
            self.output_to_display.set(self.folder_var.get()[0:50] + "...")
        else:
            self.error.config(background="indian red", foreground="black")
            if len(folder) < 50:
                self.error_message.set("  " + folder + " is not valid a folder  ")
            else:
                self.error_message.set("  " + folder[0:50] + "... is not valid a folder  ")

    def move_on(self):
        global config
        global input_folder
        global output_folder
        config = self.file_var.get()
        input_folder = self.folder_var.get()
        output_folder = self.output_var.get()
        self.controller.show_frame(ConvertPage)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Variables to store what the user has selected and error message
        self.folder_var = StringVar()
        self.folder_var.set("")
        self.folder_to_display = StringVar()
        self.folder_to_display.set("")
        self.file_var = StringVar()
        self.file_var.set("")
        self.file_to_display = StringVar()
        self.file_to_display.set("")
        self.output_var = StringVar()
        self.output_var.set("")
        self.output_to_display = StringVar()
        self.output_to_display.set("")
        self.error_message = StringVar()
        self.error_message.set("")
        self.controller = controller

        # Configure the weight of the rows and columns for spacing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=3)
        self.grid_rowconfigure(8, weight=3)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=3)
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
        list_three = ttk.Label(self, text="3", font=("Arial", 20, "bold"))
        list_three.config(background="white", foreground="#40c3f7")
        list_three.grid(row=5, column=1, sticky="W")

        # List Messages
        upload_file_message = ttk.Label(
            self, text="Select Input Folder:", font=("Arial", 20, "bold"))
        upload_file_message.config(background="white", foreground="black")
        upload_file_message.grid(row=1, column=2, sticky="W")

        file = ttk.Label(
            self, textvariable=self.folder_to_display, font=("Arial", 9))
        file.config(background="white", foreground="black")
        file.grid(row=2, column=2, sticky="W", columnspan=3)

        select_format_message = ttk.Label(
            self, text="Select Config File:", font=("Arial", 20, "bold"))
        select_format_message.config(background="white", foreground="black")
        select_format_message.grid(row=3, column=2, sticky="W")

        file1 = ttk.Label(
            self, textvariable=self.file_to_display, font=("Arial", 9))
        file1.config(background="white", foreground="black")
        file1.grid(row=4, column=2, sticky="W", columnspan=3)

        select_output_message = ttk.Label(
            self, text="Select Output Folder:", font=("Arial", 20, "bold"))
        select_output_message.config(background="white", foreground="black")
        select_output_message.grid(row=5, column=2, sticky="W")

        file2 = ttk.Label(
            self, textvariable=self.output_to_display, font=("Arial", 9))
        file2.config(background="white", foreground="black")
        file2.grid(row=6, column=2, sticky="W", columnspan=3)

        # Buttons and Dropdowns
        button_style = ttk.Style()
        button_style.configure("B.TButton", font=("Arial", 9))
        upload_folder_button = ttk.Button(self, text="Browse Folders...", style="B.TButton", width=15,
                                          command=self.select_folder)
        upload_folder_button.grid(row=1, column=3, sticky="E")

        upload_config_button = ttk.Button(self, text="Browse Files...", style="B.TButton", width=15,
                                          command=self.select_config)
        upload_config_button.grid(row=3, column=3, sticky="E")

        upload_output_button = ttk.Button(self, text="Browse Folders...", style="B.TButton", width=15,
                                          command=self.select_output)
        upload_output_button.grid(row=5, column=3, sticky="E")

        submit_button = ttk.Button(self, text="Submit for conversion", style="B.TButton",
                                   command=lambda: self.move_on())
        submit_button.grid(row=7, column=2, columnspan=3, )

        # Error Message
        self.error = ttk.Label(self, textvariable=self.error_message, font=("Arial", 9))
        self.error.config(background="white", foregroun="black")
        self.error.grid(row=8, column=0, columnspan=6)


config = ""
input_folder = ""
output_folder = ""


# The Conversion Page
class ConvertPage(tk.Frame):
    def exit_app(self):
        global shut_off
        shut_off = True
        sys.exit(0)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Change background colour
        self.configure(bg="white")

        # Configure the weight of the empty rows for spacing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_columnconfigure(0, weight=1)

        # Create Labels
        convert = ttk.Label(self, text="Converting", font=("Arial", 20, "bold"))
        convert.config(background="white", foreground="black")
        convert.grid(row=1, column=0)

        # Buttons and Dropdowns
        progress = ttk.Progressbar(self, length=300, mode='indeterminate')
        progress.grid(pady=50)
        progress.start(10)

        cancel = ttk.Button(self, text="Cancel", command=lambda: self.exit_app())
        cancel.grid(row=4, column=0)


# The Conclusion Page
class ConclusionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Change background colour
        self.configure(bg="white")

        # Configure the weight of the empty rows for spacing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)

        # Create Labels
        farewell = ttk.Label(self, text="All done!", font=("Arial", 20, "bold"))
        farewell.config(background="white", foreground="black")
        farewell.grid(row=1, column=0)

        # Buttons and Dropdowns
        button_style = ttk.Style()
        button_style.configure("B.TButton", font=("Arial", 9))
        return_to_main_page = ttk.Button(self, text="Return to conversion page", style="B.TButton", width=30,
                                         command=lambda: controller.show_frame(ConfigurationPage))
        return_to_main_page.grid(row=3, column=0)


# This function creates an instance of the app class and displays the GUI
gui = App()


def start_gui():
    # created an app icon
    # gui.tk.call('wm', 'iconphoto', gui.w, tk.PhotoImage(file='GUIicon.png'))
    # added to keep all text on screen at all times
    gui.resizable(False, False)
    gui.mainloop()
