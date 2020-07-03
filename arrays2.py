import numpy as np
from sys import getsizeof as size
#declare list
A = [1,2,3,4,5,7,8,9]
print(type(A))
#convert to array
B = np.array(A)
print(B)
print(type(B))
#size of each variable
print("A=",size(A))
print("B=",size(B))
#finding size of an empty array and empty list\memory consumed
print("empty list size",size([])) #64+8 (list size)
print("empty array size",size(np.array([]))) #96+8 (size of array)
#optimizing memory my changing int to 16,32,64
B = np.array(A,np.int8)
print("after optimizing B=",size(B))
#comparing operations in lists and arrays
C = B/2
print(C) #array
#D = A/2
#print(D)          #list error
D = list(i/2 for i in A)
print(D)