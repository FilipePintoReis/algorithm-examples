class State:
    def __init__(self, matrix, x, y):
        self.matrix = matrix
        self.x = x
        self.y = y

    
    def state_evaluation(self):
        tupl = self.matrix[self.x][self.y]
        return (tupl[0] + tupl[1])/2

    def generate_neighbors(self):
        list_to_be_ret = []
        if self.x - 1 > 0:
            list_to_be_ret.append(State(self.matrix, self.x - 1, self.y)) # not sure if I need to copy objects before passing as argument
        if self.x + 1 < len(self.matrix):
            list_to_be_ret.append(State(self.matrix, self.x + 1, self.y)) 
        if self.y - 1 > 0:
            list_to_be_ret.append(State(self.matrix, self.x, self.y - 1)) 
        if self.y + 1 < len(self.matrix):
            list_to_be_ret.append(State(self.matrix, self.x, self.y + 1)) 
        return list_to_be_ret