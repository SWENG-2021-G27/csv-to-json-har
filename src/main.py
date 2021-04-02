# main.py

from gui import *
from converter import *
from configuration import *
import sys
import os

sep = os.path.sep


# WARNING the current working directory is determined by where the program is called from not where the program is. If the user is not in the src directory when the program is called, the relative paths will not work
# We can use the first command line argument to change to src see if __name__ ==... section below
input_path = ".." + sep + "RawDatasets"  # Default input directory
# neimhin: I think this should be changed such that for each folder in RawDatasets we check if there's a config.json and use that for that folder
config_file = None
output_directory = None  # Default output directory

# In case we need to know where the user called the program from we can use this variable
global user_working_directory = os.getcwd()


global options = {
  "config_file_path": None,
  "input_path": None,
  "output_path" : None,
}

global extra_options = {
  "single_file" : None,
  "gui" : None,
}

# This function will either launch the GUI or operate as a CLI.
# Functionality is determined by the number of command line arguments.
def main():
    # Load in command line arguments
    command_line_arguments = sys.argv
    eaten = 
    # If the -gui field is present in the command line arguments, open the GUI
    if "--gui" in command_line_arguments or '-g' in command_line_arguments:
        if(len(command_line_arguments) > 2):
          print("Starting GUI and ignoring other command line arguments")
        start_gui()
        # The GUI and the CLI are not setup to work in tandem, thus for each instance of the program the user can only start one of them
        # Therefore end the main function if start the gui
        return
      
    # We should be able to handle both cases where --input is a folder or a file
    global single_file = False

    global input_directory
    global config_file
    global output_directory

    # If the --input field is present in the command line arguments, update the input directory
    overwriting = None
    for opt in ['-i','--input']:
      if opt in command_line_arguments:
        idx = command_line_arguments.index(opt)
        if idx >= len(command_line_arguments) - 1:
            print("\n    [ERROR]: " + opt + " field incorrectly specified. The " + opt + " option takes exactly one parameter. Zero given.")
            return
        else:
          path = command_line_arguments[idx + 1]
          command_line_arguments.pop(idx)
          command_line_arguments.pop(idx)
          if not os.path.exists(path):
            print("\n    [ERROR]: " + path " (parameter of " + opt + " option) does not exist")
            return
          elif not os.path.isdir(path):
            single_file = True

        options["input_path"]
        if( not single_file ):
          config_file = input_path + sep + "config.json"
          output_directory = input_path + sep + "Output"
       
        # in case both -i and --input are given we take --input overwriting -i
        if(overwriting != None):
          print("\n    [WARNING]: Overwriting " + overwriting + " option. Using " + opt +" instead of " + overwriting)
        overwriting = opt

    # If the --config field is present in the command line arguments
    overwriting = None
    for opt in ['-c', '--config']:
      if opt in command_line_arguments:
        idx = command_line_arguments.index(opt)
        if idx >= len(command_line_arguments) - 1:
            print("\n    [ERROR]: " + opt + " field incorrectly specified. --config takes exactly one argument. Zero given.")
            return
        else:
          path = command_line_arguments[idx + 1]
          command_line_arguments.pop(idx)
          command_line_arguments.pop(idx)
          if not os.path.exists(command_line_arguments[idx + 1]):
            print("\n    [ERROR]: " + command_line_arguments[idx + 1] + " (parameter of the --config option)  does not exist")
            return
        elif not os.path.isfile(command_line_arguments[idx + 1]):
            print("\n    [ERROR]: " + command_line_arguments[idx + 1] + " (parameter of the --config option)  is not a file")
            return
        elif not command_line_arguments[idx + 1].endswith(".json"):
            print("\n    [ERROR]: -" + command_line_arguments[idx + 1] + " (parameter of the --config option)  is not a json.\n TODO: provide help for the json format.")
            return

        config_file = command_line_arguments[idx + 1]

    # If the -input field is present in the command line arguments, update the output directory
    if "--output" in command_line_arguments:
        idx = command_line_arguments.index("-output")
        if idx >= len(command_line_arguments) - 1:
            print("\n    [ERROR]: --output field incorrectly specified")
            return
        else:
          path = command_line_arguments[idx + 1]
          exists = os.path.exists(path)
          if( exists and not os.path.isdir(path) and not single_file):
            print("\n    [ERROR]: The argument of the --input option is a directory but output is a file. --output takes the path to a directory unless the input is a file, in which case --output can take a file which will be created or overwritten." 

          output_directory = command_line_arguments[idx + 1]

    # If the output directory does not exist, create it
    if not os.path.exists(output_directory):
        try:
            os.mkdir(output_directory)
        except OSError:
            print("\n    [ERROR]: failed to create output directory " + output_directory)
            return

    # Load the configuration appropriately
    x = Configuration(config_file)

    # Convert all csv files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv") or filename.endswith(".txt"):
            base = os.path.splitext(filename)[0]
            if x.config["Structure"] == "Vertical":
                convert_vertical(input_directory + "\\" + filename, output_directory + "\\" + base + ".json", x)


if __name__ == "__main__":
    path_to_src = sys.argv[0]
    # Split the path by the systems path seperator
    path_to_src_as_list = path_to_src.split(sep) # separator=sep i.e. '/' on posix or '\\' on windows
    path_to_src_as_list[len(path_to_src_as_list) -1] = '.'
    for directory in path_to_src_as_list:
      os.chdir(directory)
    print("Current working directory is now: " + os.getcwd())
    main()
    print("Finished!")
