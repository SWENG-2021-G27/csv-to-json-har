# main.py

from gui import *
from converter import *
from configuration import *
import sys
import os
import re
from colorama import Fore, Style
from colorama import init as colorama_init

# This makes the coloring cross platform
colorama_init()

# Use "<dir>" + sep + "<dir>"  instead of <dir>\\<dir> or <dir>/<dir> for building paths to make it cross-platform
sep = os.path.sep

# WARNING the current working directory is determined by where the program is called from not where the program is. If the user is not in the src directory when the program is called, the relative paths will not work
# We can use the first command line argument to change to src see if __name__ ==... section below
# neimhin: I think this should be changed such that for each folder in RawDatasets we check if there's a config.json and use that for that folder

# In case we need to know where the user called the program from we can use this variable
user_working_directory = os.getcwd()


def warn(warning):
    # warning in yellow
    print("\n\t" + Fore.YELLOW + "[WARNING]: " + Style.RESET_ALL + warning)


def error(error_msg):
    # error in red
    print("\n\t" + Fore.RED + "[ERROR]: " + Style.RESET_ALL + error_msg + "\n")
    sys.exit(-1)

default_options = {
    "config_file_path": ".." + sep + "RawDatasets" + sep + "PKUMMD" + sep + "config.json",
    "input_path": ".." + sep + "RawDatasets" + sep + "PKUMMD",
    "output_path": ".." + sep + "ConvertedJsonOutput" + sep + "PKUMMD",
}
option_flag = {
    "config_file_path": "--config",
    "input_path": "--input",
    "output_path": "--output",
}
options = {
    "config_file_path": None,
    "input_path": None,
    "output_path": None,
}

extra_options = {
    "single_file": False,
    "gui": False,
}


