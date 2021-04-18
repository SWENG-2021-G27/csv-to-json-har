import os

for subdir, dirs, files in os.walk("./CMU-Data-BVH"):
    for file in os.listdir(subdir):
        if file.endswith(".bvh"):
            print(file)
            os.system("bvh2csv " + subdir + "\\" + file + " --position --out ../../RawDatasets/CMU-Data-CSV")
