import os

print("This will take a while")
for subdir, dirs, files in os.walk("./SFU-Data-BVH"):
    for file in os.listdir(subdir):
        if file.endswith(".bvh"):
            print(file)
            os.system("bvh2csv " + subdir + "\\" + file + " --position --out ../../RawDatasets/SFU-Data-CSV")
