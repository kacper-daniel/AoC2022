data = open('inputs/day10_input.txt', 'r').read().split('\n')

# input parsing

# TODO: parse columns

map = [[c for c in line.strip()] for line in data]
galaxy_count = 1
appended = 0
for i in range(len(map)):
    no_galaxies = True
    for j in range(len(map[i])):
        if map[i][j] == "#":
            no_galaxies = False
            map[i][j] = galaxy_count
            galaxy_count += 1
    if no_galaxies:
        data.insert(i+1+appended, "".join(["." for x in range(len(map[i]))]))
        appended += 1

real_map = [[c for c in line.strip()] for line in data]

# part one
paths = dict()