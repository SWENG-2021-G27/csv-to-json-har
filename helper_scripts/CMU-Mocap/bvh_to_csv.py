import os

for subdir, dirs, files in os.walk("./CMU-Data"):
    for file in os.listdir(subdir):
        if file.endswith(".bvh"):
            os.system("bvh2csv " + subdir + "\\" + file + " --position --out ./CMU-Data-CSV")
