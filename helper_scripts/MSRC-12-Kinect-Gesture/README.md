# MRSC-12: Kinect Gesture Dataset

### Repository Contents
This folder has the following structure:
````
CMU-Mocap
|- TestData
    |- config.json
    |- <several MRSC-12 mocap files for testing>
|- TestOutput
    |- <potentially json output files>
|- Verified
    |- <copies from TestOutput that have been checked by a human>
|- download_MicrosoftGestureDataset.py
|- unzip_MSRC.py
````
`TestData/config.json` is a configuration file that can be used to convert the MRSC-12: Kinect Gesture Dataset into a series of 
appropriate JSON files for animation using the conversion application.

`download_MicrosoftGestureDataset.py` is a python script that will download the CMU Motion Capture Dataset into a new 
folder in the `./RawDatasets` folder called `MSRC-Kinect`. This folder will hold a `.zip` file.

`unzip_MSRC.py` is a python script that will unzip the `.zip` file in the `MSRC-Kinect` folder.