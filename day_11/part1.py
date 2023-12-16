with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


rows_with_galaxy = set()
cols_with_galaxy = set()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            rows_with_galaxy.add(i)
            cols_with_galaxy.add(j)
rows_without = set([i for i in range(len(lines))]) - rows_with_galaxy
cols_without = set([i for i in range(len(lines[0]))]) - cols_with_galaxy


new_map = []
for i in range(len(lines)):
    string = ''
    for j in range(len(lines[0])):
        string += lines[i][j]
        if j in cols_without:
            string += '.'
    new_map.append(string)


new_new_map = []
for i in range(len(new_map)):
    new_new_map.append(new_map[i])
    if i in rows_without:
        new_new_map.append('.' * len(new_map[i]))


galaxy_pos = []
for i in range(len(new_new_map)):
    for j in range(len(new_new_map[0])):
        if new_new_map[i][j] == '#':
           galaxy_pos.append((i, j))


total = 0
for i in range(len(galaxy_pos)):
    y, x = galaxy_pos[i]
    if i < len(galaxy_pos):
        for other_pos in galaxy_pos[i+1:]:
            y_2, x_2 = other_pos
            distance = abs(y - y_2) + abs(x - x_2)
            if distance > 0:
                total += distance
print(total)