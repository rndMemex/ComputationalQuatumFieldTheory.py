import numpy as np
import matplotlib as plt
from sympy import Matrix
from sympy.physics.quantum import Operator, Dagger
from sympy.matrices import zeros
from fractions import Fraction


#this is a script with default vacum expectation valu 1/root(2) x [0, 0, v]T, v ∈ R
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

# calculate DxD= S_ab
# define an array of matrices or list 
λ_list = [λ_1, λ_2, λ_3, λ_4, λ_5, λ_6, λ_7, λ_8]
# S_ab = np.zeros((8,8))  using numpy
S_ab = zeros(8,8)
i,j=0,0
while i < len(λ_list):
        anti_commutator = np.dot(λ_list[i],λ_list[j]) +   np.dot(λ_list[j],λ_list[i])          
        Sab =  np.dot(Dagger(vev),np.dot(anti_commutator,vev))
        # print('S_{}{}:{}' . format( i+1 , j+1, Sab))
        S_ab[i,j] = Sab
        j +=1
        if j == len(λ_list):
            j=0
            i+=1  


print("S_ab matrix:{}" . format(S_ab))




