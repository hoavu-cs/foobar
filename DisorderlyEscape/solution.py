import math

def count_constraint_partitions(i, j, k):
    """
    Return the dynamic programming table for the following problem:
    count the number of ways to write an interger i >= 0 as an ordered sum of j non-negative
    integers whose value is at most k (ignoring permutations of same numbers).
    For example, if i = 3, j = 3, k = 2, then we have the following possibilities
    1 + 1 + 1
    3 + 0 + 0
    0 + 3 + 0
    0 + 0 + 3
    1 + 2 + 0
    2 + 1 + 0
    0 + 1 + 2
    0 + 2 + 1
    1 + 0 + 2
    2 + 0 + 1
    """
    D = [[[0 for c in range(k+1)] for b in range(j+1)] for a in range(i+1)]

    for a in range(i+1):
        for b in range(j+1):
            for c in range(k+1):
                if a == 0:
                    D[a][b][c] = 1
                elif a > 0 and b == 0:
                    D[a][b][c] = 0
                elif a > 0 and b > 0 and c == 0:
                    D[a][b][c] = 0
                else:
                    for t in range(min(a+1, c+1)):
                        D[a][b][c] += D[a-t][b-1][t]

    return D


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
    So the idea is to count the number of possible sequence-pair given w, h, and s.

    """
    s = s-1

    # pre-compute the number of ways to split a column-sum sums into h parts 
    # that corresponding to the values of the rows of that column and p = sum of the entries
    D = count_constraint_partitions(s*h, h, s)

    # T[i][p][k] = number of valid configuration for fixed h and s but with i columns
    # where each column has sum at most z
    T = [[[0 for k in range(s*h+1)] for j in range(s*h*w+1)] for i in range(w+1)]
    for p in range(s*h*w+1):
        for z in range(s*h+1):
            for i in range(w+1):        
                if p == 0:
                    T[i][p][z] = 1
                elif i == 0 and p > 0:
                    T[i][p][z] = 0
                elif i > 0 and p > 0 and z == 0:
                    T[i][p][z] = 0
                else:
                    for t in range(min(z+1,p+1)):
                        T[i][p][z] += D[t][h][s]*T[i-1][p-t][t]
                        #if i == 2 and p == 2 and z == 2:
                            #print(T[i][p][z])
                            #print("({},{},{}) = {}".format(i,p,t,T[i-1][p-t][t]))

    result = 0
    # for p in range(s*h*w+1):
    #     print("p={}, {}".format(p, T[w][p][s*h]))
    # print(T[2][2][1])
    for i in T[w][s*h]:
        result += i
    return result

print(count_constraint_partitions(2,2,1))
print(solution(2,2,2))
#print(count_constraint_partitions(2, 2, 1))