# Berkeley Multimodal Human Action Database

### Repository Contents
This folder has the following structure:
````
BerkeleyMHAD
|- config.json
|- download_mhad.py
|- unzip_mhad.py
|- bvh_to_csv.py
````
`config.json` is a configuration file that can be used to convert the Berkeley Multimodal Human Action Database into a 
series of appropriate JSON files for animation using the conversion application.

`download_mhad.py` is a python script that will download the Berkeley Multimodal Human Action Database as a `.zip` file 
into a new folder in the `./RawDatasets` folder called `BerkeleyMHAD`.

`unzip_mhad.py` is a python script that will unzip the Berkeley Multimodal Human Action Database in the 
`./RawDatasets/BerkeleyMHAD` folder. The files in this dataset are in `.bvh` format.

`bvh_to_csv.py` is a python script that will convert all of the `.bvh` files in the `./RawDatasets/BerkeleyMHAD` folder 
to `.csv` files that are ready for conversion. This script uses the [bvh-toolbox](https://github.com/OlafHaag/bvh-toolbox). 
This can be installed using pip: `pip install bvhtoolbox`.