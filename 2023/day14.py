# credits to HyperNeutrino 

grid = tuple(open('inputs/day14_input.txt', 'r').read().splitlines())
#grid = open('inputs/day14_input.txt', 'r').read().splitlines()

# part one

# grid = list(map("".join, zip(*grid)))
# grid = ["#".join(["".join(sorted(list(x), reverse=True)) for x in row.split("#")]) for row in grid]
# grid = list(map("".join, zip(*grid)))
# 
# print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))

# part two

def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(x), reverse=True)) for x in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

seen = {grid}
array = [grid]

iter = 0

while True:
    iter += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

first = array.index(grid)
grid = array[(1000000000 - first) % (iter - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))