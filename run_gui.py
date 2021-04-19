import os
import sys
from pathlib import Path

path = Path(sys.argv[0])

os.chdir(os.path.join(path.parent, 'dist'))
os.system(os.path.join('.', 'mocap_to_json') + ' --gui')
