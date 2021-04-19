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
|- Sharoudy_NTU_RGBD_A_CVPR_2016_paper.pdf
|- TestData
    |- config.json
    |- <several pkummd mocap files for testing>
|- TestOutput
    |- <potentially json output files>
|- Verified
    |- <copies from TestOutput that have been checked by a human>
|- pngs
    |- <potentially many images created by the generate_pngs_from_test_output.py script>
````

`TestData/config.json` is a configuration file that can be used to convert the PKUMMD Dataset into a series of 
appropriate JSON files for animation using the conversion application.
Note that most of the joints are in the order {z,y,x} but the BaseSpine joint is in the order {x,y,z}. We have no idea why it's like this.
The format of the PKUMMD dataset is supposed to be the same as the NTU dataset as described in `Shahroudy_NTU_RGBD_A_CVPR_2016_paper.pdf` but there are some differences.

`download_pkummd_Skeleton7z.py` is a python script that will download the Motion Capture Dataset into a new 
folder in the `../../RawDatasets` folder called `PKUMMD`. This folder will hold a `.zip` file.

`extract_pkummd_Skeleton7z.py` is a python script that will unzip the `.zip` file in the `RawDatasets/PKUMMD` folder.

`convert_TestData.py` will convert the files in `TestData` to json putting them in `TestOutput`

`generate_jpgs_from_test_output.py` will generate images from the JSON files in `TestOutput` writing them to `jpgs`.
