import math

def comb(a, b):
    return math.factorial(a)/(math.factorial(a-b)*math.factorial(b))



def g(a, b, c):
    # return the number of ways to partition a identical elements into b non-empty sets where
    # each set has size at most c 
    DP = [[[0 for k in range(c+1)] for j in range(b+1)] for i in range(a+1)]

    for i in range(a+1):
        for j in range(b+1):
            for k in range(1, c+1):
                if i == 0:
                    DP[i][j][k] = 1
                elif i > 0 and j == 0:
                    DP[i][j][k] == 0
                else:
                    for t in range(1, min(i, k)+1):

                        DP[i][j][k] += DP[i-t][j-1][t]
    return DP[a][b][c]

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

    def _g(a, b, c):
        # return the number of ways to partition a identical elements into b non-empty sets where
        # each set has size at most c 
        DP = [[[0 for k in range(c+1)] for j in range(b+1)] for i in range(a+1)]

        for i in range(a+1):
            for j in range(b+1):
                for k in range(c+1):
                    for t in range(k+1):
                        if i-t > 0 and j-1 > 0:
                            DP[i][j][k] += DP[i-t][j-1][t]
                        elif i-t == 0 and j-1 == 0: # base case
                            DP[i][j][k] += 1
        return DP[a][b][c]

    ret = 0
    for k in range((s-1)*w*h+1):
        row_configs = g(k, h, w*(s-1))
        col_configs = g(k, w, h*(s-1))

        ret += row_configs*col_configs
        #print("k={}, h={}, w*k={}, f[k,h,w*s]= {}").format(k, h, w*k, _g(k,h,w*s))
        print("k={}, row_configs={}, col_configs={}, ret={}").format(k, row_configs, col_configs, ret)
    return ret

print(g(1,1,1))
print(g(4,3,2))
print(g(4,3,4))
#print(g(0,0,2) == 1)

print(solution(2,2,2))
#assert(solution(2,2,2) == 7)
#assert(solution(2,3,4) == 430)
