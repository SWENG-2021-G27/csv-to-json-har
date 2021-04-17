import os
import colorama

colorama.init()

input_folder = os.path.abspath('TestData')
output_folder = os.path.abspath('TestOutput')

os.chdir(os.path.join('..','..'))
os.chdir('src')

exit_code = os.system('python main.py -i ' + input_folder + ' -o ' + output_folder)

if(exit_code ==  0):
  print( colorama.Fore.GREEN )
else:
  print( colorama.Fore.RED )

print('\n\tFinished conversion with exit code: ' + str(exit_code))

print( colorama.Style.RESET_ALL )
