# csv-to-json-har

### Prerequisites
To follow this installation guide you should have the following:
- A terminal emulator and command line shell (e.g. PowerShell, Bash)
- Python 3
- GNU Make
- A connection to the internet

Other dependencies are listed in the Makefile but you don't need to know about them to use the software.

### Installation

After you have installed **Python 3**
clone the git repository:
```bash
git clone https://github.com/SWENG-2021-G27/csv-to-json-har.git
```

Move into the directory.
```bash
cd csv-to-json-har
```
#### Python script only

Install the dependencies with:
```bash
make
```
and run the script with
```bash
python src/main.py
```
or from anywhere else:
```bash
python <path to main.py>
```

#### Executable version
Optionally build a compiled version of the program with:
```bash
make exe
```

After `make exe` has been run once successfully you can use `make exe-quick` to recompile the exectuable more quickly. The executable `mocap_to_json` can be found in the `dist` folder. Add that folder to your path or link a file in your path to the executable if you'd like to be able to call the program from anywhere with just:
```bash
mocap_to_json
```

You can change the name of the executable to whatever you'd like.

### Running the Project

#### Running the GUI
Pass the --gui option to open the GUI
```bash
python src/main.py --gui
```
or run the script `run_gui.py`:
```bash
python run_gui.py
```

#### Without any command line options
The easiest way to run the program is to navigate to a folder of datasets you want to convert, make  sure
there is a valid config.json in the top level of that folder and simply call:
```bash
python <path to main.py>
```
or
```bash
<path to mocap_to_json>
```

or if you've built the executable and added it to your path call:

```bash
mocap_to_json
```

With no options the program will
- use the user's current working directory as the input folder,
- assume there is a valid `config.json` in the current working directory (see below for specifications), and
- create a folder for the output
called `ConvertedJsonOutput` in the input folder.

#### Command Line Options
The following optional flags can also be used:
- `--gui` will open the GUI. If the `--gui` flag is present all other arguments will be ignored.
  - `python main.py --gui`  
- `--input <path of input file or directory>` will specify the input file or directory to be used. If the `--input` is a directory the default config file will be set to `<input dir>/config.json` and the default output directory will be set to `<input dir>/ConvertedJsonOutput/`.
  - `python main.py --input "C:\Users\username\InputDirectory"`
- `--config <path of configuration file>` will specify the configuration file to be used. 
  - `python main.py --config "C:\Users\username\InputDirectory\config.json"`
- `--output <path of output directory>` will specify the output directory to be used.
  - `python main.py --output "C:\Users\username\OutputDirectory"`
  
These optional flags can be used together:  
```python
python main.py --input "C:\Users\username\InputDirectory" --config "C:\Users\username\InputDirectory\config.json" --output "C:\Users\username\OutputDirectory"
```


## Config specification

The program attempts to convert files in the input folder according to
the configuration specified in `config.json`.

As of writing this only a limited number of `config.json` files have
been written and tested. Some of the variables which can be set in 
the `config.json` are experimental or have not been implemented yet.

The bleeding list of variables that can be given in the `config.json` can be seen in `src/configuration.py`.
