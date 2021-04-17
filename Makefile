dependencies: python pip tqdm requests py7zr colorama Tkinter bvhtoolbox
	echo "All dependencies installed successfully"

python:
	python --version

pip:
	python -m pip install pip

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

pyinstaller:
	pip install pyinstaller

exe: pyinstaller
	pyinstaller --onefile src/main.py

bvhtoolbox:
	pip install bvhtoolbox
