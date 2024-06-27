# The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric dataimport numpy
import numpy as np

# A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
# create array,conversion from python structure
my_arr = np.array([1,2,3,4,5], np.int64)
print(my_arr)
print(my_arr[3])

# to show size of an array
print(my_arr.shape)
# show type of data type
print(my_arr.dtype)

# it change the value in array
my_arr[0] = 45
print(my_arr)

listarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(listarray.size)
print(listarray)

tupelarray = np.array({1,2,3,4})
print(tupelarray.dtype)
