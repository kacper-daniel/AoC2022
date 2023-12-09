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

not_found_two = True
steps_two = 0
curr = [x for x in destinations.keys() if x.endswith("A")]
while not_found_two:
    for i in range(len(instructions)):
        where = int(instructions[i])
        helper = []
        steps_two += 1
        endswith_z = 0
        for el in curr:
            helper.append(destinations[el][where].strip())
            if helper[-1].endswith("Z"):
                endswith_z += 1
        curr = helper
        if endswith_z == len(curr):
            not_found_two = False
            print(steps_two)
            break

# TODO: why its not working
