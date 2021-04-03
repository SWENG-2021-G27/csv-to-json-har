import os

sep = os.path.sep

config_file = os.path.abspath('config.json')

file_to_convert = os.path.abspath('TestData' + sep + '01_01_pos.csv')

output_location = os.path.abspath('TestOutput' + sep + 'non_verified_01_01_pos.csv')

os.chdir('..')
os.chdir('..')
os.chdir('src')

exit_code = os.system('python main.py ' + config_file + ' ' + file_to_convert + ' ' + output_location)

if (exit_code == 0):
    print("Finished with exit code: " + str(exit_code))
    print("Created output in: " + output_location)

else:
    print("Finished with exit code: " + str(exit_code))
