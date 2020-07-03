#multidimensional arrays
import numpy as np
from sys import getsizeof as size
A = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
B = np.array([1,2,3,4], np.int8)
print(A.ndim)
print(A)
print(type(A))
print("A shape",A.shape)
print("B shape",B.shape)
print(A.dtype)
print(B.dtype)
print("size A",size(A))
print("size B", size(B))
# accessing elements in array
print("accessing:",A[1,2])
print("accessing:",A[3,0])
# slicing
print("slicing\n",A[:,:])
print("slicing row\n",A[:2,:])
print("slicing col\n",A[:,0:1])
print("slicing particular ele\n",A[0:1,1:2])