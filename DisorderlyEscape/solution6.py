import math




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
    Note that not every pair of sequences corresponds to a configuration.
    If s=2, then r=(2,0), c=(2,0) is not possible (but this is possible if
    s=3).
    WLOG, we consider sequences of decreasing order.
    So the idea is to count the number of possible sequence-pair given w, h, and s.

    """
    s = s-1
    
    # N[i,j,k,d] stores the number of configurations whose top left entry is q
    # and sum of all entry is k
    # sum of entries in the first row and columhn is d
    #N = [[[[0 for d in range(s*(h+w-1)+1)]  for k in range(s*w*h+1)] for j in range(w+1)] for i in range(h+1)]
    
    
    #N = [[[0 for r in range(s*h+1)] for j in range(w*s+1)] for i in range(h*s+1)]
    result = 0
    N = {}
    def computeN(i,j,r,c,k):
        t = (i,j,r,c,k)
        if t in N:
            return N[t]
        else:
            t = (i,j,r,c,k)
            if k == 0:
                N[t] = 1
                return N[t]
            elif k > 0 and (i == 0 or j == 0):
                N[t] = 0
                return N[t]
            elif k > 0 and r == 0 and c == 0:
                N[t] = 0
                return N[t]
            else:
                N[t] = 0
                q_upper = min(k, s)
                for q in range(q_upper+1):
                    r2 = r-q
                    c2 = c-q
                    if r2 >= 0 and c2 >= 0 and k-r2-c2-q >= 0:
                        N[t] += computeN(i-1,j-1,r2,c2,k-r2-c2-q)
                            #if i == 2 and j == 2 and r == 1 and c == 2 and k == 2:

                            #    print("i-1={},j-1={},r2={},c2={},q={},k-r2-c2-q={}xxxx{}".format(i-1,j-1,r2,c2,q,k-r2-c2-q, N[t]))
            return N[t]


    for k in range(s*w*h+1):
        for r in range(s*h+1):
            for c in range(s*w+1):
                computeN(h,w,r,c,k)

    result = 0
    for x in N:
        if x[0] == h and x[1] == w:
            print(x)
            result += N[x]
    for x in N:
        print("N[{}]={}".format(x,N[x]))


    return result


print(solution(2,2,2))
