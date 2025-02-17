import numpy as py
x = np.array([10, 20, 30, 40, 50])
s_ele = int(input())
def i_ele(x, s_ele):
    try:
        n = len(x)
        for i in range(n):
            if x[i] == s_ele:
                return i
        raise ValueError("Element not found")
    except ValueError:
        return -1
print(i_ele(x, s_ele))