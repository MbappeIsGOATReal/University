import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#19-4

#Prob 10
#Cubic
print('Problem 10')
x10 = np.array([-2,-1,0,1,2])
y10 = np.array([0,0,1,0,0])
int10 = sp.interpolate.CubicSpline(x10,y10)

#Prob 11
#Linear and 4th
print('Problem 11')
int11a = sp.interpolate.make_interp_spline(x10,y10,k=1)
x10lin = np.linspace(-2,2,100)
y10lin1 = int11a(x10lin)
y10lin3 = int10(x10lin)
plt.plot (x10lin,y10lin3,'--r',label='Cubic')
plt.plot (x10lin,y10lin1,'g',label='Linear')
plt.grid(True)
plt.axis([-2.5,2.5,-0.5,1.5])
plt.legend()
plt.show()

#Prob 12-16
print('Problem 12')
x12=np.array([0,2,4,6])
y12=np.array([1,9,41,41])
int12 = sp.interpolate.CubicSpline(x12,y12)
xg12 = np.linspace(0,6,100)
yg12 = int12(xg12)
x13=np.array([0,1,2,3])
y13=np.array([1,0,-1,0])
int13 = sp.interpolate.CubicSpline(x13,y13)
xg13 = np.linspace(0,3,100)
yg13 = int13(xg13)
x14=np.array([0,1,2,3])
y14=np.array([2,3,8,12])
int14 = sp.interpolate.CubicSpline(x14,y14)
yg14 = int14(xg13)
x15=np.array([0,2,4,6])
y15=np.array([4,0,4,80])
int15 = sp.interpolate.CubicSpline(x15,y15)
yg15 = int15(xg12)
x16=np.array([0,2,4,6])
y16=np.array([2,-2,2,78])
int16 = sp.interpolate.CubicSpline(x16,y16)
yg16 = int16(xg12)
plt.plot (xg12,yg12,'r',label='Prob 12')
plt.plot (xg13,yg13,'g',label='Prob 13')
plt.plot (xg13,yg14,'b',label='Prob 14')
plt.plot (xg12,yg15,'y',label='Prob 15')
plt.plot (xg12,yg16,'c',label='Prob 16')
plt.grid(True)
plt.legend()
plt.show()