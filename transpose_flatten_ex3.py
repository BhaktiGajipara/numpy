# You are given a nXm integer array matrix with space separated elements ( n= rows and  m= columns).
# Your task is to print the transpose and flatten results

import numpy as np
arr = np.array([input().split() for _ in range(int(input().split()[0]))], int)

print(arr.transpose()) 
print(arr.flatten())