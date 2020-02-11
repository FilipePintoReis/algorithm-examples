from copy import copy, deepcopy
from math import ceil

def solved(ar):
    for i in range(0, len(ar)):
        for k in range(0, len(ar)):
            if i == len(ar) - 1 and k == len(ar) - 1 and ar[i][k] == 0:
                return True
            if ar[i][k] != i * len(ar) + k + 1:
                return False
        
def manhattanDist(number, size, i, k):
    x = k
    y = i
    num = number
    if num == 0:
        num = size*size
    
    xaxis = abs(((x % size) + 1) -(((num - 1) % size) + 1))
    yaxis = abs((ceil(num / size) - 1) - y)
    
    return xaxis + yaxis

def toKey(ar):
    ret = ''
    for el in ar:
        for e in el:
            ret += str(e)
    return ret