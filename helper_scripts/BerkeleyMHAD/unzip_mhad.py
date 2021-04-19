import os
import sys
import zipfile

sep = os.path.sep

target_folder = os.path.abspath(
    '..' + sep + '..' + sep + 'RawDatasets' + sep + 'BerkeleyMHAD')
target = target_folder + sep + 'BerkeleyMHAD.7z'

if(not os.path.isfile(os.path.abspath(target))):
    print('ERROR: while attempting to extract BerkeleyMHAD zip file. File does not exist at:\n' +
          target + '\n Have you ran the download script yet?')
    sys.exit(-1)

if(not os.path.isdir(target_folder)):
    os.mkdir(target_folder)

print('Extracting ' + target + '\nThis may take a while...')
with zipfile.ZipFile(target, 'r') as zip_ref:
    filenames = zip_ref.namelist()
    for filename in filenames:
        if(filename.endswith('.bvh')):
            zip_ref.extract(filename, target_folder)
print('Finished')