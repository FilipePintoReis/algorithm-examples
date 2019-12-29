import state

# Example state
matrix_1 = [
    [(2,3), (4,3), (2,10), (12,13), (8,3)],
    [(2,3), (4,3), (2,10), (15,13), (2,3)],
    [(2,3), (4,9), (12,10), (10,9), (2,4)],
    [(2,3), (4,7), (2,10), (12,13), (5,3)],
]

init_x = 0
init_y = 0

current_state = state.State(matrix_1, init_x, init_y)
current_value = 0

# flagging if no better state has been found
flag = True
while flag:
    flag = False
    current_state_evaluation = current_state.state_evaluation()
    neighbors = current_state.generate_neighbors()
    for neighbor in neighbors:
        if neighbor.state_evaluation() > current_state_evaluation:
            flag = True
            current_state = neighbor
            break

print("X value: ", current_state.x, " Y value: ", current_state.y, "State evaluation: ", current_state.state_evaluation())

