

import io

configuration = {
  "NumberOfJoints": -1,
  "NumberOfSkeletons": 1,
  "Dimensionality": 3
}


def load_config(path_to_config, encoding="utf-8"):
  print("Loading configuration from: " + path_to_config)
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
      print( key + " is a valid configuration variable")
      configuration[key] = line[len(key):len(line)-1]
      print( "configuration[" + key + "] has been updated to " + configuration[key])
      
    print(line[:len(line)-1] + " \u2713",)
    line = f.readline()
  f.close()


load_config("config")
  
