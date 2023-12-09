data = open('inputs/day9_input.txt', 'r').read().split('\n')

def go_level_down(list):
    diffs = []
    for i in range(1, len(list)):
        diffs.append(list[i] - list[i-1])
    return diffs

result = 0
for line in data:
    parsed = [int(x) for x in line.split(" ")]
    helper = [parsed]
    one_below = go_level_down(parsed)

    while sum(one_below) != 0:
        helper.append(one_below)
        one_below = go_level_down(one_below)

    for i in range(2, len(helper) + 1):
        helper[-i].append(helper[-i][-1] + helper[-i+1][-1])

    result += helper[0][-1]

print(result)


# TODO: why its not working