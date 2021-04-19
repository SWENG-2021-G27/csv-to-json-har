import py7zr
import os

sep = os.path.sep
location = os.path.abspath('..' + sep + '..' + sep + 'RawDatasets' + sep + 'NTU')
with py7zr.SevenZipFile(os.path.abspath(location + sep + 'Skeleton.7z'), 'r') as archive:
  archive.extractall(path=os.path.abspath(location))
