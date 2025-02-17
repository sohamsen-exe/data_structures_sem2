import numpy as np
x = np.array([1,2,3,4,5])
def prod_exceptsel(x):
    n = len(x)
    res = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= x[j]
    return res
print("Original Array :", x)
print("Product Array :", prod_exceptsel(x))