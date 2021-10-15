from functools import reduce

def delInitials(L):
    return [name.capitalize() for name in L if len(name) > 1]

def everyOccurrence(S, Q):
    return [pos for pos, c in enumerate(S) if c in Q and c in S]

def factors(N):
    return [f for f in range(2, N) if N%f == 0]

import operator
def isPerfect(N):
    number = [1] + factors(N)
    if reduce(lambda x, y: x + y, number) == N:
        return True
    else:
        return False