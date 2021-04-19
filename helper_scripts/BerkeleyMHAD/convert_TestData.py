import os
import colorama

colorama.init()

sep = os.path.sep

config_file = os.path.abspath(os.path.join('TestData', 'config.json'))
input_folder = os.path.abspath('TestData')
output_folder = os.path.abspath('Verified')

os.chdir('..' + sep + '..')
os.chdir('src')

exit_code = os.system('python main.py -c \"' + config_file + '\" -i \"' + input_folder + '\" -o \"' + output_folder + "\"")

if(exit_code ==  0):
  print( colorama.Fore.GREEN )
else:
  print( colorama.Fore.RED )

print('\tFinished convert_TestData.py with exit code: ' + str(exit_code))

print( colorama.Style.RESET_ALL )
