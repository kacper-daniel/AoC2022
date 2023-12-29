from collections import deque

data = open('inputs/day16_input.txt', 'r').read().splitlines()
#data = open('inputs/day16_example.txt', 'r').read().splitlines()

data = [x.replace("\\", "b") for x in data]


def calc(r, c, dr, dc):
    a = [(r, c, dr, dc)]
    seen = set()
    q = deque(a)

    while q:
        r, c, dr, dc = q.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
            continue

        ch = data[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "b":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

    coords = {(r, c) for (r, c, _, _) in seen}

    return len(coords)

max_val = 0

for r in range(len(data[0])):
    max_val = max(max_val, calc(r, -1, 0, 1))
    max_val = max(max_val, calc(r, len(data[0]), 0, -1))

for c in range(len(data)):
    max_val = max(max_val, calc(-1, c, 1, 0))
    max_val = max(max_val, calc(len(data), c, -1, 0))

# part one
print(calc(0, -1, 0, 1))

# part two
print(max_val)

