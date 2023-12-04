# part one
data = open('inputs/day4_input.txt', 'r').read().split('\n')
output_one = []
for line in data:
    all_numbers = line.split(":")[1]
    winning_numbers = [int(x.strip()) if x != '' else None for x in all_numbers.split("|")[0].split(" ")]
    numbers_you_have = [int(x.strip()) if x!= '' else None for x in all_numbers.split("|")[1].split(" ")]
    helper = 0
    for num in numbers_you_have:
        if num is not None and num in winning_numbers:
            if helper == 0:
                helper += 1
            else:
                helper *= 2
    output_one.append(helper)
print(sum(output_one))

# part two

scratchcards = dict()
for i in range(len(data)):
    all_numbers = data[i].split(":")[1]
    winning_numbers = [int(x.strip()) if x != '' else None for x in all_numbers.split("|")[0].split(" ")]
    numbers_you_have = [int(x.strip()) if x!= '' else None for x in all_numbers.split("|")[1].split(" ")]
    scratchcards[i+1] = {'count': 1, 'wins': 0}

    for num in numbers_you_have:
        if num in winning_numbers:
            scratchcards[i+1]['wins'] += 1

for card in scratchcards:
    for i in range(scratchcards[card]['wins']):
        try:
            scratchcards[card+i+1]['count'] += scratchcards[card]['count']
        except:
            continue

output_two = 0
for card in scratchcards:
    output_two += scratchcards[card]['count']
print(output_two)        

