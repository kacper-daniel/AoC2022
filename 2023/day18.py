data = open('inputs/day18_input.txt', 'r').read().splitlines()

# part one

points = [(0, 0)]
instructions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

circ = 0

for line in data:
    direction, n, _ = line.split()
    dr, dc = instructions[direction]
    n = int(n)
    circ += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

field = int(0.5 * abs(sum(points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(len(points) - 1)) + points[-1][0] * points[0][1] - points[0][0] * points[-1][1]))
i = field - circ // 2 + 1
print(i + circ)

# part two

points = [(0, 0)]
instructions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

circ = 0

for line in data:
    direction, n, _ = line.split()
    dr, dc = instructions[direction]
    n = int(n)
    circ += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

field = int(0.5 * abs(sum(points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(len(points) - 1)) + points[-1][0] * points[0][1] - points[0][0] * points[-1][1]))
i = field - circ // 2 + 1
print(i + circ)