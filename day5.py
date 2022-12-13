# ------
# part 1

data = open('D:/DS/aoc2022/AoC2022/inputs/day5.txt', 'r').read().split('\n')
supplies = [x.replace("  ", " ").replace("[", "").replace("]", "") for x in data[:8]]
string_instructions = [x for x in data[10:]]
instructions = [x.replace("move ", "").replace(" from", "").replace(" to", "") for x in string_instructions]
crates = [[],[],[],[],[],[],[],[],[]]
for x in supplies:
    for i in range(0, len(x), 2):
        if x[i] == " ":
            continue
        else: 
            crates[i // 2].append(x[i])
for i in range(len(crates)):
    crates[i].reverse()

for x in instructions:
    temp = [int(a) for a in x.split(" ")] 
    source = temp[1]
    destination = temp[2]
    how_many = temp[0]

    for i in range(how_many):
        item = crates[source-1].pop()
        crates[destination-1].append(item)

output = []
for x in crates:
    output.append(x[-1])
print("".join(output))

# --------
# part 2

data = open('D:/DS/aoc2022/AoC2022/inputs/day5.txt', 'r').read().split('\n')
supplies = [x.replace("  ", " ").replace("[", "").replace("]", "") for x in data[:8]]
string_instructions = [x for x in data[10:]]
instructions = [x.replace("move ", "").replace(" from", "").replace(" to", "") for x in string_instructions]
crates = [[],[],[],[],[],[],[],[],[]]
for x in supplies:
    for i in range(0, len(x), 2):
        if x[i] == " ":
            continue
        else: 
            crates[i // 2].append(x[i])
for i in range(len(crates)):
    crates[i].reverse()

for x in instructions:
    temp = [int(a) for a in x.split(" ")] 
    source = temp[1]
    destination = temp[2]
    how_many = temp[0]

    stack = []
    for i in range(how_many):
        item = crates[source-1].pop()
        stack.append(item)
    
    stack.reverse()
    for x in stack:
        crates[destination-1].append(x)

output = []
for x in crates:
    output.append(x[-1])
print("".join(output))