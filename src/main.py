# main.py
import sys
from gui import *
from converter import *


def main():
    if len(sys.argv) < 2:
        print("In GUI")
        start_gui()
    else:
        print(cli())
        print("Command Line Arguments: " + str(sys.argv))


if __name__ == "__main__":
    main()
