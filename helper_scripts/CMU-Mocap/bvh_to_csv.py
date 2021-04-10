import os

for subdir, dirs, files in os.walk("./TestData/CMU"):
    for file in os.listdir(subdir):
        if file.endswith(".bvh"):
            os.system("bvh2csv " + subdir + "\\" + file + " --position --out ../../RawDatasets/CMU")
