import colorama

colorama.init()

def red(msg):
  return colorama.Fore.RED + msg + colorama.Style.RESET_ALL

def blue(msg):
  return colorama.Fore.BLUE + msg + colorama.Style.RESET_ALL

def green(msg):
  return colorama.Fore.GREEN + msg + colorama.Style.RESET_ALL

def dim(msg):
  return colorama.Style.DIM + msg + colorama.Style.RESET_ALL


