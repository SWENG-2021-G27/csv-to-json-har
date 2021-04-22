import unittest
import os
import json

from colors import *


def plural(i): 
  if(i > 1):
    return 's'
  else:
    return ''


def test():
  total_differences = 0
  number_of_files_compared = 0
  if(not os.path.isdir('TestOutput')):
    print(red("\tNo TestOutput folder in " + os.getcwd()))
    return
  for output in os.listdir('TestOutput'):
    differences = 0
    if os.path.isfile(os.path.join('TestOutput',output)):
      with open(os.path.join('TestOutput',output))as test_file:
        verified_path = os.path.join('Verified',output)
        if(not os.path.isfile(verified_path)):
          break
        with open(os.path.join('Verified',output)) as verified_file:
          print(dim("\tcomparing " + output))
          number_of_files_compared += 1
          try:
            test = json.load(test_file)
            verified = json.load(verified_file)
            for key in test.keys():
              if not key in verified:
                differences += 1
                print("\t\t" + red("For " + output + " verified[" + key + "] does not exist"))
              elif not test[key] == verified[key]:
                differences += 1
                print("\t\t" + red("For " + output + " test[" + key + "] is not the same as verified[" + key + "]"))
            if(differences != 0):
              print('\t\t' + str(differences) + " difference" + plural(differences) + " between TestOutput/" + output + " and Verified/" + output)
              total_differences += differences
          except Exception as e:
            print("Exception raised while comparing " + output + ": " + str(e))
            total_differences += 1


  if(total_differences == 0):
    print(green("\tPerfect, no differences between TestOutput and Verified."))
  else:
    print("\t" + red(str(total_differences) + " difference") + plural(total_differences) + " found in total.")
