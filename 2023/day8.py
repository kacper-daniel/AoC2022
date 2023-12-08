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

steps = 0
curr = "AAA"
for i in range(len(instructions)):
    where = int(instructions[i])
    curr = destinations[curr][where].strip()
    steps += 1
    if curr == "ZZZ":
        print(steps)
        break
