#PRECTICAL 3
'''
Implement a Program for two matrix multiplication
using simple nested loop and numpy module.
'''


#approch1
import numpy as np
array1=np.array([[0,0,0],[4,5,6],[7,8,9]])
array2=np.array([[2,3,3],[6,5,4],[3,2,1]])

result=np.dot(array1,array2)
print(result)

#approch2
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=[[12,23,34],
   [34,45,56],
   [45,56,67]]

r=[[0,0,0,],
   [0,0,0],
   [0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            r[i][j]=a[i][k]*b[k][j]
            
            
for i in r:
   print(i)
