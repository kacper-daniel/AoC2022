import math

# input parsing

data = open('inputs/day5_input.txt', 'r').read().split('\n')
seeds = [int(x) for x in data[0].split(":")[1].strip().split(" ")]
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
all = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
i = 0
for line in data[2:]:
    if line == "":
        i += 1
    elif ":" in line:
        continue
    else:
        all[i].append([int(x) for x in line.split(" ")])

# part one

def map_to_next(value, list):
    for item in list:
        if value in range(item[1], item[1] + item[2]):
            return item[0] + (value-item[1])    
    return value

min_location_first = math.inf
for value in seeds:
    next = value
    for i in range(len(all)):
        next = map_to_next(next, all[i])
    if next < min_location_first:
        min_location_first = next
print(min_location_first)

# part two
