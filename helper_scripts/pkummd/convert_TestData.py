import os

sep = os.path.sep

config_file = os.path.abspath('config.json')
input_folder = os.path.abspath('TestData')
output_folder = os.path.abspath('TestOutput')

os.chdir('..' + sep + '..')
os.chdir('src')

exit_code = os.system('python main.py -c ' + config_file + ' -i ' + input_folder + ' -o ' + output_folder)


print('Finished convert_TestData.py with exit code: ' + str(exit_code))
