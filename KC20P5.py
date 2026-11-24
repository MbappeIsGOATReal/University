import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#20-5

def linear(x,a,b):
    return a*x + b

#Prob 3
print('Problem 3')
x3 = np.array([0,1,2,3,4])
y3 = np.array([1.8,1.6,1.1,1.5,2.3])
print(sp.stats.linregress(x3,y3))
m3,b3,_,_,_ = sp.stats.linregress(x3,y3)
x3lin = np.linspace(0,4,100)
y3lin = linear(x3lin,m3,b3)
def quadratic(x,a,b,c):
    return a*x**2 + b*x + c
(q3, _)=sp.optimize.curve_fit(quadratic,xdata=x3,ydata=y3)
(a3q,b3q,c3q)=q3
y3int = quadratic(x3lin,a3q,b3q,c3q)
plt.scatter(x3,y3,color='blue',marker='*',label='raw')
plt.plot(x3lin,y3lin,'r--',label='least square')
plt.plot(x3lin,y3int,'g--',label='nonlinear (quadratic)')
plt.legend()
plt.title('Problem 3')
plt.show()

#Prob 4
#Hooke Law, F = ks
#F = lb, s = cm
print('Problem 4')
x4 = np.array([1,2,4,6,10,20])
y4 = np.array([0.3,0.7,1.3,1.9,3.2,6.3])
print(sp.stats.linregress(x4,y4))
m4,b4,r4,_,_ = sp.stats.linregress(x4,y4)
x4lin = np.linspace(0,20,100)
y4lin = linear(x4lin,m4,b4)
plt.scatter(x4,y4,color='blue',marker='*',label='raw')
plt.plot(x4lin,y4lin,'r--',label=f'Hooke Law, m={m4}, b={b4}, r2 = {r4**2}')
plt.axis([0,20,0,7.5])
plt.grid('True')
plt.xlabel('s (cm)')
plt.ylabel('F (lb)')
plt.title('Hookes Law')
plt.legend()
plt.show()

#Prob 5
#Roughly Constant Velocity
#S = km, t = hr
print('Problem 5')
x5 = np.array([9,10,11,12])
y5 = np.array([140,220,310,410])
m5,b5,r5,_,_ = sp.stats.linregress(x5,y5)
x5lin = np.linspace(9,12,100)
y5lin = linear(x5lin,m5,b5)
plt.scatter(x5,y5,color='blue',marker='*',label='raw')
plt.plot(x5lin,y5lin,'r--',label=f'Constant Velocity, vave={m5}, b={b5}, r2 = {r5**2}')
plt.axis([9,12,100,450])
plt.grid('True')
plt.xlabel('t, (hr)')
plt.ylabel('k (km)')
plt.title('Constant Velocity')
plt.legend()
plt.show()

#Prob 6
#Ohms Law U = Ri
print('Problem 6')
x6 = np.array([2,4,6,10])
y6 = np.array([104,206,314,530])
m6,b6,r6,_,_ = sp.stats.linregress(x6,y6)
x6lin = np.linspace(2,10,100)
y6lin = linear(x6lin,m6,b6)
plt.scatter(x6,y6,color='blue',marker='*',label='raw')
plt.plot(x6lin,y6lin,'r--',label=f'Ohms Law, R={m6}, b={b6}, r2 = {r6**2}')
plt.axis([2,10,100,550])
plt.grid('True')
plt.xlabel('I')
plt.ylabel('u')
plt.title('Ohms Law')
plt.legend()
plt.show()


def quadratic(x,a,b,c):
    return a*x**2 + b*x + c

#Prob 8
print('Problem 8')
x8 = np.array([-1,1,2,3])
y8 = np.array([5,3,4,8])
(q8, _)=sp.optimize.curve_fit(quadratic,xdata=x8,ydata=y8)
a8,b8,c8 =q8
x8q = np.linspace(-1,3,100)
y8q = quadratic(x8q,a8,b8,c8)
plt.scatter(x8,y8)
plt.plot(x8q,y8q)
plt.title('Problem 8')
plt.show()

#Prob 9
print('Problem 9')
x9 = np.array([2,3,5,6,7])
y9 = np.array([-3,0,1,0,-2])
(q9, _)=sp.optimize.curve_fit(quadratic,xdata=x9,ydata=y9)
a9,b9,c9 =q9
x9q = np.linspace(2,7,100)
y9q = quadratic(x9q,a9,b9,c9)
plt.scatter(x9,y9)
plt.plot(x9q,y9q)
plt.title('Problem 9')
plt.show()

#Prob 10
print('Problem 10')
x10= np.array([1,2,3,4,5])
y10= np.array([2,1.78,1.9,2.35,2.7])
(q10,_)=sp.optimize.curve_fit(quadratic,xdata=x10,ydata=y10)
a10,b10,c10=q10
x10q = np.linspace(1,5,100)
y10q = quadratic(x10q,a10,b10,c10)
plt.scatter(x10,y10)
plt.plot(x10q,y10q)
plt.title('Problem 10')
plt.show()

def cubic(x,a,b,c,d):
    return a*(x**3) + b*(x**2) + c*(x) + d
#Prob 13
print('Problem 13')
x13 = np.array([-2,-1,0,1,2,3])
y13 = np.array([-20,-4,4,4,22,68])
(i13,_) = sp.optimize.curve_fit(cubic,xdata=x13,ydata=y13)
a13,b13,c13,d13 = i13
x13c = np.linspace(-2,3,100)
y13c = cubic(x13c,a13,b13,c13,d13)
plt.scatter(x13,y13)
plt.plot(x13c,y13c)
plt.title('Problem 13')
plt.show()