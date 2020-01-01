from copy import copy, deepcopy

import logic

class Node:
    def __init__(self, state, path, zeroX, zeroY):
        self.state = state
        self.path = path
        self.path.append(state)
        self.heuristicValue = self.getHeuristic2()
        self.zeroX = zeroX
        self.zeroY = zeroY
        
    def getState(self):
        return self.state

    def getPath(self):
        return self.path

    def getChildren(self):
        childs = []
        newArU = deepcopy(self.state)
        newArD = deepcopy(self.state)
        newArL = deepcopy(self.state)
        newArR = deepcopy(self.state)

        if self.zeroX > 0:
            newArL[self.zeroY][self.zeroX] = newArL[self.zeroY][self.zeroX - 1]
            newArL[self.zeroY][self.zeroX - 1] = 0
            childs.append(Node(newArL, self.getPath(), self.zeroX - 1, self.zeroY))
        if self.zeroX < len(newArR) - 1:
            newArR[self.zeroY][self.zeroX] = newArR[self.zeroY][self.zeroX + 1]
            newArR[self.zeroY][self.zeroX + 1] = 0
            childs.append(Node(newArR, self.getPath(), self.zeroX + 1, self.zeroY))
        if self.zeroY > 0: 
            newArU[self.zeroY][self.zeroX] = newArU[self.zeroY - 1][self.zeroX]
            newArU[self.zeroY - 1][self.zeroX] = 0
            childs.append(Node(newArU, self.getPath(), self.zeroX, self.zeroY - 1))
        if self.zeroY < len(newArD) - 1:
            newArD[self.zeroY][self.zeroX] = newArD[self.zeroY + 1][self.zeroX]
            newArD[self.zeroY + 1][self.zeroX] = 0
            childs.append(Node(newArD, self.getPath(), self.zeroX, self.zeroY + 1))
        return childs
    
    def getHeuristic1(self):
        value = 0
        increment = 1
        for i in range(0, len(self.state)):
            for k in range(0, len(self.state)):
                if i == len(self.state) - 1 and k == len(self.state) - 1 and self.state[i][k] != 0:
                    value += increment
                if self.state[i][k] != i * len(self.state) + k + 1 and not (i == len(self.state) - 1 and k == len(self.state) - 1):
                    value += increment
        return value
        
    def getHeuristic2(self):
        value = 0
        for i in range(0, len(self.state)):
            for k in range(0, len(self.state)):
                if i == len(self.state) - 1 and k == len(self.state) - 1 and self.state[i][k] != 0:
                    value += logic.manhattanDist(self.state[i][k], len(self.state), i, k)
                if self.state[i][k] != i * len(self.state) + k + 1 and not (i == len(self.state) - 1 and k == len(self.state) - 1):
                    value += logic.manhattanDist(self.state[i][k], len(self.state), i, k)
        return value
        

    def getFinalValue(self):
        return self.heuristicValue

    def getFinalValueAstar(self):
        return self.heuristicValue + len(self.getPath())
   
        
    def __lt__(self, other):
        if self.getHeuristic2() > other.getHeuristic2():
            return other
        else:
            return self