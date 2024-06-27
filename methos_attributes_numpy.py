import numpy as np

arr = np.array([[0,1,1],[2,2,3],[3,3,4]])
print(arr)

# T attribute to conver array into transpose
print("Transpose:\n",arr.T)

# flat attribute  //it gives iterator
print("iterator:")
for item in arr.flat:
    print(item)

# ndim attribute //return number of dimensions
print("no.of dimensions : ",arr.ndim)
print("no.of elements/size : ",arr.size)
print("bytes : ",arr.nbytes)

# argmax() //method return maximum value from array
# and argmin() //method return minimum value
a1 = np.array([1,22,453,23,8])
print("maximum value element index : ",a1.argmax())
print("minimum value element index : ",a1.argmin())

# argsort() method return sorted array
print(a1.argsort())

# in two dimensional array first it convert it in one dimensional and then return value
print("arr :\n",arr)
print("Max value in 2D : ",arr.argmax()) 
print("Min value in 2D : ",arr.argmin()) 

print("max at axis 0 : ",arr.argmax(axis=0))
print("max at axis 1 : ",arr.argmin(axis=0))

print(arr.argsort(axis=0))