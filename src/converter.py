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


# hard load pkummd data sample
def hard_load_pkummd():
    f = open("../datasamples/pkummd/v1/A10N08-L.txt", "r") 
    return f

def pkummd_read_joints_from_line(line):
    two_skeletons_ascii = line.split()
    if(len(two_skeletons_ascii) != 150):
      print("Unexpected number of floats in line")
    joints1 = []
    for i in range(25):
      xn_ascii = two_skeletons_ascii[(3*i)]     # 0, 3, 6, 9 etc...
      yn_ascii = two_skeletons_ascii[(3*i) + 1] # 1, 4, 7, 10 etc...
      zn_ascii = two_skeletons_ascii[(3*i) + 2] # 2, 5, 8, 11 etc...
      joints1.append([xn_ascii, yn_ascii, zn_ascii])
    
    return (joints1)

def array_of_ascii_floats_to_json_tuple(a):
  json = "(" + a[0]  #DIRTY DIRTY HACK TODO fix this fucker
  for i in range(len(a) - 1):
    json += a[i+1] + ","
  json += ")"
  return json

def position_ascii_tuple_to_json(ascii_tuple):
  return '\\"p\\": \\"' + ascii_tuple + '\\"'    

f = hard_load_pkummd()
joints1 = pkummd_read_joints_from_line(f.readline())

joints_json = '\\"j\\": ['
count = 0
for json_tuple in  map(array_of_ascii_floats_to_json_tuple, joints1):
   joints_json += '{\\"s\\":2,\\"p\\":\\"(0.809, 19.154, 269.086)\\",\\"q\\":\\"(0.5, 0.4)\\",\\"o\\":\\"(0.000, 0.000, 0.000, 0.000)\\"},{\\"s\\":2,\\"p\\":\\"' + json_tuple + '\\",\\"q\\":\\"(0, 0)\\",\\"o\\":\\"(0, 0, 0, 0)\\"}'
   count += 1
   if (count == 19):
      break
   joints_json += ',\n'

joints_json +=  "]"
print( joints_json )