# This function will either launch the GUI or operate as a CLI.
# Functionality is determined by the number of command line arguments.
def main():
    # Load in command line arguments
    command_line_arguments = sys.argv
    print(Fore.GREEN + "\n\tParsing the following arguments: " + Style.RESET_ALL + str(command_line_arguments[1:]))
    # If the -gui field is present in the command line arguments, open the GUI
    if "--gui" in command_line_arguments or '-g' in command_line_arguments:
        extra_options["gui"] = False
        if (len(command_line_arguments) > 2):
            print("Starting GUI and ignoring other command line arguments")
        start_gui()
        # The GUI and the CLI are not setup to work in tandem, thus for each instance of the program the user can only start one of them
        # Therefore end the main function if start the gui
        return

    # If the --input field is present in the command line arguments, update the input directory
    overwriting = None
    for opt in ['-i', '--input']:
        if opt in command_line_arguments:
            idx = command_line_arguments.index(opt)
            if idx >= len(command_line_arguments) - 1:
                error(
                    Fore.BLUE + opt + Style.RESET_ALL + " field incorrectly specified. The " + Fore.BLUE + opt + Style.RESET_ALL + " option takes exactly one parameter. Zero given.")
                return
            else:
                path = command_line_arguments[idx + 1]
                command_line_arguments.pop(idx)
                command_line_arguments.pop(idx)
                if not os.path.exists(path):
                    error(path + " (parameter of " + opt + " option) does not exist")
                    return
                elif os.path.isfile(path):
                    extra_options["single_file"] = True
                elif os.path.isdir(path):
                    extra_options["single_file"] = False

            options["input_path"] = path
            if (not extra_options["single_file"]):
                options["config_file_path"] = options["input_path"] + sep + "config.json"
                options["output_path"] = options["input_path"] + sep + "Output"

            # in case both -i and --input are given we take --input overwriting -i
            if (overwriting != None):
                warn("Overwriting " + overwriting + " option. Using " + opt + " instead of " + overwriting)
            overwriting = opt

    # If the --config field is present in the command line arguments
    overwriting = None
    for opt in ['-c', '--config']:
        if opt in command_line_arguments:
            idx = command_line_arguments.index(opt)
            if idx >= len(command_line_arguments) - 1:
                error(opt + " field incorrectly specified. " + opt + " takes exactly one argument. Zero given.")

            path = command_line_arguments[idx + 1]
            command_line_arguments.pop(idx)
            command_line_arguments.pop(idx)
            if not os.path.exists(path):
                error(path + " (parameter of the " + opt + " option)  does not exist")
            if not os.path.isfile(path):
                error(path + " (parameter of the " + opt + " option)  is not a file")
            if not path.endswith(".json"):
                error(
                    path + " (parameter of the " + opt + " option)  is not a json.\n TODO: provide help for the json format.")

            options["config_file_path"] = path
            if (overwriting != None):
                warn(" Ignoring " + overwriting + " in favour of " + opt + " " + path)
            overwriting = opt + " " + path

    # If the --output field is present in the command line arguments, update the output directory
    overwriting = None
    for opt in ['-o', '--output']:
        if opt in command_line_arguments:
            idx = command_line_arguments.index(opt)
            if idx >= len(command_line_arguments) - 1:
                print("\n    [ERROR]: " + opt + " field incorrectly specified")
                return
            else:
                path = command_line_arguments[idx + 1]
                command_line_arguments.pop(idx)
                command_line_arguments.pop(idx)
                exists = os.path.exists(path)
                if (exists and os.path.isfile(path) and not extra_options["single_file"]):
                    print(
                        "\n    [ERROR]: The argument of the " + opt + " option is a directory but output is a file. " + opt + " takes the path to a directory unless the input is a file, in which case " + opt + " can take a file which will be created or overwritten.")

                if (overwriting != None):
                    print("\n    [WARNING]: Ignoring " + overwriting + " in favour of " + opt + " " + path)
                overwriting = opt
                options["output_path"] = path

    # We don't need the first argument (i.e. the path to main.py)
    command_line_arguments.pop(0)
    # Filter through any remaining options and report that they were invalid
    # i.e. any arguments beginning with - or --
    single_char_switch = re.compile("-[a-z]")
    multi_char_switch = re.compile("--[a-z]+")
    too_many_chars = re.compile("-[^-].+")
    idx = 0
    while idx < len(command_line_arguments):
        arg = command_line_arguments[idx]
        if (re.match(single_char_switch, arg)):
            warn(arg + " is not a recognised switch and is being ignored")
            command_line_arguments.pop(idx)
        elif (re.match(too_many_chars, arg)):
            warn(arg + " is not a recognised switch and is being ignored.\nNOTE: multi character switches begin with two dashes, e.g. --config, wheras single character switches begin with one dash, e.g -c")
            command_line_arguments.pop(idx)
        elif (re.match(multi_char_switch, arg)):
            warn(arg + " is not a recognised switch and is being ignored.")
            command_line_arguments.pop(idx)
        else:
            idx += 1

    
    # Consume remaining arguments
    if (len(command_line_arguments) > 0):
      # Assign remaining options in default order
      for opt in options.keys():
        if(len(command_line_arguments) == 0):
          break
        if options[opt] == None:
          options[opt] = command_line_arguments[0]
          command_line_arguments.pop(0)
    
    # Use default_options for any options that are still None
    for opt in options.keys():
      if options[opt] == None:
        warn("Using default " + opt + ": " + default_options[opt] + "\n\tUse " + Fore.BLUE+ option_flag[opt] + " <" + opt +">" + Style.RESET_ALL + " to set the " + opt +" manually.")
        options[opt] = default_options[opt]  
      
    if (len(command_line_arguments) > 0):
        # Show command line arguments that weren't consumed. The first argument should not have been consumed. It is the name of the program that was called.
        warn("The following command line arguments were not matched in any pattern and were not loaded: ")
        print(command_line_arguments)

    # Load the configuration appropriately
    if (options["config_file_path"] == None):
        error("No config file has been specified. Specify the path of the config file with --config <path>. Aborting.")

    if (options["input_path"] == None):
        error(
            "No input path has been specified. Specify the path of the file or folder to be converted with --input <path>. Aborting.")

    if (options["output_path"] == None):
        error(
            "No output location has been specified. Specify the path of the file to write converted json to with --ouput <path>. If the input is a single file, output may also be a single file. Aborting.")
    x = Configuration(options["config_file_path"])

    if (extra_options["single_file"]):
        pass
    # Convert all csv files in the input directory
    else:
        if not os.path.exists(options["output_path"]):
            try:
                os.makedirs(options["output_path"])
            except OSError:
                error("Failed to create output directory " + options["output_path"])
        for filename in os.listdir(options["input_path"]):
            if filename.endswith(x.config["FileExtension"]):
                base = os.path.splitext(filename)[0]
                if x.config["Structure"] == "Vertical":
                    convert_vertical(options["input_path"] + sep + filename,
                                     options["output_path"] + sep + base + ".json", x)
                elif x.config["Structure"] == "NTU":
                    convert_ntu(options["input_path"] + sep + filename,
                                options["output_path"] + sep + base + ".json", x)


if __name__ == "__main__":
    # Here's how we could change to the src directory if the user is calling the program from another directory. At the moment we're not set up to handle this.
    """
    path_to_src = sys.argv[0]
    # Split the path by the systems path seperator
    path_to_src_as_list = path_to_src.split(sep) # separator=sep i.e. '/' on posix or '\\' on windows
    path_to_src_as_list[len(path_to_src_as_list) -1] = '.'
    for directory in path_to_src_as_list:
    os.chdir(directory)
    print("Current working directory is now: " + os.getcwd())
    """
    main()
    print(Fore.GREEN + "\tFinished!" + Style.RESET_ALL)
