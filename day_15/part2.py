with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


items = lines[0].split(',')
hash_map = {i:[set()] for i in range(0, 256)}
for item in items:
    if '-' in item:
        label = item.split('-')[0]
        minus = True
    else:
        label = item.split('=')[0]
        lens = item.split('=')[1]
        minus = False
    box_number = 0
    for c in label:
        box_number += ord(c)
        box_number = 17 * box_number
        box_number = box_number % 256
    
    if minus:
        if label in hash_map[box_number][0]:
            hash_map[box_number][0] = hash_map[box_number][0].difference(set([label]))
            for i in range(len(hash_map[box_number])):
                if i != 0:
                    if hash_map[box_number][i][0] == label:
                        hash_map[box_number] = hash_map[box_number][:i] + hash_map[box_number][i+1:]
                        break
    else:
        if label in hash_map[box_number][0]:
            for i in range(len(hash_map[box_number])):
                if i != 0:
                    if hash_map[box_number][i][0] == label:
                        hash_map[box_number][i] = (label, lens)
        else:
            hash_map[box_number][0].add(label)
            hash_map[box_number].append((label, lens))


total = 0
for k,v in hash_map.items():
    box_value = k + 1
    for i in range(len(v)):
        if i != 0:
            total += box_value * i * int(v[i][1])
print(total)