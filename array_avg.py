import numpy as np
x = np.array([10, 20, 30, 40, 50])
def avg(x):
    avg = np.sum(x)/np.len(x)
    return avg
print(avg(x))