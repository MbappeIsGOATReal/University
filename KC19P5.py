import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#19-5

#Problem 3 
print('Problem 3')
x3 = np.linspace(0,1,100)
y3 = x3**2
print(sp.integrate.trapezoid(y3,x3))

#Problem 4
print('Problem 4')
x4 = np.linspace(0,1,100)
y4 = x4**4
print(sp.integrate.trapezoid(y4,x4))

#Problem 5
print('Problem 5')
x5 = np.linspace(0,1,100)
y5 = np.sin((sp.constants.pi/2)*x5)
print(sp.integrate.trapezoid(y5,x5))

#Problem 7
print('Problem 7')
x7 = np.linspace(1,2,100)
y7 = 1/x7
print(sp.integrate.simpson(y7,x=x7))

#Problem 9
print('Problem 9')
x9 = np.linspace(0,0.4,100)
y9 = x9*np.exp(-x9**2)
print(sp.integrate.simpson(y9,x=x9))

#Problem 11
print('Problem 11')
x11 = np.linspace(0,1,100)
y11 = 1/(1+((x11)**2))
print(sp.integrate.simpson(y11,x=x11))

#Problem 16
print('Problem 16')
x16= np.linspace(0.0001,1,100)
y16= np.sin(x16)/x16
print(sp.integrate.simpson(y16,x=x16))

#Problem 20
print('Problem 20')
x20= np.linspace(0,1.25,100)
y20= np.sin(x20**2)
print(sp.integrate.simpson(y20,x=x20))

#Problem 21
print('Problem 21')
x21= np.linspace(0,1.25,100)
y21= np.cos(x21**2)
print(sp.integrate.simpson(y21,x=x21))

#Prob 22
print('Problem 22')
def prob22(x):
    return np.cos(x)
print(sp.integrate.quad(prob22,0,(sp.constants.pi/2)))

#Prob 23
print('Problem 23')
def prob23(x):
    return x*np.exp(-x)
print(sp.integrate.quad(prob23,0,1))

#Prob 24
print('Problem 24')
def prob24(x):
    return np.sin(x**2)
print(sp.integrate.quad(prob24,0,1.25))

#Prob 25
print('Problem 25')
def prob25(x):
    return np.exp(-(x**2))
print(sp.integrate.quad(prob25,0,1))

#Prob 27
print('Problem 27')
def prob27(x):
    return x**4
print(sp.differentiate.derivative(prob27,0)['df'])
print(sp.differentiate.derivative(prob27,0.2)['df'])
print(sp.differentiate.derivative(prob27,0.4)['df'])
print(sp.differentiate.derivative(prob27,0.6)['df'])
print(sp.differentiate.derivative(prob27,0.8)['df'])
