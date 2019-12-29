class State:
    def __init__(self, matrix, x, y):
        self.matrix = matrix
        self.x = x
        self.y = y

    
    def state_evaluation(self):
        tupl = matrix[self.x][self.y]
        return (tupl[0] + tupl[1])/2