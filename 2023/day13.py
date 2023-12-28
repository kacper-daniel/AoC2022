import numpy as np

data = open('inputs/day13_input.txt', 'r').read().split('\n\n')

def find_reflection(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return r
        
    return 0

def find_reflection_with_smudge(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

output_one = 0
for block in data:
    grid = block.splitlines()

    row = find_reflection(grid)
    output_one += row * 100

    column = find_reflection(list(zip(*grid)))
    output_one += column

print(output_one)

output_two = 0
for block in data:
    grid = block.splitlines()

    row = find_reflection_with_smudge(grid)
    output_two += row * 100

    column = find_reflection_with_smudge(list(zip(*grid)))
    output_two += column

print(output_two)
