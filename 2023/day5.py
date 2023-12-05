data = open('inputs/day5_input.txt', 'r').read().split('\n\n')
seeds = [int(x) for x in data[0].split(":")[1].strip().split(" ")]
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
all = [seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
i = 1
for line in data[2:]:
    if line == "":
        i += 1
    elif ":" in line:
        continue
    else:
        all[i].append([int(x) for x in line.split(" ")])

# part one

from math import inf

def map(value, list):
    for x in list:
        if value in range(x[1], x[1] + x[2]):
            return x[0] + (value - x[1]) 

output_one = float(inf)
for i in range(len(seeds)):
    soil = map(seeds[i], seed_to_soil)
    next = soil
    for j in range(2, len(all[2:])):
        next = map(next, all[j])
    if next < output_one:
        output_one = next
print(output_one)