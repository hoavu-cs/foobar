import math
import itertools 

# def test_prod_enu(w, h, s):


def factorize(n):
    # output the prime factorization of n assume all primes are the first 20 primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    factorization = []
    while n > 1:
        for x in primes:
            if n % x == 0:
                factorization.append(x)
                n = n/x
    factorization.sort()
    return factorization


def product(L):
    x = 1
    for y in L:
        x *= y
    return x


def solution(w, h, s):
    """
    Let r_1, r_2,..., r_h and c_1, c_2,..., c_w be non-increasing sequences.
    Note that swapping rows or columns do not change the sequences if they
    correspond to the row or column sums. However, such sequences do not uniquely 
    identify the matrix.
    For example, c_1 = 5, c_2 = 5, r_1 = 7, r_2 = 2, r_3 = 1 and m = 5.
    Then we have two possible configurations
    [4 3, 1 1, 0 1] or [5 2, 2 0, 1 0].
    Here, instead, we map number i to the ith prime numbers. This guarantees that
    their product is unique.
    The task is to enumerate through all possible sequences r_i (or c_j) where r_i
    is the product of corresponding prime numbers in row i (or  column j respectively).
    We also need to check if a pair of sequences is valid.
    """
    # P[i][j] contains the list of possible products of i numbers using the first j primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    T = [[[] for j in range(s)] for i in range(max(w,h))]
    for i in range(max(w,h)):
        for j in range(s):
            if i == 0:
                T[i][j] = [k for k in primes[:s]]
            elif j == 0:
                T[i][j] = [math.pow(primes[0], i+1)]
            else:
                T[i][j] = T[i][j-1] + [primes[j]*k for k in T[i-1][j]]

    result = 0
    #print(list(itertools.combinations_with_replacement(T[h-1][s-1], h)))
    for C in list(itertools.combinations_with_replacement(T[w-1][s-1], w)):
        F = []
        P = [1 for i in range(h)]
        for i in C:
            F.append(factorize(i))
        for i in range(h):
            for j in range(w):
                P[i] = P[i]*F[j][i]

        for R in list(itertools.combinations_with_replacement(T[h-1][s-1], h)):
            #print("{}, {}".format(C, R))
            valid = True
            for y in range(len(R)):
                if R[y] != P[y]:
                    valid = False
            if valid == True:
                print("{},{}".format(C, R))
                result += 1

    return result






#print(test_prod_enu(2, 1, 2))
#print(factorize(44))
print(solution(2,2,2))
