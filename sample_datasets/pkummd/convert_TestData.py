import os

sep = os.path.sep

config_file = os.path.abspath('config.json')
input_file = os.path.abspath('TestData' + sep + '0002-L.txt')
output_file = os.path.abspath('TestOutput' + sep + '0002-L.txt')

os.chdir('..' + sep + '..')
os.chdir('src')

exit_code = os.system('python main.py ' + config_file + ' ' + input_file + ' ' + output_file)

print('finished with exit code: ' + str(exit_code))
