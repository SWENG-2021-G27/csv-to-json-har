# main.py
import gui
import converter
import configuration
import sys
import os
import pathlib
import ntpath
import re
import colorama

# This makes the coloring cross platform
colorama.init()

# Use "<dir>" + sep + "<dir>"  instead of <dir>\\<dir> or <dir>/<dir> for building paths to make it cross-platform
sep = os.path.sep

# WARNING the current working directory is determined by where the program is called from not where the program is.
# If the user is not in the src directory when the program is called, the relative paths will not work
# We can use the first command line argument to change to src see if __name__ ==... section below
# neimhin: I think this should be changed such that for each folder in RawDatasets we check if
# there's a config.json and use that for that folder

# In case we need to know where the user called the program from we can use this variable
user_working_directory = os.getcwd()


def warn(warning):
    # warning in yellow
    print("\n\t" + colorama.Fore.YELLOW + "[WARNING]: " + colorama.Style.RESET_ALL + warning)


def error(error_msg):
    # error in red
    print("\n\t" + colorama.Fore.RED + "[ERROR]: " + colorama.Style.RESET_ALL + error_msg + "\n")
    sys.exit(-1)


def nice_msg(msg):
    print("\n\t" + colorama.Fore.GREEN + msg + colorama.Style.RESET_ALL + "\n")


def blue(msg):
    return colorama.Fore.BLUE + msg + colorama.Style.RESET_ALL


default_options = {
    "config_file_path": ".." + sep + "RawDatasets" + sep + "PKUMMD" + sep + "config.json",
    "input_path": ".." + sep + "RawDatasets" + sep + "PKUMMD",
    "output_folder": os.path.join(os.pardir, "ConvertedJsonOutput", "PKUMMD"),
}
option_flag = {
    "config_file_path": "--config",
    "input_path": "--input",
    "output_folder": "--output",
}
options = {
    "config_file_path": None,
    "input_path": None,
    "output_folder": None,
}

extra_options = {
    "single_file": False,
}

flags = {
    "-c": "config_file_path",
    "--config": "config_file_path",
    "-i": "input_path",
    "--input": "input_path",
    "-o": "output_folder",
    "--output": "output_folder",
}


# This function will either launch the GUI or operate as a CLI.
# Functionality is determined by the number of command line arguments.
def main():
    # Load in command line arguments
    command_line_arguments = sys.argv

    global options, extra_options

    nice_msg("Parsing the following arguments: " + str(command_line_arguments[1:]))
    # If the --gui field is present in the command line arguments, open the GUI
    if "--gui" in command_line_arguments or '-g' in command_line_arguments:
        if len(command_line_arguments) > 2:
            print("Starting GUI and ignoring other command line arguments")
        gui.start_gui()
        # The GUI and the CLI are not setup to work in tandem, thus for each instance of the program the user can
        # only start one of them. Therefore end the main function if start the gui
        return

    # If the --input field is present in the command line arguments, update the input directory
    overwriting = None
    for opt in flags.keys():
        if opt in command_line_arguments:
            idx = command_line_arguments.index(opt)
            if idx >= len(command_line_arguments) - 1:
                error(blue(opt) + " field incorrectly specified." +
                      " The " + blue(opt) + " option takes exactly one parameter. Zero given.")
                return
            value = command_line_arguments[idx + 1]
            # delete opt
            command_line_arguments.pop(idx)
            # delete value
            command_line_arguments.pop(idx)
            option_to_set = flags[opt]
            if options[option_to_set] is not None:
                warn("The " + blue(option_to_set) + " is being overwritten.\n\t" +
                     blue(option_to_set) + " is now set to " + blue(value) + " (argument of " + blue(opt) + ")")
            options[option_to_set] = value

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
        if re.match(single_char_switch, arg):
            warn(arg + " is not a recognised switch and is being ignored")
            command_line_arguments.pop(idx)
        elif re.match(too_many_chars, arg):
            warn(
                arg + " is not a recognised switch and is being ignored.\n\tNOTE: multi character switches begin with "
                      "two dashes, e.g. --config, wheras single character switches begin with one dash, e.g -c")
            command_line_arguments.pop(idx)
        elif re.match(multi_char_switch, arg):
            warn(arg + " is not a recognised switch and is being ignored.")
            command_line_arguments.pop(idx)
        else:
            idx += 1

    # Consume remaining arguments
    if len(command_line_arguments) > 0:
        # Assign remaining options in default order
        for opt in options.keys():
            if len(command_line_arguments) == 0:
                break
            if options[opt] is None:
                options[opt] = command_line_arguments[0]
                command_line_arguments.pop(0)

    # Use default_options for any options that are still None
    for opt in options.keys():
        if options[opt] is None:
            warn("Using default " + opt + ": " + default_options[opt] + "\n\tUse " + blue(
                option_flag[opt] + " <" + opt + ">") + " to set the " + opt + " manually.")
            options[opt] = default_options[opt]

    if len(command_line_arguments) > 0:
        # Show command line arguments that weren't consumed.
        # The first argument should not have been consumed. It is the name of the program that was called.
        warn("The following command line arguments were not matched in any pattern and were not loaded: ")
        print(command_line_arguments)

    # Are we converting a whole folder or just a single file?
    if os.path.isfile(options["input_path"]):
        extra_options["single_file"] = True
    elif not os.path.isdir(options["input_path"]):
        error(blue(options["input_path"]) + " is neither a file nor a folder. Aborting.")
        sys.exit(-1)


    try:
      x = configuration.Configuration(options["config_file_path"])
    except OSError as e:
        error(str(e) + ": OSError raised while loading config from " + blue(options["config_file_path"]))
    except ValueError as e:
        error(str(e) + ": ValueError raised while loading config from " + blue(options["config_file_path"]))
    except Exception as e:
        error(str(e) + ": An unknown error has occurred while loading config from " + blue(options["config_file_path"]))

    if os.path.isfile(options["output_folder"]):
        error(blue(options["output_folder"]) + " is a file. " + blue("output_folder") + " (given by " + 
              blue("-o") + " or " + blue("--output") + " must be a folder.")
    if not os.path.exists(options["output_folder"]):
        try:
            os.makedirs(options["output_folder"])
        except OSError as e:
            error(str(e) + " Failed to create output directory " + options["output_folder"])
        except Exception as e:
            error(str(e) + " An unknown fatal error has occurred while trying to creat the output folder " + blue(
                options["output_folder"]))
    
    options["output_folder"] = os.path.abspath(options["output_folder"])

    # Convert all csv files in the input directory
    if x.config["Structure"] == "Vertical":
      os.chdir(options["input_path"]) 
      recursive_convert_vertical(".",
                                 options["output_folder"], x)
    elif x.config["Structure"] == "NTU":
      recursive_convert_ntu(options["input_path"],
                            os.path.abspath(options["output_folder"]), x)
    else:
      error("No Structure provided in config.json. Possible Structure values are: \"Vertical\", \"NTU\"")


