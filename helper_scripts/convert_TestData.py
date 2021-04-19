import os
import colorama

colorama.init()

def convert():
  sep = os.path.sep

  config_file = os.path.abspath(os.path.join('TestData','config.json'))
  input_folder = os.path.abspath('TestData')
  output_folder = os.path.abspath('TestOutput')

  exit_code = os.system('python ' + os.path.join(os.pardir,os.pardir,'src','main.py') + ' -c ' + config_file + ' -i ' + input_folder + ' -o ' + output_folder)

  if(exit_code ==  0):
    print( colorama.Fore.GREEN )
  else:
    print( colorama.Fore.RED )

  print('\tFinished convert_TestData.py with exit code: ' + str(exit_code))

  print( colorama.Style.RESET_ALL )
