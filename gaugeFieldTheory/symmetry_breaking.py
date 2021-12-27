# Copyright (c) 2020 Memex @ Imperial College London

import numpy as np
import matplotlib as plt
from numpy.core.numeric import identity
from sympy import Matrix, init_printing
from sympy.physics.quantum import Operator, Dagger
from sympy.matrices import zeros
from fractions import Fraction
from pprint import pprint
import time

# Initialise matrix S_ab 

S_ab = Matrix([[0, 0, 0, 0, 0, 0 ,0,0,0],
    [0, 0, 0, 0, 0, 0 ,0,0,0],
    [0, 0, 0, 0, 0, 0 ,0,0,0],
  [0, 0, 0, 1/4, 0, 0 ,0,0,0],
  [0, 0, 0, 0, 1/4, 0 ,0,0,0],
  [0, 0, 0, 0, 0, 1/4, 0, 0, 0],
  [0, 0, 0, 0, 0, 0 ,1/4, 0, 0],
    [0, 0, 0, 0, 0, 0 ,0,1/3,-1/3],
    [0, 0, 0, 0, 0, 0 ,0,-1/3,1/3]])

print("\n")
print("1: Consider the symmetry breaking matrix S_ab:")
time.sleep(1)
print("\n")
pprint("ν^2 * {}".format(S_ab))
time.sleep(2)
print("\n")
print("2: Find the eigenvalues of S_ab:")
time.sleep(1)
print("\n")
print("- Initialise λ x Identity")
time.sleep(1)
print("\n")
λI= identity(9)
print("λI= λ x {}".format(λI))
time.sleep(1)
print("\n")
print("- Compute det(S_ab - λI) = 0")
time.sleep(1)
print("\n")
λ_i=S_ab.eigenvals()
print("- The eigenvalues are: ν^2 x {}".format(λ_i))
time.sleep(2)
print("\n")
print("3: Find the eigenvactors of S_ab:")
time.sleep(1)
print("\n")
v_i=S_ab.eigenvects()
print("- The eigenvectors are: ν^2 x {}".format(v_i))
time.sleep(1)
print("\n")

