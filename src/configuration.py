# configuration.py

import json


# A configuration class that holds information about the file being converted
class Configuration:
    config = {
        "Device": 3,  # Default to 3 for other (not kinect) device
        "Ground": (0, 1, 0, 0.6),  # Default to (0, 1, 0 , 0.6) for ground
        "Offset": 0,
        "Structure": "Vertical",  # Default to joint positions going down
        "ColumnSeperator": "Comma",
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
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "Neck": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftShoulder": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightShoulder": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftElbow": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightElbow": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftWrist": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightWrist": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftHand": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightHand": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "TopSpine": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "MidSpine": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "BaseSpine": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftHip": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightHip": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftKnee": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightKnee": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "LeftFoot": {
                "x": -1,
                "y": -1,
                "z": -1,
                "status": 1
            },
            "RightFoot": {
                "x": -1,
                "y": -1,
                "z": -1,
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
