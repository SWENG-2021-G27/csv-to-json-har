import pandas as pd
import scipy.io
import os
import sys

sep = os.path.sep

file_to_convert =  "TestData" + sep + "S1_1_1.mat"

def mat2csv(file_mat, file_csv, index=False):
    mat = loadmat(file_mat)

    data = {}
    for col_id in range(len(mat['X'][0])):
        data[col_id] = []

    for row in mat['X']:
        for col_id, value in enumerate(row):
            data[col_id].append(value)

    data['class'] = []
    for row in mat['y']:
        for value in row:
            data['class'].append(value)

    df = pd.DataFrame(data)
    df.to_csv(file_csv, index=index)



mat =  scipy.io.loadmat(file_to_convert)

print(mat.keys())

print("Finished")
