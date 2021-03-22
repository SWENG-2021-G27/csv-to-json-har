import py7zr
import os

with py7zr.SevenZipFile(os.path.abspath('gitignore' + os.path.sep + 'Skeleton.7z'), 'r') as archive:
  archive.extractall(path=os.path.abspath('gitignore'))
