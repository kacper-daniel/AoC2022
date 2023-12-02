# part one

data = open('inputs/day2_input.txt', 'r').read().split('\n')
output = 0
max_cubes = {'red': 12, 'green':13, 'blue': 14}
for line in data:
    helper = line.split(":")
    game_id = helper[0].split(" ")[1]
    is_valid = True
    for showing in helper[1].split(";"):
        for cube in showing.split(','):
            for key in max_cubes.keys():
                if key in cube:
                    if max_cubes[key] < int(cube.split(" ")[1].strip()):
                        is_valid = False
    if is_valid:
        output += int(game_id)
print(output)
    
# part two

output = []
for line in data:
    helper = line.split(":")
    min_cubes = {'red': 1, 'green': 1, 'blue': 1}
    for showing in helper[1].split(";"):
        for cube in showing.split(','):
            for key in min_cubes.keys():
                if key in cube:
                    if min_cubes[key] < int(cube.split(" ")[1].strip()):
                        min_cubes[key] = int(cube.split(" ")[1].strip())
    output.append(min_cubes['red']*min_cubes['green']*min_cubes['blue'])
print(sum(output))