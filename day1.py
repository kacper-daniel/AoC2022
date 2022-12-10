# -----
# part 1
data = open('D:/DS/aoc2022/AoC2022/inputs/day1.txt', 'r').read().split('\n')
output = []
value = 0 
for x in data:
    if x != "":
        value += int(x)
    else:
        if len(output) == 0:
            output.append(value)
            value = 0
        else:
            if output[0] < value:
                output.insert(0, value)
            else:
                output.append(value)
            value = 0

print(output[0])

# ------
# part 2

data = open('D:/DS/aoc2022/AoC2022/inputs/day1.txt', 'r').read().split('\n')
output = []
value = 0 
for i in range(len(data)):
    if data[i] != "":
        value += int(data[i])
    else:
        if len(output) < 3:
            output.append(value)
            value = 0
        elif len(output) == 3:
            output.sort(reverse=True)
            for i in range(len(output)):
                if value > output[i]:
                    output.pop()
                    output.insert(i, value)
                    break
            value = 0

print(sum(output))

