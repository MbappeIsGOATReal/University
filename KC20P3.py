import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#20-1

#Prob 7
print('Problem 7')
a7 = np.array([[-3,6,-9],[1,-4,3],[2,5,-7]])
b7 = np.array([[-46.725],[19.571],[-20.073]])
print(sp.linalg.solve(a7,b7))

#Prob 8
print('Problem 8')
a8 = np.array([[5,3,-1],[0,-4,8],[10,-6,26]])
b8 = np.array([[2],[-3],[0]])
print(sp.linalg.solve(a8,b8))

#Prob 9
print('Problem 9')
a9 = np.array([[0,6,13],[6,0,-8],[13,-8,0]])
b9 = np.array([[137.86],[-85.88],[178.54]])
print(sp.linalg.solve(a9,b9))

#Prob 10
print('Problem 10')
a10 = np.array([[4,4,2],[3,-1,2],[3,-7,1]])
b10 = np.array([[0],[0],[0]])
print(sp.linalg.solve(a10,b10))

#Prob 13
print('Problem 13')
a13 = np.array([[0,3,5],[3,-4,0],[5,0,6]])
b13 = np.array([[1.2073],[-2.34066],[-0.329193]])
print(sp.linalg.solve(a13,b13))

#Prob 14
print('Problem 14')
a14 = np.array([[-47,4,-7],[19,-3,2],[-15,5,0]])
b14 = np.array([[-118],[43],[-25]])
print(sp.linalg.solve(a14,b14))

#Prob 15
print('Problem 15')
a15 = np.array([[0,2.2,1.5,-3.3],[0.2,1.8,0,4.2],[-1,3.1,2.5,0],[0.5,0,-3.8,1.5]])
b15 = np.array([[-9.3],[9.24],[-8.7],[11.94]])
print(sp.linalg.solve(a15,b15))

#Prob 16
print('Problem 16')
a16 = np.array([[3.2,1.6,0,0],[1.6,-0.8,2.4,0],[0,2.4,-4.8,3.6],[0,0,3.6,2.4]])
b16 = np.array([[-0.8],[16],[-39],[10.2]])
print(sp.linalg.solve(a16,b16))

#20-3
#Old Methods not in SciPy (Jacobi,SOR,gauss Seidel). Most basic is Conjugate Gradient but not for general

#Prob 4
print('Problem 4')
a4 = np.array([[4,-1,0],[-1,4,-1],[0,-1,4]])
b4 = np.array([[21],[-45],[33]])
print(sp.sparse.linalg.gmres(a4,b4))

#Prob 5
print('Problem 5')
a5 = np.array([[10,1,1],[1,10,1],[1,1,10]])
b5 = np.array([[6],[6],[6]])
print(sp.sparse.linalg.gmres(a5,b5))

#Prob 6
print('Problem 6')
a6 = np.array([[0,1,7],[5,1,0],[1,6,1]])
b6 = np.array([[25.5],[0],[-10.5]])
print(sp.sparse.linalg.gmres(a6,b6))

#Prob 7
print('Problem 7')
a7 = np.array([[5,-2,0],[-2,10,-2],[0,-2,15]])
b7 = np.array([[18],[-60],[128]])
print(sp.sparse.linalg.gmres(a7,b7))

#Prob 8
print('Problem 8')
a8 = np.array([[5,1,2],[1,4,-2],[2,3,8]])
b8 = np.array([[19],[-2],[39]])
print(sp.sparse.linalg.gmres(a8,b8))

#Prob 9
print('Problem 9')
a9 = np.array([[4,0,5],[1,6,2],[8,2,1]])
b9 = np.array([[12.5],[18.5],[-11.5]])
print(sp.sparse.linalg.gmres(a9,b9))

#Prob 10
print('Problem 10')
a10 = np.array([[3,2,1],[1,3,2],[2,1,3]])
b10 = np.array([[7],[4],[7]])
print(sp.sparse.linalg.gmres(a10,b10))
