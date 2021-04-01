# csv-to-json-har

### Prerequisites
To run this project, you need to following installed on your machine:
- Python 3
- Tkinter

### Running the Project
Open the terminal and navigate to the src folder. You can then run the project with the following command:

```
python main.py
```

Running the project with the command above will assume the following defaults:
- All files to be converted are in the ```RawDatasets``` directory.
- The configuration file is located in the RawDatasets directory and is named ```config.json```.
- The output directory is ```RawDatasets/Output```.

The following optional flags can also be used:
- ```-gui``` will open the GUI
  - ```python main.py -gui```  
- ```-input <path of input directory>``` will specify the input directory to be used, and update the assumption 
for the configuration file and output directory accordingly.
  - ```python main.py -input "C:\Users\username\InputDirectory"```
- ```-config <path of configuration file>``` will specify the configuration file to be used. 
  - ```python main.py -config "C:\Users\username\InputDirectory\config.json"```
- ```-output <path of output directory>``` will specify the output directory to be used.
  - ```python main.py -output "C:\Users\username\OutputDirectory"```
  
These optional flags can be used together:  
```python main.py -input "C:\Users\username\InputDirectory" -config "C:\Users\username\InputDirectory\config.json" -output "C:\Users\username\OutputDirectory"```

Note: if the ```-gui``` flag is present, the GUI will open and no conversion will happen immediately. The conversion 
will take place once submitted through the GUI.