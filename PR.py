import numpy as np
import scipy as sp
import matplotlib as plt

def preos(Tc,Pc,w,T,P):
    s=1+np.sqrt(2) #sigma
    e=1-np.sqrt(2) #epsilon
    o=0.07780 #omega
    f=0.45724 #phi
    Zc=0.30740
    R=83.14 # in mLBar/molK

    Tr=T/Tc
    #print("Tr: ",Tr)
    Pr=P/Pc
    #print("Pr: ",Pr)
    fo=(0.37464+(1.5426*w)-(0.26992*(w**2))) #f(acentic)
    a= (1+(fo*(1-np.sqrt(Tr))))**2  #alpha
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
    print("PR Gas Z: ",Zgasn)

    Zliqo=b
    errorl=1000

    while abs(errorl) > 1e-12: #liq Z
        Zliqn=b+(((Zliqo+(e*b))*(Zliqo+(s*b)))*((1+b-Zliqo)/(q*b)))
        errorl=Zliqn-Zliqo
        #print("Current Guess: ",Zliqn)
        Zliqo=Zliqn
    print("PR Liq Z: ",Zliqn)

    Vgas = (Zgasn*R*T)/P
    Vliq = (Zliqn*R*T)/P
    print(f"PR: The molar volumes are {Vgas} and {Vliq} for gas and liquid respectively in mL/mol")

if __name__ == '__main__':
    preos()