# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float


import numpy

def arrays(arr):
    arr = arr[::-1]
    return numpy.array(arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)