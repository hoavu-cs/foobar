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


def fix(r, c, s):
    # compute the number of fix points given row permutation r
    # and column permutation c (in cycle notations)
    result = 1
    for i in range(len(r)):
        for j in range(len(c)):
            result *= int(math.pow(s, gcd(r[i], c[j])))
    return result


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
