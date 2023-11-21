from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

# -----------
# part 1

data = open('D:/DS/aoc2022/AoC2022/inputs/day3.txt', 'r').read().split('\n')
output = 0
for x in data:
    halfs = [x[:len(x)//2], x[len(x)//2:]]
    for i in range(len(halfs[0])):
        if halfs[1].find(halfs[0][i]) != -1:
            if halfs[0][i].islower():
                value = 1
                for lt in alc:
                    if halfs[0][i] == lt:
                        output += value
                        break
                    else:
                        value += 1
            elif halfs[0][i].isupper():
                value = 27
                for lt in auc:
                    if halfs[0][i] == lt:
                        output += value
                        break
                    else:
                        value += 1
            break
print(output)

# -----------------
# part 2

data = open('D:/DS/aoc2022/AoC2022/inputs/day3.txt', 'r').read().split('\n')
output = 0
groups = []
three = []
for i in range(1, len(data) + 1):
    three.append(data[i - 1])
    if i % 3 == 0:
        groups.append(three)
        three = []
for x in groups:
    for letter in x[0]:
        if x[1].find(letter) != -1 and x[2].find(letter) != -1:
            if letter.islower():
                value = 1
                for lt in alc:
                    if letter == lt:
                        output += value
                        break
                    else:
                        value += 1
            elif letter.isupper():
                value = 27
                for lt in auc:
                    if letter == lt:
                        output += value
                        break
                    else:
                        value += 1
            break
print(output)