import numpy as np
from sys import getsizeof as size
A = np.array([[1,2],[4,5]])
B = np.array([[6,7],[8,9]] , np.int8)
print(A)
print(B)
print(A.ndim)
print(B.ndim)
print("shape A=",A.shape)
print("shape B=",B.shape)
print("size A",size(A)) #default size=int32
print("size B", size(B))
#elementwise arthimetic operations
add  = np.add(A,B)
print("addition\n",add)
sub = np.subtract(A,B)
print("sub\n",sub)
mul = np.multiply(A,B)
print("mul\n",mul)
div  = np.divide(A,B)
print("div\n",div)
#identity matrix
I = np.identity(4)
print("identity matrix\n",I)
#null matrix
N = np.zeros((3,4))
print("null\n",N)
# matrix with ones
O = np.ones((3,2))
print("all ones\n",O)
#matrix multiplication
C  = np.matmul(A,B)
print("matrix mul\n",C)
#dot product
D = np.dot(A,B)
print("dot\n",D)
#inverse of matrix
E = np.linalg.inv(A)
print("inverse\n",E)
#determinant of matrix
F = np.linalg.det(A)
print("det\n", F)
#transpose of matrix
G = np.transpose(A)
print("transpose\n", G)