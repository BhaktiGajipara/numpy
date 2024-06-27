# 1 dimensinal array have one axis(axis-0)
# 2 dimensional array have 2 axis (axis-0, axis-1)
'''
    -------> axis 1
|   0  1  1
|   2  2  3
v   3  3  4

axis 0
'''
# if we sum axis 0 then result is (5 6 8)
# and sum axis 1 is (2 7 10)

import numpy as np

arr = np.array([[0,1,1],[2,2,3],[3,3,4]])
print("Array:\n",arr)
print("axis 0 sum",arr.sum(axis=0))
print("axis 1 sum",arr.sum(axis=1))