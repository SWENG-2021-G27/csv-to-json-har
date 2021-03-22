#converter.py
# This file will contain the source code for converting csv files to json
import json
import os
import map_joints
import itertools


def generate_valid_json_for_single_frame_with_mapping(mapping=list(range(19)),
          input_file="../datasamples/pkummd/v1/A10N08-L.txt",
          out="./pkummd_out/default.json"):
    f = open(input_file)    
    line = f.readline()
    f.close()

    joints = pkummd_read_joints_from_line(line)
    
    mapped_joints = map_joints.map_n_joints_to_19(mapping, joints) 
    print(str(len(mapped_joints)) + str(mapped_joints))
    with open(out, 'w+') as out_file:
      # HEADER json header
      out_file.write("{\"d\":2,\"g\":\"(0.027, 0.994, 0.106, 0.505)\",\"o\":\"0.075\",\"t\":\"{\\\"Items\\\":[{\\\"f\\\":12,\\\"b\\\":{\\\"i\\\":72057594037931204,")
      
      # JOINTS
      out_file.write( '\\"j\\": [')
      count = 0
      for json_tuple in  map(array_of_floats_to_json_tuple, mapped_joints):
         out_file.write( '{\\"s\\":2,\\"p\\":\\"(0.809, 19.154, 269.086)\\",\\"q\\":\\"(0.5, 0.4)\\",\\"o\\":\\"(0.000, 0.000, 0.000, 0.000)\\"},{\\"s\\":2,\\"p\\":\\"' + json_tuple + '\\",\\"q\\":\\"(0, 0)\\",\\"o\\":\\"(0, 0, 0, 0)\\"}')
         count += 1
         if (count == 19):
            break
         out_file.write( ',')
      
      out_file.write( "]")
      
      # FOOTER

      out_file.write(',\\"r\\":0,\\"l\\":0,\\"_negativeGroundOffset\\":0.0,\\"_previousNegativeGroundOffset\\":0.0}}]}"}')


def all_possible_mappings_as_iterable():
    return itertools.permutations(list(range(19))+[-1,-1,-1,-1,-1,-1])

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
      joints1.append([float(xn_ascii), float(yn_ascii), float(zn_ascii)])
    
    return (joints1)

def array_of_floats_to_json_tuple(a):
  json = "(" + str(a[0])#DIRTY DIRTY HACK TODO fix this fucker
  for i in range(len(a) - 1):
    json += ',' + str(a[i+1])
  json += ")"
  return json

def position_ascii_tuple_to_json(ascii_tuple):
  return '\\"p\\": \\"' + ascii_tuple + '\\"'    



mapping = [12, 11, 1, 0, 2, 4, 8, 6, 3, 5, 9, 7, 13, 15, 17, -1, 14, 16, 18, -1, 10, -1 ,-1, -1, -1]
print(len(mapping))
generate_valid_json_for_single_frame_with_mapping(mapping=mapping,out="pkummd_out/1.json")
"""
# creating a file for each of all the possible mappings

map_number = 0
map1 = list(range(19)) + [-1,-1,-1,-1,-1,-1]
map1.reverse()
for mapping in itertools.permutations(map1):
  generate_valid_json_for_single_frame_with_mapping(mapping=mapping,out="pkummd_out/" + str(map_number).zfill(15) + ".json")
  with open("pkummd_out/" + str(map_number).zfill(15) + ".map",'w+') as f:
    f.write(str(mapping)) 
  map_number += 1
  if map_number > 100:
    break
"""
