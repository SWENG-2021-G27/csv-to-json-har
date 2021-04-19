# MRSC-12: Kinect Gesture Dataset

### Repository Contents
This folder has the following structure:
````
pkummd
|- download_pkummd_Skeleton7z.py
|- extract_pkummd_Skeleton7z.py
|- convert_TestData.py
|- generate_pngs_from_test_output.py
|- README.md

````
`config.json` is a configuration file that can be used to convert the MRSC-12: Kinect Gesture Dataset into a series of 
appropriate JSON files for animation using the conversion application.

`download_MicrosoftGestureDataset.py` is a python script that will download the CMU Motion Capture Dataset into a new 
folder in the `./RawDatasets` folder called `MSRC-Kinect`. This folder will hold a `.zip` file.

`unzip_MSRC.py` is a python script that will unzip the `.zip` file in the `MSRC-Kinect` folder.
