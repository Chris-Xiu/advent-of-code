from tqdm import tqdm


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


output = []
for line in tqdm(lines):
    pattern, numbers = line.split()
    pattern = pattern + ('?' + pattern) * 4
    numbers = [int(i) for i in numbers.split(',')]
    numbers = numbers * 5
    current_state = {}
    next_state = {}
    max_hash = sum(numbers)
    max_dot = len(pattern) - max_hash
    total = 0
    for i in range(len(pattern)):
        if i == 0:
            if pattern[i] == '.' or pattern[i] == '?':
                next_state[(0, 0, 0, 1)] = 1
            if pattern[i] == '#' or pattern[i] == '?':
                next_state[(1, 0, 1, 0)] = 1
        elif i == len(pattern) - 1:
            for k,v in current_state.items():
                current_length, current_hash, total_hash, total_dot = k
                if pattern[i] == '.' or pattern[i] == '?':
                    if current_length != 0 and current_hash == len(numbers) - 1 and current_length == numbers[current_hash]:
                        total += v
                    elif current_length == 0 and current_hash == len(numbers):
                        total += v
                if pattern[i] == '#' or pattern[i] == '?':
                    if current_hash == len(numbers) - 1 and current_length + 1 == numbers[current_hash]:
                        total += v
        else:
            next_state = {}
            for k,v in current_state.items():
                current_length, current_hash, total_hash, total_dot = k
                if total_hash <= max_hash and total_dot <= max_dot:
                    if pattern[i] == '.' or pattern[i] == '?':
                        if current_length != 0  and current_hash < len(numbers) and current_length == numbers[current_hash]:
                            next_key = (0, current_hash+1, total_hash, total_dot+1)
                            next_state[next_key] = next_state.get(next_key, 0) + v
                        elif current_length == 0:
                            next_key = (0, current_hash, total_hash, total_dot+1)
                            next_state[next_key] = next_state.get(next_key, 0) + v
                    if pattern[i] == '#' or pattern[i] == '?':
                        if current_length != 0 and current_length + 1 <= numbers[current_hash]:
                            next_key = (current_length+1, current_hash, total_hash+1, total_dot)
                            next_state[next_key] = next_state.get(next_key, 0) + v
                        elif current_length == 0 and current_hash + 1 <= len(numbers):
                            next_key = (1, current_hash, total_hash+1, total_dot)
                            next_state[next_key] = next_state.get(next_key, 0) + v
        current_state = next_state
    output.append(total)
print(sum(output))