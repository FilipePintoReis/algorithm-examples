# This is a weighted directed graph
class Graph:
    def __init__(self):
        self.graph = {}
        self.edgeList = []

    def insertNode(self, node, edges=None):
        self.graph[node.name] = [node, []]
        if not edges is None:
            for edge in edges:
                self.createEdge(node.name, edge[0], edge[1]) 
    
    def getNode(self, nodeName):
        node = None
        for node in self.graph:
            if node == nodeName:
                return self.graph[node][0]

    def createEdge(self, node1, node2, weight):
        self.graph[node1][1].append([node2, weight])
        self.edgeList.append(Edge(node1, node2, weight))
    
    def getNodeEdges(self, node):
        retVal = []
        for edge in edgeList:
            if edge.node1 == node:
                retVal.append(edge)
        return retVal

class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.pheromoneLevel = 0
    
    def tweakPheromoneValue(self, value):
        self.pheromoneLevel += value
    
    def printEdge(self):
        print("Printing an Edge")
        print("Node 1: ", self.node1)
        print("Node 2: ", self.node2)
        print("Weight: ", self.weight)
        print("Pheromone: ", self.pheromoneLevel)

    def edgeQuality(self):
        return 1 / self.weight
        
class Node:
    def __init__(self, name, nodeType, foodValue=None):
        self.name = name
        self.nodeType = nodeType
        if not foodValue is None: 
            self.foodValue = foodValue

    def subtractFood(self, value):
        if not self.foodValue is None:
            self.foodValue -= value
    
    def printNode(self):
        print("Printing a Node")
        print("Node name: ", self.name)
        print("Node type: ", self.nodeType)
        if not self.foodValue is None: 
            print("Food amount: ", self.foodValue)

graph = Graph()
graph.insertNode(
    Node('source', 'source'),
    [['node1', 2], ['node2', 5], ['node3', 1]]
)
graph.insertNode(
    Node('node1', 'normal'),
    [['node3', 2]]
)
graph.insertNode(
    Node('node2', 'normal')
)
graph.insertNode(
    Node('node3', 'normal')
)
graph.insertNode(
    Node('food1', 'food', 50)
)

graph.createEdge('node1','food1', 3)

print(graph.getNode('source'))