import unittest
import os
import json


def plural(i): 
  if(i > 1):
    return 's'
  else:
    return ''


def test():
  total_differences = 0
  number_of_files_compared = 0
  for output in os.listdir('TestOutput'):
    differences = 0
    if os.path.isfile(os.path.join('Verified',output)): 
    with open(os.path.join('TestOutput',output))as test_file:
      verified_path = os.path.join('Verified',output) 
      if(not os.path.isfile(verified_path)):
        break
      with open(os.path.join('Verified',output)) as verified_file:
        print("comparing TestOutput/" + output + " and Verified/" + output)
        number_of_files_compared += 1
        test = json.load(test_file)
        verified = json.load(verified_file)
        for key in test.keys():
        if not test[key] == verified[key]:
          differences += 1
          print("\tFor " + output + " test[" + key + "] is not the same as verified[" + key + "]")
    if(differences == 0):
      pass
    else:
      print('\t' + str(differences) + " difference" + plural(differences) + " between TestOutput/" + output + " and Verified/" + output)
    total_differences += differences


  if(total_differences == 0):
    print("Perfect, no differences between TestOutput and Verified.")
  else:
    print(str(total_differences) + " difference" + plural(total_differences) + " found in total.")
