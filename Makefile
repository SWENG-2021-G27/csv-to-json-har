dependencies: python3 pip tqdm requests py7zr colorama Tkinter bvhtoolbox
	echo "All dependencies installed successfully"

python3:
	python3 --version

pip:
	python3 -m pip install pip


sys:
	pip install sys

ntpath:
	pip install ntpath

tqdm:
	pip install tqdm

requests:
	pip install requests
	

py7zr:
	pip install py7zr

colorama:
	pip install colorama

Tkinter:
	pip install tk


exe: pyinstaller dependencies
	pyinstaller --onefile src/main.py


pyinstaller:
	pip install pyinstaller

bvhtoolbox:
	pip install bvhtoolbox
