# configuration.py

import json
import sys
import ERROR


# A configuration class that holds information about the file being converted
class Configuration:
    config = {
        "Device": 3,  # Default to 3 for other (not kinect) device
        "Ground": (0, 1, 0, 0.6),  # Default to (0, 1, 0 , 0.6) for ground
        "Offset": 0,
        "Structure": "Vertical",  # Default to joint positions going down
        "ColumnSeparator": "Comma",
        "StartRow": 0,
        "Frames": {
            "FramesInfo": False,  # Flag to say if there is timing data in the file
            "FrameIdx": -1  # If there is timing data in the file, it is in this column
        },
        "x-offset": 0,
        "y-offset": 0,
        "z-offset": 0,
        "magnify": {
            "x": 1,
            "y": 1,
            "z": 1
        },
        "FileExtension": ".csv",
        "Joints": {  # These are the order of the joints in the file
            "Head": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "Neck": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftShoulder": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightShoulder": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftElbow": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightElbow": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftWrist": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightWrist": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftHand": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightHand": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "TopSpine": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "MidSpine": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "BaseSpine": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftHip": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightHip": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftKnee": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightKnee": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "LeftFoot": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
            "RightFoot": {
                "x-column": -1,
                "y-column": -1,
                "z-column": -1,
                "n": -1,
                "status": 1
            },
        },
        "JointMap": {
            "Head": -1,
            "Neck": -1,
            "LeftShoulder": -1,
            "RightShoulder": -1,
            "LeftElbow": -1,
            "RightElbow": -1,
            "LeftWrist": -1,
            "RightWrist": -1,
            "LeftHand": -1,
            "RightHand": -1,
            "TopSpine": -1,
            "MidSpine": -1,
            "BaseSpine": -1,
            "LeftHip": -1,
            "RightHip": -1,
            "LeftKnee": -1,
            "RightKnee": -1,
            "LeftFoot": -1,
            "RightFoot": -1
        }
    }
    

    def render_path(self,prefix):
      return self.render_path_rec(prefix)
    
    def render_path_rec(self,prefix):
      try:
        key = prefix[0]
        return "\"" + key + "\":" + self.render_path_rec(prefix[1:])
      except:
        return "<value>"

    def load(self, data):
      for key in data.keys():
        self.recursive_load([key], data[key], self.config, key)

 
    def recursive_load(self, path_so_far,data, target, key):
      if isinstance(data, dict):
        for k in data.keys():
          backup_path = path_so_far.copy()
          if k in target[key]:
            path_so_far.append(k)
            self.recursive_load(path_so_far,data[k],target[key], k)
          else:
            backup_path = path_so_far.copy()
            path_so_far.append(k)
            print(self.render_path(path_so_far) + " is not a valid configuration key")
            path_so_far = backup_path
          path_so_far = backup_path
      else:
        target[key] = data
        print( self.render_path(path_so_far) + " is now " + str(target[key]))  
    def set(self,path,value):
      self.config 

    def __init__(self, input_file):
        with open(input_file) as f:
          try:
            data = json.load(f)
          except Exception as e:
            print("Exception raised while loading json data: " +str(e) + " Aborting.")
            sys.exit(-1)
   

        self.load(data)
        """
        #                   array of keys starts as an empty list and is appended for deeply nested dicts
                            [], 
    
        #                   data loaded for 
                            data,

        #                   target to load data into
                            self.config,
        
        #                   current key to load into, starts as None
                            None) 
        """

        print("Using the following configuration:\n" + str(self.config))

        # THE OLD WAY
        """
        if "Device" in data:
            self.config["Device"] = data["Device"]

        if "Ground" in data:
            self.config["Ground"] = data["Ground"]

        if "NumberOfSkeletons" in data:
            self.config["NumberOfSkeletons"] = data["NumberOfSkeletons"]

        if "NumberOfJoints" in data:
            self.config["NumberOfJoints"] = data["NumberOfJoints"]

        if "Structure" in data:
            self.config["Structure"] = data["Structure"]

        if "ColumnSeperator" in data:
            self.config["ColumnSeperator"] = data["ColumnSeperator"]

        if "StartRow" in data:
            self.config["StartRow"] = data["StartRow"]

        if "Offset" in data:
            self.config["Offset"] = data["Offset"]

        if "Frames" in data:
            if data["Frames"]["FramesInfo"]:
                self.config["Frames"]["FramesInfo"] = True
                self.config["Frames"]["FrameIdx"] = data["Frames"]["FrameIdx"]

        if "x-offset" in data:
            self.config["x-offset"] = data["x-offset"]

        if "y-offset" in data:
            self.config["y-offset"] = data["y-offset"]

        if "z-offset" in data:
            self.config["z-offset"] = data["z-offset"]

        if "magnify" in data:
            self.config["magnify"] = data["magnify"]

        if "FileExtension" in data:
            self.config["FileExtension"] = data["FileExtension"]

        if "Joints" in data:
            self.config["Joints"] = data["Joints"]

        if "JointMap" in data:
            self.config["JointMap"] = data["JointMap"]
        """
