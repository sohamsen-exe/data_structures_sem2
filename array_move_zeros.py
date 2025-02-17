import numpy as np
x = np.array([0, 1, 1, 0, 1, 0, 1, 0, 0])
def move_zeros(arr):
    ones = arr[arr == 1]
    zeros = arr[arr == 0]
    return np.concatenate((ones, zeros))
x_sorted = move_zeros(x)
print("Array after moving zeros :", x_sorted)