import numpy as np
import pandas as pd
import sys

def moving_average(series, n):
    return np.average(series[-n:])

def ma_predictor(series):
    val = moving_average(series, 3)
    if val > series[-1]:
        return 1
    else:
        return 0


csv = pd.read_csv('data_ngrams.csv')['LogReturns']

for index, row in csv.iterrows():
    data = np.asarray(list(row), dtype=np.float64)
    val = ma_predictor(data)
    print(val)