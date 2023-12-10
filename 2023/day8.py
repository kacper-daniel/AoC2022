import math

data = open('inputs/day8_input.txt', 'r').read().split('\n')
instructions = data[0]
instructions = instructions.replace("L", "0").replace("R", "1")
destinations = dict()
for line in data[2:]:
    helper = [x.strip() for x in line.split("=")]
    source = helper[0]
    dest_list = [helper[1][1:-1].split(",")[0], helper[1][1:-1].split(",")[1]]
    destinations[source] = dest_list

# part one 

steps_one = 0
not_found_one = True
curr = "AAA"
while not_found_one:
    for i in range(len(instructions)):
        where = int(instructions[i])
        curr = destinations[curr][where].strip()
        steps_one += 1
        if curr == "ZZZ":
            not_found_one = False
            print(steps_one)
            break

# part two

steps_two = 0
cycles = []
currents = [key for key in destinations.keys() if key[-1] == "A"]
for c in currents:
    cycle = 0
    while c[-1] != "Z":
        cycle += 1
        for j in range(len(instructions)):
            if c[-1] != "Z":
                c = destinations[c.strip()][int(instructions[j])]
            else:
                break
    cycles.append(cycle*len(instructions))
steps_two = math.lcm(*cycles)

print(steps_two)
