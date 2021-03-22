# converter.py
# This file will contain the source code for converting csv files to json

import csv


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
                    out.write("\\\"p\\\":\\\"(" + str(
                        float(row[c.config["Joints"][joint]["x"]]) + float(c.config["x-offset"])).strip() + ","
                              + str(
                        float(row[c.config["Joints"][joint]["y"]]) + float(c.config["y-offset"])).strip() + ","
                              + str(
                        float(row[c.config["Joints"][joint]["z"]]) + float(c.config["z-offset"])).strip() + ")\\\",")
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
