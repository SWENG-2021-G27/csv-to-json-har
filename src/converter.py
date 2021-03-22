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
      # Read file with space seperated columns
      with open(os.path.abspath(filename), "r") as f:
        row_idx = 0
        frame = 0

        line = f.readline()
        for line in f:
          if row_idx >= c.config["StartRow"]:
                  # TODO this implementation is only handling the first skeleton in pkummd and throwing out the second
                  row = line.split()
                  
                  # Write the frame field
                  if frame > 0:
                      out.write(",")
                  out.write("{\\\"f\\\":")
                  out.write(str((frame + 1) * 33))
                  out.write(",")

                  # Write the joint information appropriately
                  out.write("\\\"b\\\":{\\\"i\\\":" + str(frame + 1) + ",")
                  out.write("\\\"j\\\":[")
                  

                  for joint in joint_order:
                      out.write("{\\\"s\\\":2,")
                      out.write("\\\"p\\\":\\\"("
                                + str(float(row[c.config["Joints"][joint]["x"]])*100).strip() + ","
                                + str(float(row[c.config["Joints"][joint]["y"]])*100).strip() + ","
                                + str(float(row[c.config["Joints"][joint]["z"]])*100).strip() + ")\\\",")
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

                  frame = frame + 1
                  out.write("}")


          row_idx += 1  
      out.write("]}\"}")
    
    else:
      # Read every row of the csv and process the data accordingly
      with open(filename) as f:
          row_idx = 0
          frame = 0
          for row in csv.reader(f):
              if row_idx > c.config["StartRow"]:
                  # Write the frame field
                  if frame > 0:
                      out.write(",")
                  out.write("{\\\"f\\\":")
                  out.write(str((frame + 1) * 33))
                  out.write(",")

                  # Write the joint information appropriately
                  out.write("\\\"b\\\":{\\\"i\\\":" + str(frame + 1) + ",")
                  out.write("\\\"j\\\":[")
                  

                  for joint in joint_order:
                      out.write("{\\\"s\\\":2,")
                      out.write("\\\"p\\\":\\\"("
                                + str(row[c.config["Joints"][joint]["x"]]).strip() + ","
                                + str(row[c.config["Joints"][joint]["y"]]).strip() + ","
                                + str(float(row[c.config["Joints"][joint]["z"]])+200).strip() + ")\\\",")
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

                  frame = frame + 1
                  out.write("}")

              row_idx = row_idx + 1

          out.write("]}\"}")
