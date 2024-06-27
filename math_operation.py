import numpy as np
import sys

a1 = np.array([[2,1,5],[4,3,1],[5,1,2]])
a2 = np.array([[0,2,3],[2,5,3],[4,2,1]])

print("a1 : ",a1)
print("a1 : ",a2)
print("sum is :\n",a1+a2)
print("multiplication is :\n",a1*a2)

# for find square root
print("Square root : \n",np.sqrt(a1))

# sum() for sum of all element
print("\nsum of all element : ",np.sum(a1))
print("max value from a2 : ",np.max(a1))
print("min value from a2 : ",np.min(a1))

# where() method return index of given value 
print(np.where(a1>4))

# count_nonzeros() method return total no of non zero elements
print(np.count_nonzero(a2)) 
print(np.nonzero(a2)) 

py_ar = [0,4,55,2]
np_ar = np.array(py_ar)
print("size pf py_ar : ",sys.getsizeof(1)*len(py_ar))
print("size pf np_ar : ", np_ar.itemsize * np_ar.size)

print("List of numpy array : ",np_ar.tolist())