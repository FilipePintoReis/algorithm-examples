from copy import copy, deepcopy

def solved(ar):
    for i in range(0, len(ar)):
        for k in range(0, len(ar)):
            if i == len(ar) - 1 and k == len(ar) - 1 and ar[i][k] == 0:
                return True
            if ar[i][k] != i * len(ar) + k + 1:
                return False

            
def canMoveR(ar):
    for i in range(0, len(ar)):
        if 0 in ar[i]:
            index = ar[i].index(0)
            if index < len(ar) - 1: return True
            else: return False
            
def canMoveL(ar):
    for i in range(0, len(ar)):
        if 0 in ar[i]:
            index = ar[i].index(0)
            if index > 0: return True
            else: return False
            
def canMoveU(ar):
    for i in range(0, len(ar)):
        if 0 in ar[i]:
            index = i
            if index > 0: return True
            else: return False
            
def canMoveD(ar):
    for i in range(0, len(ar)):
        if 0 in ar[i]:
            index = i
            if index < len(ar) - 1: return True
            else: return False
            
            
def right(ar):
    newAr = deepcopy(ar)
    for i in range(0, len(newAr)):
        if 0 in newAr[i]:
            index = newAr[i].index(0)
            newAr[i][index] = newAr[i][index + 1]
            newAr[i][index + 1] = 0
            return newAr
            
def left(ar): 
    newAr = deepcopy(ar)
    for i in range(0, len(newAr)):
        if 0 in newAr[i]:
            index = newAr[i].index(0)
            newAr[i][index] = newAr[i][index - 1]
            newAr[i][index - 1] = 0
            return newAr
            
def up(ar): 
    newAr = deepcopy(ar)
    for i in range(0, len(newAr)):
        if 0 in newAr[i]:
            index = newAr[i].index(0)
            newAr[i][index] = newAr[i - 1][index]
            newAr[i - 1][index] = 0
            return newAr   

def down(ar): 
    newAr = deepcopy(ar)
    for i in range(0, len(newAr)):
        if 0 in newAr[i]:
            index = newAr[i].index(0)
            newAr[i][index] = newAr[i + 1][index]
            newAr[i + 1][index] = 0
            return newAr
        
def manhattanDist(number, size, actualI, actualK):
    num = deepcopy(number)
    if num == 0:
        num = size*size
    i = number // size
    k = number % size
    
    return abs(i - actualI) + abs(k - actualK)