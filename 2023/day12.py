data = open('inputs/day12_input.txt', 'r').read().split('\n')

cache = {}

def count(config, nums):
    if config == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in config else 1
    
    key = (config, nums)
    if key in cache:
        return cache[key]

    res = 0
    if config[0] in ".?":
        res += count(config[1:], nums)
    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            res += count(config[nums[0] + 1:], nums[1:])

    cache[key] = res
    return res

# part one

output_one = 0

for line in data:
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    output_one += count(config, nums)

print(output_one)

# part two

output_two = 0 

for line in data:
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    nums *= 5
    config = "?".join([config] * 5)
    output_two += count(config, nums)

print(output_two)