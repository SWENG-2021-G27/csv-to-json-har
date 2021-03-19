# configuration.py

import json


# A configuration class that holds information about the file being converted
class Configuration:
    config = {
        "Device": 3,  # Default to 3 for other (not kinect) device
        "Ground": (0, 1, 0, 0.6),  # Default to (0, 1, 0 , 0.6) for ground
        "Offset": 0,
        "NumberOfSkeletons": 1,  # Default to one skeleton per file
        "NumberOfJoints": 19,  # Default to 19 joints per file (19 joints in the JSON output)
        "Structure": "Vertical",  # Default to joint positions going down
        "StartRow": 0,
        "Frames": {
            "FramesInfo": False,  # Flag to say if there is timing data in the file
            "FrameIdx": -1  # If there is timing data in the file, it is in this column
        },
        "Joints": {  # These are the order of the joints in the file
            "Head": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "Neck": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftShoulder": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightShoulder": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftElbow": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightElbow": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftWrist": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightWrist": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftHand": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightHand": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "TopSpine": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "MidSpine": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "BaseSpine": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftHip": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightHip": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftKnee": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightKnee": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "LeftFoot": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
            "RightFoot": {
                "x": -1,
                "y": -1,
                "z": -1,
            },
        }
    }

    def __init__(self, input_file):
        with open(input_file) as f:
            data = json.load(f)

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

        if "StartRow" in data:
            self.config["StartRow"] = data["StartRow"]

        if "Offset" in data:
            self.config["Offset"] = data["Offset"]

        if "Frames" in data:
            if data["Frames"]["FramesInfo"]:
                self.config["Frames"]["FramesInfo"] = True
                self.config["Frames"]["FrameIdx"] = data["Frames"]["FrameIdx"]

        self.config["Joints"] = data["Joints"]
