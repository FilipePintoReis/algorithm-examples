from copy import copy, deepcopy

import logic

class Node:
    def __init__(self, state, path):
        self.state = state
        self.path = path
        self.path.append(state)
        
    def getState(self):
        return deepcopy(self.state)
    def getPath(self):
        return deepcopy(self.path)
        
    def getChildren(self):
        childs = []
        if logic.canMoveR(self.state):
            childs.append(logic.right(self.state))
        if logic.canMoveL(self.state):
            childs.append(logic.left(self.state))
        if logic.canMoveD(self.state):
            childs.append(logic.down(self.state))
        if logic.canMoveU(self.state):
            childs.append(logic.up(self.state))
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
        return self.getHeuristic2()

    def getFinalValueAstar(self):
        return self.getHeuristic2() + len(self.getPath())
   
        
    def __lt__(self, other):
        if self.getHeuristic2() > other.getHeuristic2():
            return other
        else:
            return self