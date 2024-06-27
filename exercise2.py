# ou are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

import numpy as np

data = list(map(int, input().split()))
data = np.array(data, int)
print(np.reshape(data, (3,3)))