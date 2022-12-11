# -----------
# part 1
data = open('D:/DS/aoc2022/AoC2022/inputs/day2.txt', 'r').read().split('\n')
input = [x.split(' ') for x in data]
score = 0
for x in input:
    if x[0] == 'A':
        if x[1] == 'X':
            score += 4
        elif x[1] == 'Y':
            score += 8
        elif x[1] == 'Z':
            score += 3
    elif x[0] == 'B':
        if x[1] == 'X':
            score += 1
        elif x[1] == 'Y':
            score += 5
        elif x[1] == 'Z':
            score += 9
    elif x[0] == 'C':
        if x[1] == 'X':
            score += 7
        elif x[1] == 'Y':
            score += 2
        elif x[1] == 'Z':
            score += 6
print(score)

# -----------------
# part 2

data = open('D:/DS/aoc2022/AoC2022/inputs/day2.txt', 'r').read().split('\n')
input = [x.split(' ') for x in data]
score = 0
for x in input:
    if x[0] == 'A':
        if x[1] == 'X':
            score += 3
        elif x[1] == 'Y':
            score += 4
        elif x[1] == 'Z':
            score += 8
    elif x[0] == 'B':
        if x[1] == 'X':
            score += 1
        elif x[1] == 'Y':
            score += 5
        elif x[1] == 'Z':
            score += 9
    elif x[0] == 'C':
        if x[1] == 'X':
            score += 2
        elif x[1] == 'Y':
            score += 6
        elif x[1] == 'Z':
            score += 7
print(score)
