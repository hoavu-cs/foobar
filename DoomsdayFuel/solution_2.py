from fractions import Fraction

max_size = 5

# dynamic programming table that stores f(i) to avoid recomputation
DP = [[-1, -1] for i in range(max_size)]

DP[3][0] = 0
DP[3][1] = 0
DP[4][0] = 0
DP[4][1] = 0
DP[2][0] = 1
DP[2][1] = 0

DP[0][0] = 0
DP[0][1] = 1

def f(i, p, n): 
    # return the probability of getting to state i in terms of a_0 starting at state i
    # p is the probability transition matrix
    # a_0 is the probability of getting to state i from state 0 
    # returns u and v such that f(i) = u + v a_0
    
    #print(i)
    #print(DP[0])
    if p[i][i] == Fraction(1,1):
        DP[i][0] = 0
        DP[i][1] = 1
    else:
        u = 0
        v = 0
        for j in range(n):
            if p[i][j] > 0:
                if p[j][j] == 1 and j != i:
                    DP[j][0] = 0
                    DP[j][0] = 0
                elif DP[j][0] == -1:
                    f(j, p, n) 
                u +=  p[i][j] * DP[j][0]
                v +=  p[i][j] * DP[j][1]

        DP[i][0] = u 
        DP[i][1] = v
                

def solution(m):
    n = len(m)
    p = [[Fraction(0,1) for i in range(n)] for j in range(n)]
    term_st = set()
    abs_prob = {}
    
    # create probability transition matrix
    for i in range(n):
        row_sum = sum(m[i])
        if row_sum == 0:
            p[i][i] = Fraction(1,1)
            term_st.add(i)
            DP[i][0] = 1
            DP[i][1] = 0
        else:
            for j in range(n):
                p[i][j] = Fraction(m[i][j], row_sum)

    # compute u, v such that a_i = u + v a_i and then a_i = u/(1-v)
    #for i in term_st:
    f(2, p, n)
    print(DP)

        #abs_prob[i] = Fraction(DP[i][0],1-DP[i][1])
    return abs_prob

abs_prob = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
#print(abs_prob)