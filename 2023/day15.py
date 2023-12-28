data = open('inputs/day15_input.txt', 'r').read()

def hash_algorithm(text):
    curr = 0
    for c in text:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

# part one

output_one = 0
for string in data.split(","):
    output_one += hash_algorithm(string)

print(output_one)

# part two 

boxes = [[] for _ in range(256)]
focal_lenghts = {}

for string in data.split(","):
    if "-" in string:
        label = string[:-1]
        hash_value = hash_algorithm(label)
        if label in boxes[hash_value]:
            boxes[hash_value].remove(label)

    else:
        label, focal = string.split("=")
        focal = int(focal)
        hash_value = hash_algorithm(label)

        if label not in boxes[hash_value]:
            boxes[hash_value].append(label)

        focal_lenghts[label] = focal


output_two = 0
for i in range(len(boxes)):
    if boxes[i] != []:
        for j in range(len(boxes[i])):
            output_two += (i + 1) * (j + 1) * focal_lenghts[boxes[i][j]]
print(output_two) 
