import math


def enu_row_col(k, i, j, r, c, s):
# enumerate possible value for first row sum and column sum
# r and c are upper bound for row and column sum resp.
# k is the total entry sum.
# i is the number of rows and j is the number of columns.
    q_upper = min(k, s, r, c)
    output = []
    for q in range(q_upper+1):
        r2_upper = min(q*(j-1), k-q, r-q)
        for r2 in range(r2_upper+1):
            c2_upper = min(q*(i-1), k-r2-q, c-q)
            for c2 in range(c2_upper+1):
                output.append([r2, c2, q])
    return output
#
def solution(w, h, s):
    """
    Solution sketch
    Consider the sequences (r_1, r_2,..., r_h), (c_1, c_2,..., c_w) 
    that are sorted row sums and column sums respectively.
    These two uniquely determine equivalent configurations as row or column
    exchange do not change the sequences. Furthermore, they form h*w linear 
    equations for h*w variables and therefore the entries must be unique if 
    exist.

    For example, for s=2 the sequences r=(2,0) and c=(1,1) gives
    [1 1
     0 0]. Another examples r=(1,1), c=(1,1) gives
    [1 0
    1 0].
    Note that not every pair of sequences corresponds to a valid configuration.
    If s=2, then r=(2,0), c=(2,0) is not possible (but this is possible if
    s=3).
    We can consider sequences of decreasing order.
    So the idea is to count the number of possible sequence-pair given w, h, and s.

    """
    s = s-1
    result = 0
    N = {}

    def computeN(k, i , j, r, c):
        t = (k,i,j,r,c)
        if t in N:
            return N[t]
        else:
            N[t] = 0
            if k == 0:
                N[t] = 1
            elif k > 0 and i > 0 and j > 0 and r > 0 and c > 0:
                L = enu_row_col(k, i, j, r, c, s)
                for x in L:
                    print(x)
                    N[t] += computeN(k-x[0]-x[1]-x[2], i-1, j-1, x[0], x[1])    
            return N[t]


    computeN(1,1,1,2,2)
    #for k in range(s*w*h+1):
    #    for r in range(s*h+1):
    #        for c in range(s*w+1):
    #            computeN(k,h,w,r,c)

    result = 0
    for x in N:
        if x[1] == h and x[2] == w and x[3] == h*s and x[4] == w*s:
            print(x)
            print(N[x])
            result += N[x]
    for x in N:
        print("N[{}]={}".format(x,N[x]))


    return result


#print(enu_row_col(2, 2, 1, 1, 2, 4))
#print(enu_row_col(4, 1, 1, 0, 0, 1))
print(solution(2,2,2))
