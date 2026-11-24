import numpy as np
import scipy as sp
from matplotlib import pyplot as plt


#20-8


#Prob 1
print('Problem 1')
A1 = np.array([[5,2,4],[-2,0,2],[2,4,7]])
print(sp.linalg.eig(A1))
#To prove that it is correct, use eigenvalue decomposition
val1,vec1=sp.linalg.eig(A1)
val1b = np.eye(3)
for i in range(3):
    val1b[i,i] = val1[i]
val1 = val1b
print(vec1@val1@sp.linalg.inv(vec1))


#Prob 2
print('Problem 2')
A2 = np.array([[5,1e-2,1e-2],[1e-2,8,1e-2],[1e-2,1e-2,9]])
print(sp.linalg.eig(A2))

#Prob 3
print('Problem 3')
A3 = np.array([[0,0.4,-0.1],[-0.4,0,0.3],[0.1,-0.3,0]])
print(sp.linalg.eig(A3))

#Prob 4
print('Problem 4')
A4 = np.array([[1,0,1],[0,4,3],[1,3,12]])
print(sp.linalg.eig(A4))

#Prob 6
print('Problem 6')
A6 = np.array([[10,0.1,-0.2],[0.1,6,0],[-0.2,0,3]])
print(sp.linalg.eig(A6))

#Prob 3
print('Problem 3')
a3 = np.array([[2,-1,1],[-1,3,2],[1,2,3]])
print(sp.linalg.eig(a3))

#Prob 4
print('Problem 4')
a4 = np.array([[3.6,-1.8,1.8],[-1.8,2.8,-2.6],[1.8,-2.6,2.8]])
print(sp.linalg.eig(a4))

#Prob 5
print('Problem 5')
a5 = np.array([[4,2,3],[2,7,6],[3,6,4]])
print(sp.linalg.eig(a5))

#Prob 6
print('Problem 6')
a6 = np.array([[5,1,0,0],[1,3,1,0],[0,1,3,1],[0,0,1,5]])
print(sp.linalg.eig(a6))

#Prob 7
print('Problem 7')
a7 = np.array([[2,4,0,1],[4,1,2,8],[0,2,5,2],[1,8,2,0]])
print(sp.linalg.eig(a7))