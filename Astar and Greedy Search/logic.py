from copy import copy, deepcopy

def solved(ar):
    for i in range(0, len(ar)):
        for k in range(0, len(ar)):
            if i == len(ar) - 1 and k == len(ar) - 1 and ar[i][k] == 0:
                return True
            if ar[i][k] != i * len(ar) + k + 1:
                return False
        
def manhattanDist(number, size, actualI, actualK):
    num = deepcopy(number)
    if num == 0:
        num = size*size
    i = number // size
    k = number % size
    
    return abs(i - actualI) + abs(k - actualK)

def toKey(ar):
    ret = ''
    for el in ar:
        for e in el:
            ret += str(e)
    return ret