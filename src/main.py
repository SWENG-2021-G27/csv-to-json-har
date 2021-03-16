# main.py

from gui import *
from converter import *
from configuration import *
import sys


# This function will either launch the GUI or operate as a CLI.
# Functionality is determined by the number of command line arguments.
def main():
    if len(sys.argv) < 2:
        print("In GUI")
        start_gui()
    else:
        x = Configuration(sys.argv[1])
        if x.config["Structure"] == "Vertical":
            convert_vertical(sys.argv[2], x, sys.argv[3])
        else:
            print("Error")


if __name__ == "__main__":
    main()
