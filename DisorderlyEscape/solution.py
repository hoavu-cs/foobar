import math


def generate_perms(n, m):
    # generate a list of possible cycle lengths (called configurations) 
    # of S_n such that the maximum cycle length is m in non-decreasing order 
    configs = []
    if n == 0:
        return [[]]
    elif n > 0 and m == 0:
        return None
    else:
        for i in range(1, min(m+1, n+1)):
            L = generate_perms(n-i, i)
            if L != None:
                for l in L:
                    l.append(i)
                    configs.append(l)
    return configs

def unique_products(u, v):
    # return the unique product sequences between u and v up to permutations
    # u and v must have length at least 1
    u.sort()
    r = 1
    U = []
    V = []

<<<<<<< HEAD
def num_perms(n, configs):
    # count the number of permutations given a configuration
    result = math.factorial(n)
    p = 1
    for k in range(1, n+1):
        a_k = configs.count(k)
        p *= math.factorial(a_k)*math.pow(k, a_k)
    return int(result//p)


def gcd(x, y):
    # return the GCD
    if y == 0:
        return x
    r = int(x % y)
    return gcd(y , r)

=======
    for i in range(len(u)-1):
        if u[i] == u[i+1]:
            r += 1
            break

    for p in list(itertools.combinations(v, r)):
        if p in V:
            continue
        else:
            V.append(p)
        q = [x for x in v]
        z = [0 for x in range(r)]
        j = 0
        for x in p:
            q.remove(x)
            z[j] = u[j]*x
            j += 1
        W = unique_products(u[r:], q)     

        if len(q) > 0:
            W = unique_products(u[r:], q) 
            for w in W:
                z_copy = z + w
                z_copy.sort()
                if z_copy not in U:
                    U.append(z_copy)
        else:
            z.sort()
            if z not in U:
                U.append(z)

    return U


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
    T = [[[] for j in range(s)] for i in range(h)]
    for i in range(h):
        for j in range(s):
            if i == 0:
                T[i][j] = [k for k in primes[:s]]
            elif j == 0:
                T[i][j] = [math.pow(primes[0], i+1)]
            else:
                T[i][j] = T[i][j-1] + [primes[j]*k for k in T[i-1][j]]
                T[i][j] = list(set(T[i][j]))

    result = 0
    for C in list(itertools.combinations_with_replacement(T[h-1][s-1], w)):     
        configs = []
        for c in C:
            new_configs = []
            F = factorize(c)
            if len(configs) == 0:
                new_configs.append(F)
            else:
                for d in configs:
                    for e in unique_products(d, F):
                        e.sort()
                        if tuple(e) not in new_configs:
                            new_configs.append(e)
            configs = new_configs
        print("C={}, configs={}".format(C,configs))
        result += len(configs)
>>>>>>> c295feaac97cf83b75d483a44ed468058429360a

def fix(r, c, s):
    # compute the number of fix points given row permutation r
    # and column permutation c (in cycle notations)
    result = 1
    for i in range(len(r)):
        for j in range(len(c)):
            result *= int(math.pow(s, gcd(r[i], c[j])))
    return result


<<<<<<< HEAD
def solution(w, h, s):
    # we solve this using Burnside lemma
    P = generate_perms(w, w)
    Q = generate_perms(h, h)
    result = 0
    for p in P:
        for q in Q:
            result += fix(p, q, s)*num_perms(w, p)*num_perms(h, q)
    result = result//(math.factorial(w)*math.factorial(h))
    return str(int(result))
=======



#A = unique_products([2, 2, 3, 3], [5, 7, 7, 11])
#for a in A:
#    print(a)
#print(test_prod_enu(2, 1, 2))
#print(factorize(44))
print(solution(2,2,2))
>>>>>>> c295feaac97cf83b75d483a44ed468058429360a
