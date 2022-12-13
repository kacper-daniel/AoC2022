# ----------------
# part 1

data = open('D:/DS/aoc2022/AoC2022/inputs/day4.txt', 'r').read().split('\n')
input = [[y.split('-') for y in x.split(',')] for x in data]
output = 0
for x in input:
    if int(x[0][0]) >= int(x[1][0]) and int(x[0][1]) <= int(x[1][1]):
        output += 1
        continue
    elif int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1]):
        output += 1
        continue
print(output)

# -----------
# part 2

data = open('D:/DS/aoc2022/AoC2022/inputs/day4.txt', 'r').read().split('\n')
input = [[y.split('-') for y in x.split(',')] for x in data]
output = 0
for x in input:
    if int(x[0][1]) < int(x[1][0]):
        continue
    elif int(x[0][0]) > int(x[1][1]):
        continue
    else:
        output += 1
print(output)