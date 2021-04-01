import os

sep = os.path.sep

config_file = os.path.abspath('config.json')
input_file = os.path.abspath('TestData' + sep + '0222-M.txt')
output_file = os.path.abspath('TestOutput' + sep + 'non_verified_0222-M.json')

os.chdir('..' + sep + '..')
os.chdir('src')

exit_code = os.system('python main.py ' + config_file + ' ' + input_file + ' ' + output_file)


print('Finished convert_TestData.py with exit code: ' + str(exit_code))
