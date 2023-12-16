import numpy as np
from copy import deepcopy


def roll_north(lines):
    empty_matrix = deepcopy(lines)
    empty_matrix[empty_matrix != '#'] = '.'
    obstacle_row = [0] * len(lines[0])
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'O':
                empty_matrix[obstacle_row[j]][j] = 'O'
                obstacle_row[j] += 1
            elif lines[i][j] == '#':
                obstacle_row[j] = i + 1
    return empty_matrix


def rotate_cycle(lines):
    after_north = roll_north(lines)
    prepare_for_west = after_north[::-1].T
    after_west = roll_north(prepare_for_west).T[::-1]
    prepare_for_south = after_west[::-1]
    after_south = roll_north(prepare_for_south)[::-1]
    prepare_for_east = []
    for array in after_south:
        prepare_for_east.append(array[::-1])
    prepare_for_east = np.array(prepare_for_east).T
    after_east = roll_north(prepare_for_east).T
    final_output = []
    for array in after_east:
        final_output.append(array[::-1])
    return np.array(final_output)


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
lines = [list(line) for line in lines]
lines_array = np.array(lines)


seen_map = []
for i in range(1000000000):
    lines_array = rotate_cycle(lines_array)
    seen = False
    for j in range(len(seen_map)):
        if np.all(lines_array == seen_map[j]):
            seen = True
            break
    if seen:
        break
    else:
        seen_map.append(lines_array)


final_array = seen_map[j + (1000000000 - j) % (i-j) - 1]
total = 0
for i in range(len(final_array)):
    for j in range(len(final_array[i])):
        if final_array[i][j] == 'O':
            total += len(final_array) - i
print(total)