with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


obstacle_row = [0] * len(lines[0])
total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'O':
            total += (len(lines) - obstacle_row[j])
            obstacle_row[j] += 1
        elif lines[i][j] == '#':
            obstacle_row[j] = i + 1
print(total)