from queue import PriorityQueue

import node
import logic

def slide_puzzle(ar):
    solvingCycle(ar)
    
    
def solvingCycle(ar):
    q = PriorityQueue()
    root = node.Node(ar,[])
    
    q.put([root.getFinalValue(), root])
    obj = q.get()
    visited = [ar]
    
    while not logic.solved(obj[1].getState()) == True:
        for child in obj[1].getChildren():
            if child not in visited:
                visited.append(child)
                node1 = node.Node(child, obj[1].getPath())
                q.put([node1.getFinalValue(), node1])
        obj = q.get()
        
    print(obj[1].getState())

    

puzzle1 = [
	[4,1,3],
	[6,2,0],
	[7,8,5]
]

puzzle2 = [
	[10, 3, 6, 4],
	[ 1, 5, 8, 0],
	[ 2,13, 7,15],
	[14, 9,12,11]
]

puzzle3 = [
	[ 3, 7,14,15,10],
	[ 1, 0, 5, 9, 4],
	[16, 2,11,12, 8],
	[17, 6,13,18,20],
	[21,22,23,19,24]
]

#slide_puzzle(puzzle1)
slide_puzzle(puzzle2)
