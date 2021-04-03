# main.py

from gui import *
from converter import *
from configuration import *
import sys
import os.path

input_directory = "..\\RawDatasets"  # Default input directory
config_file = "..\\RawDatasets\\config.json"  # Default config file
output_directory = "..\\RawDatasets\\Output"  # Default output directory


# This function will either launch the GUI or operate as a CLI.
# Functionality is determined by the number of command line arguments.
def main():
    # Load in command line arguments
    command_line_arguments = sys.argv

    # If the -gui field is present in the command line arguments, open the GUI
    if "-gui" in command_line_arguments:
        start_gui()
    else:
        global input_directory
        global config_file
        global output_directory

        # If the -input field is present in the command line arguments, update the input directory
        if "-input" in command_line_arguments:
            idx = command_line_arguments.index("-input")
            if idx >= len(command_line_arguments) - 1:
                print("\n    [ERROR]: -input field incorrectly specified")
                return
            elif not os.path.exists(command_line_arguments[idx + 1]):
                print("\n    [ERROR]: -input path does not exist")
                return
            elif not os.path.isdir(command_line_arguments[idx + 1]):
                print("\n    [ERROR]: -input path is not a directory")
                return

            input_directory = command_line_arguments[idx + 1]
            config_file = input_directory + "\\config.json"
            output_directory = input_directory + "\\Output"

        # If the -config field is present in the command line arguments
        if "-config" in command_line_arguments:
            idx = command_line_arguments.index("-config")
            if idx >= len(command_line_arguments) - 1:
                print("\n    [ERROR]: -config field incorrectly specified")
                return
            elif not os.path.exists(command_line_arguments[idx + 1]):
                print("\n    [ERROR]: -config path does not exist")
                return
            elif not os.path.isfile(command_line_arguments[idx + 1]):
                print("\n    [ERROR]: -config path is not a file")
                return
            elif not command_line_arguments[idx + 1].endswith(".json"):
                print("\n    [ERROR]: -config file is not a json")
                return

            config_file = command_line_arguments[idx + 1]

        # If the -input field is present in the command line arguments, update the output directory
        if "-output" in command_line_arguments:
            idx = command_line_arguments.index("-output")
            if idx >= len(command_line_arguments) - 1:
                print("\n    [ERROR]: -output field incorrectly specified")
                return

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
    main()
    print("Finished!")
