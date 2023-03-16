from fractions import Fraction
import numpy as np


def swap_rows(M,i,j):
    # swap rows i and j of M
    for k in range(len(M[i])):
        x = M[i][k]
        M[i][k] = M[j][k]
        M[j][k] = x


def gaussian_elm(M, b):
    # perform Gaussian elimination on matrix M
    # require M to be invertible
    n = len(M)

    if n >= 2:
        for i in range(1, n):
            c = Fraction(M[i][0]/M[0][0])
            for j in range(n):
                M[i][j] = M[i][j] - M[0][j]*c 
            b[i] = b[i] - b[0]*c

        # swap rows if necessary
        if M[1][0] == 0:
            for i in range(2, n):
                if M[i][0] != 0:
                    swap_rows(M, 1, i)
                    swap_rows(b, 1, i)

        #  recurse
        N = [r[1:] for r in M[1:]]
        r = gaussian_elm(N, b[1:])
        for i in range(1, n):
            for j in range(1,n):
                M[i][j] = r[0][i-1][j-1] 
            b[i] = r[1][i-1]

    return (M, b)

def solve_sys_ln_eqs(A, b):
    # solve the system of linear equations Ax = b 
    # require A to be invertible
    r = gaussian_elm(A, b)
    A = r[0]
    b = r[1]
    n = len(A)
    x = [0 for i in range(n)]

    for i in range(n-1,-1,-1):
        z = 0

        for j in range(i+1,n):

            z += A[i][j]*x[j]
        x[i] = (b[i]-z)/A[i][i]


    return x


def solution(m):
    return
   

A = [[Fraction(2,1), Fraction(1,1), Fraction(1,1)], \
    [Fraction(4,1),Fraction(1,1),Fraction(0,1)], \
    [Fraction(-2,1), Fraction(2,1), Fraction(1,1)]]
b = [1, -2, 7]


print(solve_sys_ln_eqs(A,b))


#N = gaussian_elm(M)


#print(sum(M[0]))
#print(Fraction(5,3)/Fraction(5,4))
#abs_prob = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
#print(abs_prob)