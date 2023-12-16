from copy import deepcopy

data = open('inputs/day11_input.txt', 'r').read().split('\n')
#data = open('inputs/day11_example.txt', 'r').read().split('\n')

def part_one():
    # input parsing
    # parsing rows

    data_copy = deepcopy(data)
    map = [[c for c in line.strip()] for line in data_copy]
    appended_rows = 0
    for i in range(len(map)):
        no_galaxies = True
        for j in range(len(map[i])):
            if map[i][j] == "#":
                no_galaxies = False
                break
        if no_galaxies:
            data_copy.insert(i+1+appended_rows, "".join(["." for _ in range(len(map[i]))]))
            appended_rows += 1

    better_map = [[c for c in line.strip()] for line in data_copy]

    # parsing columns

    better_map_copy = deepcopy(better_map)
    appended_cols = 1
    for i in range(len(better_map_copy[0])):
        no_galaxies = True
        for j in range(len(better_map_copy)):
            if better_map_copy[j][i] == "#":
                no_galaxies = False
                break
        if no_galaxies:
            for row in better_map:
                row.insert(i+appended_cols, ".")
            appended_cols += 1

    parsed_map = better_map.copy()

    galaxies = dict()
    galaxies_count = 1
    for i in range(len(parsed_map)):
        for j in range(len(parsed_map[i])):
            if parsed_map[i][j] == "#":
                galaxies[galaxies_count] = [i,j]
                galaxies_count += 1

    paths = []
    for i in range(len(galaxies.keys())):
        for j in range(i + 1, len(galaxies.keys())):
            first_point = galaxies[list(galaxies.keys())[i]]
            second_point = galaxies[list(galaxies.keys())[j]]
            paths.append(abs(first_point[0] - second_point[0]) + abs(first_point[1] - second_point[1]))
    print(f"part 1: {sum(paths)}")


def part_two():
    # input parsing
    # parsing rows

    data_copy = deepcopy(data)
    map = [[c for c in line.strip()] for line in data_copy]
    appended_rows = 0
    for i in range(len(map)):
        no_galaxies = True
        for j in range(len(map[i])):
            if map[i][j] == "#":
                no_galaxies = False
                break
        if no_galaxies:
            data_copy.insert(i+1+appended_rows, "".join(["e" for _ in range(len(map[i]))]))
            appended_rows += 1

    better_map = [[c for c in line.strip()] for line in data_copy]

    # parsing columns

    better_map_copy = deepcopy(better_map)
    appended_cols = 1
    for i in range(len(better_map_copy[0])):
        no_galaxies = True
        for j in range(len(better_map_copy)):
            if better_map_copy[j][i] == "#":
                no_galaxies = False
                break
        if no_galaxies:
            for row in better_map:
                row.insert(i+appended_cols, "empty_col")
            appended_cols += 1

    parsed_map = better_map.copy()

    galaxies = dict()
    galaxies_count = 1
    for i in range(len(parsed_map)):
        for j in range(len(parsed_map[i])):
            if parsed_map[i][j] == "#":
                galaxies[galaxies_count] = [i,j]
                galaxies_count += 1

    paths = []
    expand = 1000000 - 2
    for i in range(len(galaxies.keys())):
        for j in range(i + 1, len(galaxies.keys())):
            first_point = galaxies[list(galaxies.keys())[i]]
            second_point = galaxies[list(galaxies.keys())[j]]
            empty_rows_passed = 0
            empty_cols_passed = 0
            for x in range(abs(first_point[0] - second_point[0])):
                if parsed_map[first_point[0]+x][first_point[1]] == "e":
                    empty_rows_passed += 1

            if second_point[1] >= first_point[1]:
                for y in range(first_point[1]+1, second_point[1]+1):
                    if parsed_map[second_point[0]][y] == "empty_col":
                        empty_cols_passed += 1
            else:
                for y in range(second_point[1]+1, first_point[1]+1):
                    if parsed_map[second_point[0]][y] == "empty_col":
                        empty_cols_passed += 1
            paths.append(
                abs(first_point[0] - second_point[0]) + abs(first_point[1] - second_point[1])
                + (empty_rows_passed + empty_cols_passed)*expand
            )
    print(f"part 2: {sum(paths)}")

part_one()
part_two()