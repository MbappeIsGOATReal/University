import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#20-3

#Prob 1
#y'1 = -y1 +y2, y1(0)=0
#y'2 = -y1 -y2, y2(0)=4
def prob1(t,y):
    ya = y[0]
    yb = y[1]
    dya = -ya + yb
    dyb = -ya -yb
    return np.array([dya,dyb])
y1 = sp.integrate.solve_ivp(prob1,[0,10],[0,4],method='RK45',max_step=0.1)
plt.plot(y1.t,y1.y[0],'b',label='y1')
plt.plot(y1.t,y1.y[1],'r',label='y2')
plt.plot(y1.y[0],y1.y[1],'g',label='parametric')
plt.legend()
plt.title('Problem 1')
plt.grid()
plt.show()

#Prob 2
#y'1 = 2y1 - 4y2, y1(0) = 3
#y'2 = -y1 -3y2, y2(0) = 0
def prob2(t,y):
    ya = y[0]
    yb = y[1]
    dya = 2*ya - 4*yb
    dyb = -ya -3*yb
    return np.array([dya,dyb])
y2 = sp.integrate.solve_ivp(prob2,[0,10],[3,0],method='RK45',max_step=0.1)
plt.plot(y2.t,y2.y[0],'b',label='y1')
plt.plot(y2.t,y2.y[1],'r',label='y2')
plt.legend()
plt.title('Problem 2')
plt.grid()
plt.show()

#Prob 3
#y'' + 0.25y = 0
#y(0) = 1, y'(0) = 0
def prob3(t,y):
    ya = y[0]
    yb = y[1]
    dy = yb
    d2y = -0.25*ya
    return np.array([dy,d2y])
y3 = sp.integrate.solve_ivp(prob3,[0,10],[1,0],method='RK45',max_step=0.1)
plt.plot(y3.t,y3.y[0],'b',label='y')
plt.plot(y3.t,y3.y[1],'r',label='dy')
plt.legend()
plt.title('Problem 3')
plt.grid()
plt.show()

#Prob 4
#y'1 = -3y1 + y2 y1(0) = 2
#y'2 = y1 - 3y2 y2(0) = 0
def prob4(t,y):
    ya = y[0]
    yb = y[1]
    dya = -3*ya + yb
    dyb = ya -3*yb
    return np.array([dya,dyb])
y4 = sp.integrate.solve_ivp(prob4,[0,10],[2,0],method='RK45',max_step=0.1)
plt.plot(y4.t,y4.y[0],'b',label='y1')
plt.plot(y4.t,y4.y[1],'r',label='y2')
plt.legend()
plt.title('Problem 4')
plt.grid()
plt.show()

#Prob 5
#y'' - y = x 
#y(0) = 1, y'(0) = -2
def prob5(t,y):
    ya = y[0]
    yb = y[1]
    dy = yb
    d2y = t + ya
    return np.array([dy,d2y])
y5 = sp.integrate.solve_ivp(prob5,[0,10],[1,-2],method='RK45',max_step=0.1)
plt.plot(y5.t,y5.y[0],'b',label='y')
plt.plot(y5.t,y5.y[1],'r',label='dy')
plt.legend()
plt.title('Problem 5')
plt.grid()
plt.show()

#Prob 6
#y1' = y1, y1(0)= 2
#y2' = -y2, y2(0)= 2
def prob6(t,y):
    ya = y[0]
    yb = y[1]
    dya = ya
    dyb = -yb
    return np.array([dya,dyb])
y6 = sp.integrate.solve_ivp(prob6,[0,1],[2,2],method='RK45',max_step=0.01)
plt.plot(y6.t,y6.y[0],'b',label='y1')
plt.plot(y6.t,y6.y[1],'r',label='y2')
plt.legend()
plt.title('Problem 6')
plt.grid()
plt.show()

#Prob 11
#y'' + siny = 0
#y(pi) = 0
#y'(pi) = 1
def prob11(t,y):
    ya = y[0]
    yb = y[1]
    dy = yb
    d2y = -1*np.sin(ya)
    return np.array([dy,d2y])
pi = sp.constants.pi
y11b = sp.integrate.solve_ivp(prob11,[pi,0],[1,1],method='RK45',max_step=0.2)
y11f = sp.integrate.solve_ivp(prob11,[pi,10],[1,1],method='RK45',max_step=0.2)
plt.plot(y11b.t,y11b.y[0],'b',label='y')
plt.plot(y11f.t,y11f.y[0],'b')
plt.plot(y11b.t,y11b.y[1],'r',label='dy')
plt.plot(y11f.t,y11f.y[1],'r')
plt.legend()
plt.title('Problem 11')
plt.grid()
plt.show()
