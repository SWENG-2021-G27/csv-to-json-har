import os

input_folder = os.path.abspath('TestOutput')

if(not os.path.isdir('pngs')):
  os.mkdir('pngs')

output_folder = os.path.abspath('pngs')

os.chdir('..')
os.chdir('..')
os.chdir('RobotAnimationCreator')

prog_name = os.path.abspath('ConvertJsonToImages.exe')

command = ''
if (os.name == 'posix'):
  print('Using wine to run ' + os.path.abspath('ConvertJsonToImages.exe'))
  print('If you do not have wine installed and configured correctly, this will fail')
  command = command + 'wine '
else:
  print("I'm assuming you're on windows...")

command = command + prog_name + ' -i ' + input_folder + ' -o ' + output_folder + ' -d 0'

exit_code = os.system(command)
print('Finished with exit_code: ' + str(exit_code))

