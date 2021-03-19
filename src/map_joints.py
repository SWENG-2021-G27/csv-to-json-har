

def map_n_joints_to_19(mapping, joints):
  new_joints = []
  number_of_joints_mapped = 0
  for map_to in mapping:
    if(number_of_joints_mapped == 19):
      return new_joints

    if(map_to >= 0):
      new_joints.append(joints[map_to])
      number_of_joints_mapped += 1

  if len(new_joints) < 19:
    print('ERROR: the mapping did not provide enough joints\t' + str(len(new_joints)) +'/19')
    return -1
  return new_joints
