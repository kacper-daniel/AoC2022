# part one

data = open('inputs/day1_input.txt', 'r').read().split('\n')
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
output = 0
for line in data:
    helper = []
    for x in line:
        if x in numbers:
            helper.append(x)
    output += int("".join([helper[0], helper[-1]]))
print(output)

# part two
output = 0
for line in data:
    corrected_line = line.replace("oneight", "oneeight").replace("threeight", "threeeight").replace("fiveight", "fiveeight").replace("nineight", "nineeight").replace("twone", "twoone").replace("sevenine", "sevennine").replace("eightwo", "eighttwo")

    better_line = corrected_line.replace('eight', "8").replace('seven', "7").replace("zero", "0").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("nine", "9")
    helper = []
    for x in better_line:
        if x in numbers:
            helper.append(x)
    output += int("".join([helper[0], helper[-1]]))
print(output)

    

