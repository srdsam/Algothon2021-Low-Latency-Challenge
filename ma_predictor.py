import numpy as np
from sys import stdin

def moving_average(series, n):
    return np.average(series[-n:])

def ma_predictor(series):
    val = moving_average(series, 3)
    if val > series[-1]:
        return 1
    else:
        return 0

# classify terminal input
for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    val=ma_predictor(d)
    print(val)