# converter.py
# This file will contain the source code for converting csv files to json

import csv


# A function that returns "In CLI". This function is called in main.py to signify that the GUI has not been started.
def cli():
    return "In CLI"


# A function which converts a vertically aligned csv to the strict json required
def convert_vertical(filename, c, output):
    with open(filename) as f:
        row_idx = 0
        for row in csv.reader(f):
            if row_idx > c.config["StartRow"]:
                print(row[0])
            row_idx = row_idx + 1
