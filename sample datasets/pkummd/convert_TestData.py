import os

os.chdir('../..')
os.chdir('src')
sep = os.path.sep

config_file = '..' + sep + 'pkummd' + sep + 'config.json'
input_file = '..' + sep + 'pkummd' + sep + 'TestData' + sep + '0002-L.txt'
output_file = '..' + sep + 'pkummd' + sep + 'TestData' + sep + '0002-L.json'
exit_code = os.system('python main.py ' + config_file + ' ' + input_file + ' ' + output_file)