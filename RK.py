import numpy as np
import scipy as sp
import matplotlib as plt

def rkeos(Tc,Pc,w,T,P):
    s=1 #sigma
    e=0 #epsilon
    o=0.08664 #omega
    f=0.42748 #phi
    Zc=1/3
    R=83.14 # in mLBar/molK

    Tr=T/Tc
    #print("Tr: ",Tr)
    Pr=P/Pc
    #print("Pr: ",Pr)
    fo=1 #f(acentic)
    a= 1/(np.sqrt(Tr))  #alpha
    #print("Aplha: ",a)
    b=(o*Pr)/Tr
    #print("Beta: ",b)
    q=(f*a)/(o*Tr)
    #print("q: ",q)

    Zgaso=1
    errorg=1000

    while abs(errorg) > 1e-12: #gas Z
        Zgasn=1+b-((q*b)*((Zgaso-b)/((Zgaso+(s*b))*(Zgaso+(e*b)))))
        errorg=Zgasn-Zgaso
        #print("Current Guess: ",Zgasn)
        Zgaso=Zgasn
    print("RK Gas Z: ",Zgasn)

    Zliqo=b
    errorl=1000

    while abs(errorl) > 1e-12: #liq Z
        Zliqn=b+(((Zliqo+(e*b))*(Zliqo+(s*b)))*((1+b-Zliqo)/(q*b)))
        errorl=Zliqn-Zliqo
        #print("Current Guess: ",Zliqn)
        Zliqo=Zliqn
    print("RK Liq Z: ",Zliqn)

    Vgas = (Zgasn*R*T)/P
    Vliq = (Zliqn*R*T)/P
    print(f"RK: The molar volumes are {Vgas} and {Vliq} for gas and liquid respectively in mL/mol")

if __name__ == '__main__':
    rkeos()