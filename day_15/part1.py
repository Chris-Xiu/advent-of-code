with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


items = lines[0].split(',')
total = 0
for item in items:
    current_value = 0
    for c in item:
        current_value += ord(c)
        current_value = 17 * current_value
        current_value = current_value % 256
    total += current_value
print(total)