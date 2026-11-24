"""
import numpy as np
from PR import preos
from SRK import srkeos
from RK import rkeos
from VDW import vdweos

Tc=(input("Input Tc (K): "))
Pc=(input("Input Pc (bar): "))
w=(input("Input Acentric: "))

T=(input("Input T(K): "))
P=(input("Input P (bar): "))

Tc=float(Tc)
Pc=float(Pc)
w=float(w)
T=float(T)
P=float(P)

preos(Tc,Pc,w,T,P)
"""
import numpy as np
import scipy.optimize as sp

# Define the nonlinear system
def f4(x):
    fa = x[0] + x[1] + x[2] + x[3] + x[4] - 15
    fb = x[0] + (x[1]*x[2]*x[3]*x[4]) - 29
    fc = (x[0]*x[1]) + (x[2]*x[3]*x[4]) - 26
    fd = (x[3]*x[4]) + (x[0]*x[1]*x[2]) - 62
    fe = x[4] + (x[1]*x[2]*x[3]*x[0]) - 121
    return np.array([fa, fb, fc, fd, fe])

# Settings
method = 'broyden1'
tol = 1e-12
required_solutions = 9
found_solutions = []
initial_guesses = []

print("🔍 Searching for 9 unique solutions to the nonlinear system...")
while len(found_solutions) < required_solutions:
    x0 = np.random.uniform(0, 10, size=5)
    sol = sp.root(f4, x0, method=method, tol=tol)

    if sol.success:
        x_rounded = np.round(sol.x, 6)  # Round to 6 decimal places
        # Check uniqueness
        if not any(np.allclose(x_rounded, s, atol=1e-6) for s in found_solutions):
            found_solutions.append(x_rounded)
            initial_guesses.append(np.round(x0, 6))
            print(f"\n✅ Solution #{len(found_solutions)} found:")
            print(f"Initial guess: {np.round(x0, 6)}")
            print(f"Solution:     {x_rounded}")
            print(f"Exit status:  {sol.message}")

print("\n🎯 All 9 unique solutions found!")
