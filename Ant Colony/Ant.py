import random

class Ant:
        def __init__(self, graph, sourceName, objective):
                self.alpha = 1
                self.beta = 1

                self.graph = graph
                self.sourceName = sourceName
                self.objective = objective
                self.currentNode = self.graph.getNode(sourceName)
                self.pathToObjective = [] # edges
                self.pathBackHome = [] # edges
                self.currentObjective = self.objective

                self.foodAmount = 0

        def setFood(self, amount):
                self.foodAmount = amount

        def setCurrentNode(self, node):
                self.currentNode = node

        def setObjectiveHome(self):
                self.currentObjective = self.sourceName

        def addEdgeToPath(self, edge):
                if self.currentObjective == self.objective:
                        self.pathToObjective.append(edge)
                else: self.pathBackHome.append(edge)

        def chooseNextNode(self):
                randN = random.random()
                accumulator = 0
                nodeEdges = self.graph.getNodeEdges(self.currentNode)

                for edge in nodeEdges:
                        edgePheromones = edge.pheromoneLevel
                        edgeQuality = edge.edgeQuality()
                        accumulator += (edgePheromones ** self.alpha) + (edgeQuality ** self.beta)

                randomN = random.uniform(0, accumulator)

                ac1 = 0
                ac2 = 0
                for edge in range(0, len(nodeEdges)):
                        ac1 = ac2
                        edgePheromones = edge.pheromoneLevel
                        edgeQuality = edge.edgeQuality()
                        ac2 += (edgePheromones ** self.alpha) + (edgeQuality ** self.beta)
                        if randomN > ac1 and randomN < ac2: 
                                return self.graph.getNode(edge.node2)

        def isObjectiveNode(self):
                if self.currentNode.name == self.objective: return True
                else: return False

        def isSourceNode(self):
                if self.currentNode.name == self.sourceName: return True
                else: return False

        #def setPheromones(self):