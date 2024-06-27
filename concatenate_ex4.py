# Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print (numpy.concatenate((array_1, array_2, array_3)))   

# If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print (numpy.concatenate((array_1, array_2), axis = 1))

# You are given two integer arrays of size nXp and mXp ( n & m  are rows, and p is the column). Your task is to concatenate the arrays along axis .
n, m, p = map(int, input().split())
print(numpy.array([list(map(int, input().split())) for _ in range(n + m)], ndmin=p))
