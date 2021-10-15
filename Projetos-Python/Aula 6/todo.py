from functools import reduce

def firstChars(L):
    if not L:
        return None
    else:
        return list(map(lambda x: str(x)[0], L))

def sum(L):
    if not L: 
        return 0
    else:
        soma = reduce(lambda acc, x: acc + x, L, 0)
        return soma

def avg(L):
    if not L: 
        return 0
    else:
        return sum(L)/len(L)

def maxString(L):
    if not L:
        return None
    else:
        L1 = tuple(map(lambda x: len(str(x)), L))
        return L[L1.index(reduce(max, L1))]

def add2Dict(D, N, S):
    if N is None or not S:
        return None
    else:
        D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    if not L:
        return None
    else:
        D = {}
        for x in L:
            add2Dict(D, len(x), x)
        return D        

def incValue(D, N):
    if not D or N is None:
        return None
    else:
        D[N] = D[N] + 1 if N in D else 1
        return D

def countFirsts(L):
    if not L:
        return None
    else:
        D = {str(L[0][0]): 0}
        for i in map(lambda x: str(x)[0], L):
            incValue(D, i)
        return D

def mostCommonFirstChar(L):
    if not L:
        return None
    else:
        D = countFirsts(L)
        L1 = list(D.keys())
        L2 = list(D.values())
        return L1[L2.index(max(D.values()))]
