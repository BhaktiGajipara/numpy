# intrinsic python array creation object
import numpy as np
zeros = np.zeros((2,4))
print("zero array:\n",zeros)
print(zeros.dtype)
print(zeros.shape)

# arange    /like range in python
x = np.arange(10)
print("Arrange array:\n",x)
print(x.shape)

# linspace return equal space number between given number
lspace = np.linspace(0,10,5)
print("lspace :\n",lspace)

# it return given size empty array and array has garbeg/random element  
empty_array = np.empty((2,3))
print("empty array:\n",empty_array)

# empty_like
emp_like = np.empty_like(lspace)
print("empty like:\n",emp_like)

# identity ,it return nxn identity matrix
ide = np.identity(5)
print("identity matrix:\n",ide)

# reshape, it reshape the structure of array
arr = np.arange(1,100)
print("\n",arr)
print("reshapeed array:\n",arr.reshape(3,33))

# reshape will not change the actuall arr you need to update it
print("\n",arr)
arr = arr.reshape(3,33)
print("updated array:\n",arr)

# to make array one dimensional from two dimensional use ravel
print("ravel:\n",arr.ravel())