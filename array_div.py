import numpy as np
import math
x = np.array([1,2,3,4,5])
def prod_exceptsel_div(x):
    total_prod = math.prod(x)
    prod_arr = []
    for i in x:
        prod_arr.append(total_prod // i)
    return prod_arr
print("Origincal Array :", x)
print("Product Array :", prod_exceptsel_div(x))