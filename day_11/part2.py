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


galaxy_pos = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '#':
           galaxy_pos.append((i, j))


total = 0
for i in range(len(galaxy_pos)):
    y, x = galaxy_pos[i]
    if i < len(galaxy_pos):
        for other_pos in galaxy_pos[i+1:]:
            y_2, x_2 = other_pos
            distance = abs(y - y_2) + abs(x - x_2)
            for y_coor in range(min(y, y_2)+1, max(y, y_2)):
                if y_coor in rows_without:
                    distance += 999999
            for x_coor in range(min(x, x_2)+1, max(x, x_2)):
                if x_coor in cols_without:
                    distance += 999999
            total += distance
print(total)