def recursive_convert_vertical(input, output, config):
  for file_or_dir in os.listdir('.'):
    if os.path.isdir(file_or_dir):
      nice_msg("Descending into " + blue(os.path.abspath(input)))
      os.chdir(os.path.abspath(file_or_dir))
      print(os.path.join(output, file_or_dir))
      recursive_convert_vertical( os.getcwd(),
                                  os.path.join(output, file_or_dir), config)
      nice_msg("Ascending back to " + blue(os.path.abspath(os.pardir)))
      os.chdir(os.pardir)
    elif os.path.isfile(file_or_dir) and file_or_dir.endswith(config.config["FileExtension"]):
      base = os.path.splitext(file_or_dir)[0]
      nice_msg("Converting: " + os.path.join(input, file_or_dir) + blue(" into ") + "\n\t" + os.path.join(output, base + ".json"))
      if not os.path.exists(output):
        os.makedirs(output)
      converter.convert_vertical(os.path.join(input,file_or_dir),
                       os.path.join(output, base + ".json"), config)

def recursive_convert_ntu(input, output, config):
  for file_or_dir in os.listdir('.'):
    if os.path.isdir(file_or_dir):
      nice_msg("Descending into " + blue(os.path.abspath(input)))
      os.chdir(os.path.abspath(file_or_dir))
      print(os.path.join(output, file_or_dir))
      recursive_convert_ntu( os.getcwd(),
                                  os.path.join(output, file_or_dir), config)
      nice_msg("Ascending back to " + blue(os.path.abspath(os.pardir)))
      os.chdir(os.pardir)
    elif os.path.isfile(file_or_dir) and file_or_dir.endswith(config.config["FileExtension"]):
      base = os.path.splitext(file_or_dir)[0]
      nice_msg("Converting: " + os.path.join(input, file_or_dir) + blue(" into ") + "\n\t" + os.path.join(output, base + ".json"))
      if not os.path.exists(output):
        os.makedirs(output)
      converter.convert_ntu(os.path.join(input,file_or_dir),
                       os.path.join(output, base + ".json"), config)


if __name__ == "__main__":
    # Here's how we could change to the src directory if the user is calling the program from another directory.
    # At the moment we're not set up to handle this.
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
    print(colorama.Fore.GREEN + "\n\tFinished!" + colorama.Style.RESET_ALL)
