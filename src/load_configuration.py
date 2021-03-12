

import io

configuration = {
  "NumberOfJoints": -1,
  "NumberOfSkeletons": 1,
  "Dimensionality": 3
}


# ANSI color codes can be seen here: https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007

def load_config(path_to_config, encoding="utf-8",silent=False):
  if(not silent):
    print("\033[0;37;40mLoading configuration from: " + path_to_config)
  f = open(path_to_config, "r", encoding=encoding)
  
  line = f.readline()
  while line :
    key = ''
    char = line[0]
    i = 0
    while( char != " " and char != "\n"):
      key += char
      i += 1
      char = line[i]

    if(configuration.get(key)):
      configuration[key] = line[len(key):len(line)-1]
      if(not silent):
        print( "\033[0;32mconfiguration['" + key + "'] has been updated to " + type(configuration[key]).__name__ + ": '" +  configuration[key] + "' \u2713")
    else :
      if(not silent):
        print("\033[1;31;44mERROR " + key + " is not a recognised configuration variable\033[0;37;40m")      
    line = f.readline()

  f.close()


load_config("config")
load_config("config",silent=True)
