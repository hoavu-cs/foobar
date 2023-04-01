import math

def comb(a, b):
    return math.factorial(a)/(math.factorial(a-b)*math.factorial(b))

def g(n, k):
    ret = 0
    for i in range(k+1):
        ret += math.pow(-1,i) * comb(k, i) * math.pow(k-i, n)
    ret = ret/math.factorial(k)
    return ret

def solution(w, h, s):
    # Solution sketch:
    """
    let the row sums be r_0, r_1,..., r_{h-1} = R
    let the column sums be c_0, c_2,..., c_{w-1} = C
    swapping rows do not change the row sums except for the ordering 
    swapping columns do not change the column sums except for the ordering
    furthermore, sum_{i=0}^{h-1} r_i = sum_{j=0}^{w-1} c_j

    we say two row sums are equivalent if one can be rearranged to form another e.g., (3,1,1) ~ (1,1,3)
    we define similarly for column sums

    let g(k,t) be the number of ways to partition k similar items into t groups (including empty groups)
    for example, g(5,3) =     ({5}{0}{0}, {4}{1}{0}, {3}{2}{0}, {3}{1}{1}, ...) 
    I think this is called Stirling number of second kind


    claim: the number of equivalent grids = sum_{k=1}^{min(h, w)} [g(k,h) * g(k,w)]
    proof: ...

    """

    ret = 0
    for k in range(h * w, h * w * s + 1):
        row_configs = g(k, h) #comb(k+h-1, h-1)/math.factorial(h-1)
        col_configs = g(k, w) #comb(k+w-1, w-1)/math.factorial(w-1)
        #for i in range(1, w+1):
        #    col_configs += g(k, i)
        print("k = {}, row_configs = {}, col_configs = {}").format(k, row_configs, col_configs)
        ret += row_configs*col_configs
        print("ret = {}").format(ret)

    return ret


print(solution(2,2,2))
assert(g(5, 3) == 25)
assert(g(9, 4) == 7770)


