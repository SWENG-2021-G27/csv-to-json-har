import os

for subdir, dirs, files in os.walk("./SFU-Data-BVH"):
    for file in os.listdir(subdir):
        if file.endswith(".bvh"):
            os.system("bvh2csv " + subdir + "\\" + file + " --position --out ./SFU-Data-CSV")
