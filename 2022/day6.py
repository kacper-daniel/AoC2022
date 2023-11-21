# ------
# part 1

data = open('D:/DS/aoc2022/AoC2022/inputs/day6.txt', 'r').read()
last_four = []
index = 1
for x in data:
    last_four.append(x)
    if len(last_four) == 4:
        temp = []
        for y in last_four:
            if y not in temp:
                temp.append(y)
        if len(temp) == 4:
            break
        else:
            last_four.pop(0)
    index += 1
print(index)

# ------
# part 2

data = open('D:/DS/aoc2022/AoC2022/inputs/day6.txt', 'r').read()
last_fourteen = []
index = 1
for x in data:
    last_fourteen.append(x)
    if len(last_fourteen) == 14:
        temp = []
        for y in last_fourteen:
            if y not in temp:
                temp.append(y)
        if len(temp) == 14:
            break
        else:
            last_fourteen.pop(0)
    index += 1
print(index)