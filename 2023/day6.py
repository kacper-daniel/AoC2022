import re

data = open('inputs/day6_input.txt', 'r').read().split('\n')
times = [int(x) for x in re.findall(r'\d+', data[0])]
distances = [int(x) for x in re.findall(r'\d+', data[1])]

# part one

output_one = 1
for i in range(len(times)):
    valid = 0
    for j in range(times[i]):
        if (times[i] - j)*j > distances[i]:
            valid += 1
    output_one *= valid
print(output_one) 

# part two 
times_longer = int("".join([x for x in re.findall(r'\d+', data[0])]))
distances_longer = int("".join([x for x in re.findall(r'\d+', data[1])]))

output_two = 0
for i in range(times_longer):
    if (times_longer - i)*i > distances_longer:
        output_two += 1
print(output_two)