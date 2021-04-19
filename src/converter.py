# converter.py
# This file will contain the source code for converting csv files to json

import csv
import os


# A function that returns "In CLI". This function is called in main.py to signify that the GUI has not been started.
def cli():
    return "In CLI"


joint_order = ["Head",
               "Neck",
               "LeftShoulder",
               "RightShoulder",
               "LeftElbow",
               "RightElbow",
               "LeftWrist",
               "RightWrist",
               "LeftHand",
               "RightHand",
               "TopSpine",
               "MidSpine",
               "BaseSpine",
               "LeftHip",
               "RightHip",
               "LeftKnee",
               "RightKnee",
               "LeftFoot",
               "RightFoot"]


# A function which converts a vertically aligned csv to the strict json required
def convert_vertical(filename, output, c):
    # Open the output file in write mode and write the header fields of the json
    out = open(output, "w")
    out.write("{\"d\":" + str(c.config["Device"]) + ","
              + "\"g\":\"(" + str(c.config["Ground"][0]) + "," + str(c.config["Ground"][1]) + "," + str(
        c.config["Ground"][2]) + "," + str(c.config["Ground"][3]) + ")\","
              + "\"o\":\"" + str(c.config["Offset"]) + "\","
              + "\"t\":\"{\\\"Items\\\":[")
    
    if(c.config["ColumnSeperator"] == "Spaces"):
      column_separator = None # the default separator for str.split() is any whitespace so we can use the default
    else: # default column separator is comma
      column_separator = ','
    
   
    # Read every row of the csv (or other filetype) and process the data accordingly
    with open(filename) as f:
      row_idx = 0
      frame = 0
      for line in f:
        row = line.split(column_separator)
        if row_idx > c.config["StartRow"]:
          # Write the frame field
          if frame > 0:
            out.write(",")
          out.write("{\\\"f\\\":")

          if c.config["Frames"]["FramesInfo"]:
            time = row[c.config["Frames"]["FrameIdx"]]
            if frame >= int(float(time) * 33):
              frame = frame + 1
            else:
              frame = int(float(time) * 33)
            out.write(str(frame))
          else:
            out.write(str((frame + 1) * 33))
            frame = frame + 1

          out.write(",")

          # Write the joint information appropriately
          out.write("\\\"b\\\":{\\\"i\\\":" + str(frame + 1) + ",")
          out.write("\\\"j\\\":[")

          for joint in joint_order:
            out.write("{\\\"s\\\":" + str(c.config["Joints"][joint]["status"]).strip() + ",")
            out.write(
             "\\\"p\\\":\\\"(" 
             + str(
              float(row[c.config["Joints"][joint]["x-column"]]) * float(c.config["magnify"]["x"])
              + float(
                c.config["x-offset"]
              )
             ).strip() + ","
             + str(
              float(row[c.config["Joints"][joint]["y-column"]]) * float(c.config["magnify"]["y"])
              + float(
                c.config["y-offset"]
              )
             ).strip() + ","
             + str(
              float(
                row[c.config["Joints"][joint]["z-column"]]) * float(c.config["magnify"]["z"])
                + float(
                  c.config["z-offset"]
                )
             ).strip()
             + ")\\\","
            )
            out.write("\\\"q\\\":\\\"(0,0)\\\",")
            out.write("\\\"o\\\":\\\"(0,0,0,0)\\\"}")
            if joint != joint_order[len(joint_order) - 1]:
              out.write(",")

          out.write("],")
          out.write("\\\"r\\\":0,")
          out.write("\\\"l\\\":0,")
          out.write("\\\"_negativeGroundOffset\\\":0.0,")
          out.write("\\\"_previousNegativeGroundOffset\\\":0.0")
          out.write("}")
          out.write("}")

        row_idx = row_idx + 1

      out.write("]}\"}")


# A function which converts a vertically aligned csv to the strict json required
def convert_ntu(filename, output, c):
    body_id_and_file = {}
  
    # Open the output file in write mode and write the header fields of the json
    out = open(output, "w")
    out.write("{\"d\":" + str(c.config["Device"]) + ","
              + "\"g\":\"(" + str(c.config["Ground"][0]) + "," + str(c.config["Ground"][1]) + "," + str(
        c.config["Ground"][2]) + "," + str(c.config["Ground"][3]) + ")\","
              + "\"o\":\"" + str(c.config["Offset"]) + "\","
              + "\"t\":\"{\\\"Items\\\":[")
    
    if(c.config["ColumnSeperator"] == "Spaces"):
      column_separator = None # the default separator for str.split() is any whitespace so we can use the default
    else: # default column separator is comma
      column_separator = ','
    
   
    # Read every row of the csv (or other filetype) and process the data accordingly
    with open(filename) as f:
      framecount = int(f.readline())
      for frame in range(framecount):
       bodycount = int(f.readline())
       for body_number in range(bodycount):
          body_meta_data = f.readline()
          body_meta_data = body_meta_data.split(column_separator)
          bodyID = body_meta_data[0]
          trackingState = body_meta_data[9]
          number_of_joints = int(f.readline()) 

          # Write the frame field
          if frame > 0:
            out.write(",")
          out.write("{\\\"f\\\":")

          out.write(str((frame + 1) * 33))
          frame = frame + 1

          out.write(",")

          # Write the joint information appropriately
          out.write("\\\"b\\\":{\\\"i\\\":" + str(bodyID) + ",")
          out.write("\\\"j\\\":[")
          
          all_joints  = []

          for joint in range(number_of_joints):
            joint_info = f.readline().split(column_separator)
            x = str(joint_info[0]).strip()
            y = str(joint_info[1]).strip()
            z = str(joint_info[2]).strip()
            trackingState = str(joint_info[len(joint_info) -1]).strip()
            joint_info = {
                "x": x,
                "y": y,
                "z": z,
                "trackingState": trackingState}
            all_joints.append(joint_info)

          for joint in joint_order:
            ntu_joint = all_joints[int(c.config["JointMap"][joint])]
            out.write("{\\\"s\\\":" + ntu_joint["trackingState"] + ",")
            out.write(
             "\\\"p\\\":\\\"(" 
             + str(
              float(ntu_joint["x"]) * float(c.config["magnify"]["x"])
              + float(
                c.config["x-offset"]
              )
             ).strip() + ","
             + str(
              float(ntu_joint["y"]) * float(c.config["magnify"]["y"])+ float(c.config["y-offset"])).strip() + ","
             + str(
              float(ntu_joint["z"]) * float(c.config["magnify"]["z"])
                + float(
                  c.config["z-offset"]
                )
             ).strip()
             + ")\\\","
            )
            out.write("\\\"q\\\":\\\"(0,0)\\\",")
            out.write("\\\"o\\\":\\\"(0,0,0,0)\\\"}")
            if joint != joint_order[len(joint_order) - 1]:
              out.write(",")

          out.write("],")
          out.write("\\\"r\\\":0,")
          out.write("\\\"l\\\":0,")
          out.write("\\\"_negativeGroundOffset\\\":0.0,")
          out.write("\\\"_previousNegativeGroundOffset\\\":0.0")
          out.write("}")
          out.write("}")

      out.write("]}\"}")
