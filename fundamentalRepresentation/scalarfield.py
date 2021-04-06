# Copyright (c) 2020 rndMemex @ Imperial College London

import numpy as np
import matplotlib as plt
from sympy import Matrix
from sympy.physics.quantum import Operator, Dagger
from sympy.matrices import zeros
from fractions import Fraction
from pprint import pprint
import time

print("PLAYING WITH GELL-MANN MATRICES..")
#vacum expectation value 1/root(2) x [0, 0, 1]T, v ∈ R
#t_a =  λ _a/2

# define Gell-Mann matrices

λ_1 = Matrix([[0, 1, 0 ],
    [1, 0, 0],
    [0, 0, 0]])


λ_2 = Matrix([[0, -1j, 0],
    [1j, 0, 0],
    [0, 0, 0]])


λ_3 = Matrix([[1, 0, 0],
    [0, -1, 0],
    [0, 0, 0]])

λ_4 = Matrix([[1, 0, 0],
    [0, -1, 0],
    [0, 0, 0]])


λ_5 = Matrix([[0, 0, -1j],
    [0, 0, 0],
    [1j, 0, 0]])

λ_6 =Matrix( [[0, 0, 0],
    [0, 0, 1],
    [0, 1, 0]])

λ_7 = Matrix([[0, 0, 0],
    [0, 0, -1j],
    [0, 1j, 0]])

const_8 =np.sqrt(1/3)
λ_8 = Matrix([[1* const_8, 0, 0],
    [0, 1* const_8, 0],
    [0, 0, -2* const_8]])


vev =  np.transpose(Matrix([[0, 0, 1*np.sqrt(1/2)]]))
print("\n")
print("1: Consider Gell-Mann Matrices:")
print("\n")
print("λ_1= {}".format(λ_1))
print("\n")
time.sleep(2)
print("λ_2= {}".format(λ_2))
time.sleep(2)
print("\n")
print("λ_3=  {}".format(λ_3))
time.sleep(2)
print("\n")
print("λ_4=  {}".format(λ_4))
time.sleep(2)
print("\n")
print("λ_5=  {}".format(λ_5))
time.sleep(2)
print("\n")
print("λ_6= {}".format(λ_6))
time.sleep(2)
print("\n")
print("λ_7= {}".format(λ_7))
time.sleep(2)
print("\n")
print("λ_8= {}".format(λ_8))
time.sleep(2)
print("\n")
print("2: Consider a scalar field ϕ with Vacum Expectation Value,")
time.sleep(2)
print("v = {}".format(vev))
time.sleep(2)
print("\n")
print("3: Compute the matrix S_ab = conjugate_transpose(ϕ_0) x {t_a, t_b} x ϕ_0")
time.sleep(1)
print("\n")
print(" - Where ϕ_0 = 1/sqrt(2) x transpose(0, 0, v), v belongs to R")
time.sleep(1)
print("\n")
print(" - Where t_a = λ_a/2 are the generators of SU(3) with 1<= a <=8")
# calculate DxD= S_ab
# define an array of matrices or list 
λ_list = [λ_1, λ_2, λ_3, λ_4, λ_5, λ_6, λ_7, λ_8]
# S_ab = np.zeros((8,8))  using numpy
time.sleep(2)
print("\n")
print("4: Initialising an empty 8x8 Matrix")
S_ab = zeros(8,8)
i,j=0,0
time.sleep(2)
print("\n")
print("5: Computing components S_ij of S_ab: ")
print("\n")
while i < len(λ_list):
        anti_commutator = np.dot(λ_list[i],λ_list[j]) +   np.dot(λ_list[j],λ_list[i])          
        Sab =  np.dot(Dagger(vev),np.dot(anti_commutator,vev))
        print('S_{}{}:{}' . format( i+1 , j+1, Sab))
        print("\n")
        time.sleep(1)
        S_ab[i,j] = Sab
        j +=1
        if j == len(λ_list):
            j=0
            i+=1  

time.sleep(3)
print("\n")
print("S_ab = {}" . format(S_ab))
print("\n")
print("RobotAstray says: Goodbye!")




