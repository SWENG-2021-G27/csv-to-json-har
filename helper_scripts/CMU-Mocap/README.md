# CMU Motion Capture Dataset

### Repository Contents
This folder has the following structure:
````
CMU-Mocap
|- TestData
| |- config.json
|- download.py
|- bvh_to_csv.py
````
`TestData/config.json` is a configuration file that can be used to convert the CMU Motion Capture Dataset into a series of 
appropriate JSON files for animation using the conversion application.

`download.py` is a python script that will download the CMU Motion Capture Dataset into a new folder in the `./RawDatasets` 
folder called `CMU-Data-BVH`. The files in this dataset are in `.bvh` format.

`bvh_to_csv.py` is a python script that will convert all of the `.bvh` files in the `CMU-Data-BVH` folder to `.csv` 
files that are ready for conversion. This script uses the [bvh-toolbox](https://github.com/OlafHaag/bvh-toolbox). 
This can be installed using pip: `pip install bvhtoolbox`.