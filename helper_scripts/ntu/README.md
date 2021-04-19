# MRSC-12: Kinect Gesture Dataset

### Repository Contents
This folder has the following structure:
```
.
├── download_ntu.py
├── extract_ntu.py
├── generate_jpgs_from_test_output.py
├── jpgs
│   ├...
│   ...
├── README.md
├── Shahroudy_NTU_RGBD_A_CVPR_2016_paper.pdf
├── TestData
│   ├── config.json
│   ├── S001C001P001R001A001.skeleton
│   ├── S001C001P001R001A002.skeleton
│   ├── S001C001P001R001A003.skeleton
│   ├── S001C001P001R001A004.skeleton
│   └── S001C001P001R001A005.skeleton
├── TestOutput
│   ├── S001C001P001R001A001.json
│   ├── S001C001P001R001A002.json
│   ├── S001C001P001R001A003.json
│   ├── S001C001P001R001A004.json
│   └── S001C001P001R001A005.json
├── tree.md
└── Verified
    ├── S001C001P001R001A001.json
    ├── S001C001P001R001A002.json
    ├── S001C001P001R001A003.json
    ├── S001C001P001R001A004.json
    └── S001C001P001R001A005.json
```

### Verified output
Any time you check the generated images from a <file>.json you should put the json in Verified if you are happy with it.
If the output for that file changes during development it'll be picked up when you run `consistency_check.py` in the `helper_scripts` directory.


### Config
`TestData/config.json` is a configuration file that can be used to convert the NTU Dataset into a series of 
appropriate JSON files for animation using the conversion application.
Note that most of the joints are in the order {z,y,x} but the BaseSpine joint is in the order {x,y,z}. We have no idea why it's like this.
The format of the NTU dataset is supposed to be the same as the NTU dataset as described in `Shahroudy_NTU_RGBD_A_CVPR_2016_paper.pdf` but there are some differences.

### Scripts
`download_ntu.py` is a python script that will download the Motion Capture Dataset into a new 
folder in the `../../RawDatasets` folder called `NTU`. This folder will hold a `.zip` file.

`extract_ntu.py` is a python script that will unzip the `.zip` file in the `RawDatasets/NTU` folder.

`convert_TestData.py` will convert the files in `TestData` to json putting them in `TestOutput`

`generate_jpgs_from_test_output.py` will generate images from the JSON files in `TestOutput` writing them to `jpgs`.
