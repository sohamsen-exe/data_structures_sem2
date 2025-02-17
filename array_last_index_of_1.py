import numpy as np
x = np.array([0,1,1,0,1,0,1,0,0])
def last_index(x):
    index = -1
    n = len(x)
    for i in range(n):
        if x[i] == 1:
            index = i
    return index
print("Last index of one :", last_index(x))