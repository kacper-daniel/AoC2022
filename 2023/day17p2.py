from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open('inputs/day17_input.txt')]
#grid = [list(map(int, line.strip())) for line in open('inputs/day17_example.txt')]

seen = set()
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    heat_loss, row, col, dr, dc, n = heappop(pq)

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        print(heat_loss)
        break

    if (row, col, dr, dc, n) in seen:
        continue

    seen.add((row, col, dr, dc, n))

    if n < 3 and (dr, dc) != (0, 0):
        nr = row + dr
        nc = col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (heat_loss + grid[nr][nc], nr, nc, dr, dc, n + 1))

    for ndr, ndc in [(1,0), (0,1), (-1,0), (0,-1)]:
        if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
            nr = row + ndr
            nc = col + ndc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (heat_loss + grid[nr][nc], nr, nc, ndr, ndc, 1))