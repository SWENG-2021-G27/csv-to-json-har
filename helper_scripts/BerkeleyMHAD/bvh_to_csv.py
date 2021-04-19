import os

print("This will take a while")
for subdir, dirs, files in os.walk("../../RawDatasets/BerkeleyMHAD/Mocap"):
    for file in os.listdir(subdir):
        if file.endswith(".bvh"):
            print(file)
            os.system("bvh2csv " + subdir + "\\" + file + " --position --out ../../RawDatasets/BerkeleyMHAD-CSV")
