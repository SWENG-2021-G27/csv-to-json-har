
import colorama
colorama.init()

def b(m):
  return colorama.Fore.BLUE + m + colorama.Style.RESET_ALL
def r(m):
  return colorama.Fore.RED + m + colorama.Style.RESET_ALL
def g(m):
  return colorama.Fore.GREEN + m + colorama.Style.RESET_ALL
def y(m):
  return colorama.Fore.YELLOW + m + colorama.Style.RESET_ALL
def w(m):
  return colorama.Fore.WHITE + m + colorama.Style.RESET_ALL

def print_help():

  print(
  "\t" + b('-h') + " or " + b('--help') + " to print this help text.\n\n" +

  "\t" + b("-i") + " or " + b("--input") + " takes one argument which should be a relative or absolute path to the input file or directory. If the argument is a directory then the program will recursively convert all files in the directory which match the " + b('"FileExtension"') + " specified in the " + b("config.json") + "\n\n" +
  
  "\t" + b("-c") + " or " + b("--config") + " takes one argument which should be a relative or absolute path to a config file in JSON format. The specifics of the JSON format are given in the top level ./README.md.\n\n" +

  "\t" + b("-o") + " or " + b("--output") + " takes one argument which should be a relative or absolute path to a " + y('FOLDER') + ". Even if the input is a single file the output should be a folder. If the input is a folder then the structure of the input folder will be replicated in the output folder.\n\n" +

  "\t" + b("-g") + " or " + b("--gui") + " will start the GUI and all other command line arguments will be ignored.\n\n"

  )
