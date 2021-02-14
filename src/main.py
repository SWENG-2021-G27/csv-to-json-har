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


if __name__ == "__main__":
    main()
