# converter.py
# This file will contain the source code for converting csv files to json
import json
import os


# A function that returns "Hello World". This function is called in start_gui() in gui.py.
# Change what is returned in this function to edit what is displayed in the "Hello World" GUI.
def hello_world():
    return "Hello World"


# A function that returns "In CLI". This function is called in main.py to signify that the GUI has not been started.
def cli():
    return "In CLI"


# A function which writes the contents of a Python dictionary to a JSON file
def dict_to_json(json_path, dictionary):
    # Check if path is a directory
    is_directory = os.path.isdir(json_path)
    if is_directory:
        json_path = json_path + "\\data.json"

    # Ensure we are not overwriting an existing file
    if os.path.exists(json_path):
        i = 1
        found = False
        while not found:
            old_path = json_path.rsplit(".", 1)
            new_path = old_path[0] + "(" + str(i) + ")." + old_path[1]
            if not os.path.exists(new_path):
                found = True
                json_path = new_path
            i = i + 1

    # Write the file if the path is correct
    try:
        with open(json_path, "w") as outfile:
            json.dump(dictionary, outfile)
    except:
        return "Error: Output path incorrect"

    return ""  # No error to return
