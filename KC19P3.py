import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#19-3

#Prob 5
#Regression of e^-x from 0 to 1 using linear and quadratic regression
#f(0.25) = 0.7788, f(0.75) = 0.47237
print('Problem 5')
x5l1 = np.array([0,0.5])
y5l1 = np.exp(-x5l1)
x5l2 = np.array([0.5,1])
y5l2 = np.exp(-x5l2)
x5q = np.array([0,0.5,1])
y5q = np.exp(-x5q)
def linear(x,a,b):
    return a*x + b
def quadratic(x,a,b,c):
    return a*x**2 + b*x + c
(l5v1, _)=sp.optimize.curve_fit(linear,xdata=x5l1,ydata=y5l1)
(a5l1,b5l1)=l5v1
print(linear(0.25,a5l1,b5l1))
(l5v2, _)=sp.optimize.curve_fit(linear,xdata=x5l2,ydata=y5l2)
(a5l2,b5l2)=l5v2
print(linear(0.75,a5l2,b5l2))
(q5, _)=sp.optimize.curve_fit(quadratic,xdata=x5q,ydata=y5q)
(a5q,b5q,c5q)=q5
print(quadratic(0.25,a5q,b5q,c5q))
print(quadratic(0.75,a5q,b5q,c5q))
def error(x1,x2):
    return (100)*((abs(x1-x2))/x2)
print("Percent Error:")
print(error((linear(0.25,a5l1,b5l1)),(np.exp(-0.25))))
print(error((linear(0.75,a5l1,b5l1)),(np.exp(-0.75))))
print(error((quadratic(0.25,a5q,b5q,c5q)),(np.exp(-0.25))))
print(error((quadratic(0.75,a5q,b5q,c5q)),(np.exp(-0.75))))

#Prob 7
#Regression of sinx from 0 to pi/2 using quadratic regression
#f(-pi/8) = -0.3826, f(pi/8) = 0.3826, f(3pi/8) = 0.92388, f(5pi/8) = 0.92388
print('Problem 7')
pi = sp.constants.pi
x7 = np.array([0,(0.25*pi),(0.75*pi)])
y7 = np.sin(x7)
(q7, _)=sp.optimize.curve_fit(quadratic,xdata=x7,ydata=y7)
(a7,b7,c7)=q7
print(quadratic((-pi/8),a7,b7,c7))
print(quadratic((pi/8),a7,b7,c7))
print(quadratic((3*(pi/8)),a7,b7,c7))
print(quadratic((5*(pi/8)),a7,b7,c7))
print("Percent Error:")
print(error((quadratic((-pi/8),a7,b7,c7)),(np.sin(-pi/8))))
print(error((quadratic((pi/8),a7,b7,c7)),(np.sin(pi/8))))
print(error((quadratic((3*pi/8),a7,b7,c7)),(np.sin(3*pi/8))))
print(error((quadratic((5*pi/8),a7,b7,c7)),(np.sin(5*pi/8))))

#Prob 11
#f(0.5)=0.93470, f(1.5)=0.511828, f(2.5)=-0.048384
print('Problem 11')
x11 = np.array([0,1,2,3])
y11 = np.array([1,0.765198,0.223891,-0.260052])
def cubic(x,a,b,c,d):
    return a*(x**3) + b*(x**2) + c*(x) + d
(c11,_)=sp.optimize.curve_fit(cubic,xdata=x11,ydata=y11)
(a11,b11,c11,d11)=c11
print(cubic(0.5,a11,b11,c11,d11))
print(cubic(1.5,a11,b11,c11,d11))
print(cubic(2.5,a11,b11,c11,d11))
print("Percent Error:")
print(error((cubic(0.5,a11,b11,c11,d11)),(0.93470)))
print(error((cubic(1.5,a11,b11,c11,d11)),(0.511828)))
print(error((cubic(2.5,a11,b11,c11,d11)),(-0.048384)))

#Prob 12
#f(1.25)=1.14645
print('Problem 12')
x12l=np.array([1,1.5])
y12l=np.array([0.94608,1.32468])
x12q=np.array([1,1.5,2])
y12q=np.array([0.94608,1.32468,1.60541])
x12c=np.array([1,1.5,2,2.5])
y12c=np.array([0.94608,1.32468,1.60541,1.77852])
(l12, _)=sp.optimize.curve_fit(linear,xdata=x12l,ydata=y12l)
(a12l,b12l)=l12
print(linear(1.25,a12l,b12l))
(q12, _)=sp.optimize.curve_fit(quadratic,xdata=x12q,ydata=y12q)
(a12q,b12q,c12q)=q12
print(quadratic(1.25,a12q,b12q,c12q))
(c12,_)=sp.optimize.curve_fit(cubic,xdata=x12c,ydata=y12c)
(a12c,b12c,c12c,d12c)=c12
print(cubic(1.25,a12c,b12c,c12c,d12c))
print("Percent Error:")
print(error((linear(1.25,a12l,b12l)),(1.14645)))
print(error((quadratic(1.25,a12q,b12q,c12q)),(1.14645)))
print(error((cubic(1.25,a12c,b12c,c12c,d12c)),(1.14645)))

#Prob 13
print('Problem 13')
def quartic(x,a,b,c,d,e):
    return (a*x**4) + (b*x**3) + (c*x**2) + (d*x) + (e)
x14 = np.array([-4,-2,0,2,4])
y14 = np.array([50,18,2,2,18])
(q14,_) = sp.optimize.curve_fit(quartic,xdata=x14,ydata=y14)
(a14,b14,c14,d14,e14)=q14
(q14b,_) = sp.optimize.curve_fit(quadratic,xdata=x14,ydata=y14)
(a14b,b14b,c14b)=q14b
print(f"Function: {a14}x^4 + {b14}x^3 + {c14}x^2 + {d14}x + {e14}")
print(f"Function: {a14b}x^2 + {b14b}x + {c14b}")
