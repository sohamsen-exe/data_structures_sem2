import numpy as np
x = np.array([10, 20, 30])
def min_max(x):
    min_e = np.min(x)
    max_e = np.max(x)
    return min_e, max_e
print(min_max(x))