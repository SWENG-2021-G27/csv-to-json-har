import os
import sys
from pathlib import Path

path = Path(sys.argv[0])

os.chdir(path.parent)
os.system(os.path.join('.', 'mocap_to_json.exe') + ' --gui')
