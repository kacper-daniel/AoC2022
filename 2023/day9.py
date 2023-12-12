data = open('inputs/day9_input.txt', 'r').read().split('\n')

def go_level_down(list):
    diffs = []
    for i in range(1, len(list)):
        diffs.append(list[i] - list[i-1])
    return diffs

result = 0
part_two = 0
for line in data:
    parsed = [int(x) for x in line.split(" ")]
    helper = [parsed]
    one_below = go_level_down(parsed)

    while not all([x == 0 for x in one_below]):
        helper.append(one_below)
        one_below = go_level_down(one_below)

    for i in range(2, len(helper) + 1):
        helper[-i].append(helper[-i][-1] + helper[-i+1][-1])
        helper[-i].insert(0, helper[-i][0] - helper[-i+1][0])

    print(helper)

    result += helper[0][-1]
    part_two += helper[0][0]

print(result)
print(part_two)