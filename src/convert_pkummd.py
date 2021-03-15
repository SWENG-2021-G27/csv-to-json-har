# converter.py
# This file will contain the source code for converting csv files to json
import json
import os

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

