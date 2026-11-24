import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#19 - 2

#Fized Point

#Prob 3
print('Problem 3')
def prob3(x):
    return (0.5*np.cos(x))
    # x - 0.5cosx = 0
    # 0.5cosx = x
    # Use x = 1
print (sp.optimize.fixed_point(prob3,[1],xtol=1e-12))

#Prob 4
print('Problem 4')
def prob4(x):
    return 1/np.sin(x)
    # x - cscx = 0
    # cscx = x
    # Use x = 1
print (sp.optimize.fixed_point(prob4,[1],xtol=1e-12))

#Prob 7
print('Problem 7')
def prob7(x):
    return np.asin(np.exp(-x))
    # sin x = e^-x
    # Get Smallest Root
    # x = arcsin(e^-x)
print (sp.optimize.fixed_point(prob7,[0],xtol=1e-12))

#Prob 8
print('Problem 8')
def prob8(x):
    return (x**4) - 0.12
    # x^4 - x - 0.12 = 0
    # x^4 - 0.12 = x
    # Use x = 1
print (sp.optimize.fixed_point(prob8,[1],xtol=1e-12)) 

#Prob 10
print('Problem 10')
def prob10(x):
    return 1/np.cosh(x)
    #xcoshx = 1
    #x = 1/coshx
print (sp.optimize.fixed_point(prob10,[1],xtol=1e-12)) 

#Prob 14
def prob14(x):
    return (x**3) - 7
    # Find cbrt(7)
    # x^3 = 7
    # Use x = 2
print(sp.optimize.newton(prob14,[2],tol = 1e-12))

#Prob 15
def prob15(x):
    return (2*x) - np.cos(x)
    # Use x = 1
print(sp.optimize.newton(prob15,[1],tol = 1e-12))

#Prob 18
def prob18(x):
    return (1/8)*((63*x**5)-(70*x**3)+(15*x))
    #Find Largest Root
    #Roots are around -1, -0.5, 0, 0.5, and 1
print(sp.optimize.newton(prob18,[1],tol = 1e-12))

#Prob 20
def prob20(x):
    return x + np.log(x) - 2
    #Use x = 2
print(sp.optimize.newton(prob20,[2],tol = 1e-12))

#Prob 21
def prob21(x):
    return (x**3) - (5*x) + 3
    #Use x = -2,0,2
print(sp.optimize.newton(prob21,[-2],tol = 1e-12))
print(sp.optimize.newton(prob21,[0],tol = 1e-12))
print(sp.optimize.newton(prob21,[2],tol = 1e-12))

#Prob 22
def prob22(x):
    #T1 = 100(1-e^(-0.2x))
    #T2 = 40*(e^(0.01x))
    #x = Time, find T1=T2
    return (100*(1-np.exp(-0.2*x))) - (40*np.exp(-0.01*x))
def prob22p1(x):
    return (100*(1-np.exp(-0.2*x)))
def prob22p2(x):
    return (40*np.exp(-0.01*x))
tp22 = (sp.optimize.newton(prob22,[5],tol = 1e-12))
print(tp22)
print(prob22p1(tp22))
print(prob22p2(tp22))
