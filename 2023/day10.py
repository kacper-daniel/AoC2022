data = open('inputs/day10_input.txt', 'r').read().split('\n')

position = [0,0]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "S":
            position = [i,j]

position = [position[0]-1, position[1]]
last_move = [-1, 0]
steps = 1
while data[position[0]][position[1]] != "S":
    if data[position[0]][position[1]] == "|":
        if last_move == [1, 0]:
            position = [position[0] + 1, position[1]]
        else:
            position = [position[0] - 1, position[1]]
            last_move = [-1, 0]
    elif data[position[0]][position[1]] == "-":
        if last_move == [0, 1]:
            position = [position[0], position[1] + 1]
        else:
            position = [position[0], position[1] - 1]
            last_move = [0, -1]
    elif data[position[0]][position[1]] == "L":
        if last_move == [1, 0]:
            position = [position[0], position[1] + 1]
            last_move = [0, 1]
        else:
            position = [position[0] - 1, position[1]]
            last_move = [-1, 0]
    elif data[position[0]][position[1]] == "J":
        if last_move == [1, 0]:
            position = [position[0], position[1] - 1]
            last_move = [0, -1]
        else:
            position = [position[0] - 1, position[1]]
            last_move = [-1, 0]
    elif data[position[0]][position[1]] == "7":
        if last_move == [-1, 0]:
            position = [position[0], position[1] - 1]
            last_move = [0, -1]
        else:
            position = [position[0] + 1, position[1]]
            last_move = [1, 0]
    elif data[position[0]][position[1]] == "F":
        if last_move == [-1, 0]:
            position = [position[0], position[1] + 1]
            last_move = [0, 1]
        else:
            position = [position[0] + 1, position[1]]
            last_move = [1, 0]
    steps += 1
print(steps // 2)

# TODO: why its not working