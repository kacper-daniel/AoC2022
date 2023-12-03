# part one
data = open('inputs/day3_input.txt', 'r').read().split('\n')
data_matrix = [line for line in data]
symbols = ['!', '@', '#', '$','%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '/']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def read_number(list, i):
    number = []
    idx = i
    if list[idx - 1] in numbers:
        idx -= 1
    if idx - 1 >= 0:
        if list[idx - 1] in numbers:
            idx -= 1 

    for i in range(3):
        if list[idx] not in numbers:
            break
        number.append(list[idx])
        idx += 1
    return int("".join(number))

output = [-1]
for i in range(1,len(data_matrix) - 1):
    for j in range(1, len(data_matrix[i]) - 1):
        if data_matrix[i][j] in symbols:
            if data_matrix[i-1][j-1] in numbers:
                output.append(read_number(data_matrix[i-1], j-1))
            if data_matrix[i-1][j] in numbers:
                detected_number = read_number(data_matrix[i-1], j)
                output.append(detected_number) if output[-1] != detected_number else None
            if data_matrix[i-1][j+1] in numbers:
                detected_number = read_number(data_matrix[i-1], j+1)
                output.append(detected_number) if output[-1] != detected_number else None
            if data_matrix[i][j-1] in numbers:
                detected_number = read_number(data_matrix[i], j-1)
                output.append(detected_number) if output[-1] != detected_number else None
            if data_matrix[i][j+1] in numbers:
                detected_number = read_number(data_matrix[i], j+1)
                output.append(detected_number) if output[-1] != detected_number else None
            if data_matrix[i+1][j-1] in numbers:
                detected_number = read_number(data_matrix[i+1], j-1)
                output.append(detected_number) if output[-1] != detected_number else None
            if data_matrix[i+1][j] in numbers:
                detected_number = read_number(data_matrix[i+1], j)
                output.append(detected_number) if output[-1] != detected_number else None
            if data_matrix[i+1][j+1] in numbers:
                detected_number = read_number(data_matrix[i+1], j+1)
                output.append(detected_number) if output[-1] != detected_number else None
print(sum(output) + 1)

# part two

output_two = []
for i in range(1,len(data_matrix) - 1):
    for j in range(1, len(data_matrix[i]) - 1):
        if data_matrix[i][j] == "*":
            helper = [-1]
            if data_matrix[i-1][j-1] in numbers:
                helper.append(read_number(data_matrix[i-1], j-1))
            if data_matrix[i-1][j] in numbers:
                detected_number = read_number(data_matrix[i-1], j)
                helper.append(detected_number) if helper[-1] != detected_number else None
            if data_matrix[i-1][j+1] in numbers:
                detected_number = read_number(data_matrix[i-1], j+1)
                helper.append(detected_number) if helper[-1] != detected_number else None
            if data_matrix[i][j-1] in numbers:
                detected_number = read_number(data_matrix[i], j-1)
                helper.append(detected_number) if helper[-1] != detected_number else None
            if data_matrix[i][j+1] in numbers:
                detected_number = read_number(data_matrix[i], j+1)
                helper.append(detected_number) if helper[-1] != detected_number else None
            if data_matrix[i+1][j-1] in numbers:
                detected_number = read_number(data_matrix[i+1], j-1)
                helper.append(detected_number) if helper[-1] != detected_number else None
            if data_matrix[i+1][j] in numbers:
                detected_number = read_number(data_matrix[i+1], j)
                helper.append(detected_number) if helper[-1] != detected_number else None
            if data_matrix[i+1][j+1] in numbers:
                detected_number = read_number(data_matrix[i+1], j+1)
                helper.append(detected_number) if helper[-1] != detected_number else None
            helper.pop(0)
            if len(helper) == 2:
                output_two.append(helper[0]*helper[1])
print(sum(output_two))