import colorama
colorama.init()

def warn(warning):
    # warning in yellow
    print("\n\t" + colorama.Fore.YELLOW + "[WARNING]: " + colorama.Style.RESET_ALL + warning + "\n")


def error(error_msg):
    # error in red
    print("\n\t" + colorama.Fore.RED + "[ERROR]: " + colorama.Style.RESET_ALL + error_msg + "\n")
    sys.exit(-1)


def nice_msg(msg):
    print("\n\t" + colorama.Fore.GREEN + msg + colorama.Style.RESET_ALL + "\n")


def blue(msg):
    return colorama.Fore.BLUE + msg + colorama.Style.RESET_ALL


