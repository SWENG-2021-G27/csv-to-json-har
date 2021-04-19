import unit_test
import os
from colors import *


if __name__ == "__main__":
 for dir in os.listdir('.'):
  if(os.path.isdir(dir) and dir != "__pycache__"):
    print(blue(dir))
    os.chdir(dir)
    unit_test.test()
    os.chdir('..')
