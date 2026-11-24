import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#20-1

#No Euler or Heun, RK2 is closest

#Prob 1
#y' + 0.2y = 0, y(0) = 5
def prob1(t,y):
    return -0.2*y
y1 = sp.integrate.solve_ivp(prob1,[0,10],[5],method='RK23',max_step=0.2)
plt.plot(y1.t,y1.y[0],'b--',label='Prob 1')
plt.grid('True')
plt.title('Problem 1')
plt.legend()
plt.show()

#Prob 2
#y' = pi/2*sqrt(1-y^2), y(0)=0
pi = sp.constants.pi
def prob2(t,y):
    return (pi/2)*np.sqrt(1-y**2)
y2 = sp.integrate.solve_ivp(prob2,[0,1],[0],method='RK23',max_step=0.1)
plt.plot(y2.t,y2.y[0],'b--',label='Prob 2')
plt.grid('True')
plt.title('Problem 2')
plt.legend()
plt.show()

#Prob 3
#y' = (y-x)^2, y(0) = 0
def prob3(t,y):
    return (y-t)**2
y3 = sp.integrate.solve_ivp(prob3,[0,5],[0],method='RK23',max_step=0.1)
plt.plot(y3.t,y3.y[0],'b--',label='Prob 3')
plt.grid('True')
plt.title('Problem 3')
plt.legend()
plt.show()

#Prob 4
#y' = (y+x)^2, y(0) = 0
def prob4(t,y):
    return (y+t)**2
y4 = sp.integrate.solve_ivp(prob4,[0,1],[0],method='RK23',max_step=0.1)
plt.plot(y4.t,y4.y[0],'b--',label='Prob 4')
plt.grid('True')
plt.title('Problem 4')
plt.legend()
plt.show()

#Prob 5
#y' = y, y(0) = 1
def prob5(t,y):
    return y
y5 = sp.integrate.solve_ivp(prob5,[0,5],[1],method='RK23',max_step=0.1)
plt.plot(y5.t,y5.y[0],'b--',label='Prob 5')
plt.grid('True')
plt.title('Problem 5')
plt.legend()
plt.show()

#Prob 6
#y' = 2(1+y^2), y(0) = 0
def prob6(t,y):
    return 2*(1+y**2)
y6 = sp.integrate.solve_ivp(prob6,[0,0.5],[0],method='RK23',max_step=0.05)
plt.plot(y6.t,y6.y[0],'b--',label='Prob 6')
plt.grid('True')
plt.title('Problem 6')
plt.legend()
plt.show()

#Prob 7
#y' - xy^2 = 0, y(0) = 1
def prob7(t,y):
    return t*(y**2)
y7 = sp.integrate.solve_ivp(prob7,[0,1],[1],method='RK23',max_step=0.1)
plt.plot(y7.t,y7.y[0],'b--',label='Prob 7')
plt.grid('True')
plt.title('Problem 7')
plt.legend()
plt.show()


#Prob 11
#y' - xy^2 = 0, y(0) = 1
def prob11(t,y):
    return t*(y**2)
y11 = sp.integrate.solve_ivp(prob11,[0,1],[1],method='RK45',max_step=0.1)
plt.plot(y11.t,y11.y[0],'b--',label='Prob 11')
plt.grid('True')
plt.title('Problem 11')
plt.legend()
plt.show()

#Prob 12
#y' = y - y^2, y(0) = 0.2
def prob12(t,y):
    return y - y**2
y12 = sp.integrate.solve_ivp(prob12,[0,5],[0.2],method='RK45',max_step=0.1)
plt.plot(y12.t,y12.y[0],'b--',label='Prob 12')
plt.grid('True')
plt.title('Problem 12')
plt.legend()
plt.show()

#Prob 13
#y' = 1 + y^2, y(0) = 0
def prob13(t,y):
    return 1 + y**2
y13 = sp.integrate.solve_ivp(prob13,[0,1],[0],method='RK45',max_step=0.1)
plt.plot(y13.t,y13.y[0],'b--',label='Prob 13')
plt.grid('True')
plt.title('Problem 13')
plt.legend()
plt.show()

#Prob 14
#y' = (1 - 1/x)y, y(1) = 1
def prob14(t,y):
    return (1-(t**-1))*y
y14b = sp.integrate.solve_ivp(prob14,[1,0.05],[1],method='RK45',max_step=0.1)
y14f = sp.integrate.solve_ivp(prob14,[1,5],[1],method='RK45',max_step=0.1)
plt.plot(y14b.t,y14b.y[0],'b--',label='Prob 14')
plt.plot(y14f.t,y14f.y[0],'b--')
plt.grid('True')
plt.title('Problem 14')
plt.legend()
plt.show()

#Prob 15
#y' + ytanx = sin 2x, y(0) = 1
def prob15(t,y):
    return np.sin(2*t) - (y*np.tan(t))
y15 = sp.integrate.solve_ivp(prob15,[0,5],[1],method='RK45',max_step=0.1)
plt.plot(y15.t,y15.y[0],'b--',label='Prob 15')
plt.grid('True')
plt.title('Problem 15')
plt.legend()
plt.show()

#Prob 17
#y' = 4*(x^3)(y^2), y(0)=0.5
def prob17(t,y):
    return 4*(t**3)* (y**2)
y17 = sp.integrate.solve_ivp(prob17,[0,1],[0.5],method='RK45',max_step=0.1)
plt.plot(y17.t,y17.y[0],'b--',label='Prob 17')
plt.grid('True')
plt.title('Problem 17')
plt.legend()
plt.show()
