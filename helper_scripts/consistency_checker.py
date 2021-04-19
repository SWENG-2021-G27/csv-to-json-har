import unit_test
import os
import convert_TestData
from colors import *


if __name__ == "__main__":
 for dir in os.listdir('.'):
  if(os.path.isdir(dir) and dir != "__pycache__"):
    print(blue('#################'))
    print(blue(dir))
    print(blue('#################'))
    os.chdir(dir)
    convert_TestData.convert() 
    unit_test.test()
    os.chdir('..')
