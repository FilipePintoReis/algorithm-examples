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

        def chooseNextNode(self):
                randN = random.random()
                accumulator = 0
                for edge in self.graph.getNodeEdges(self.currentNode):
                     edgePheromones = edge.pheromoneLevel
                     edgeQuality = edge.edgeQuality()
                     accumulator += (edgePheromones ** self.alpha) + (edgeQuality ** self.beta)
        

        #def setPheromones