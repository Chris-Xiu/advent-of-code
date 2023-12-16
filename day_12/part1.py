import itertools
from tqdm import tqdm


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


output = []
for line in tqdm(lines):
    pattern, numbers = line.split()
    numbers = [int(i) for i in numbers.split(',')]
    numbers_total = sum(numbers)
    question_pos = []
    total_hash = 0
    for i in range(len(pattern)):
        if pattern[i] == '?':
            question_pos.append(i)
        elif pattern[i] == '#':
            total_hash += 1
    hash_to_add = numbers_total - total_hash
    if hash_to_add <= 0:
        arrangements = 1
    else:
        all_combinations = itertools.combinations(question_pos, hash_to_add)
        arrangements = 0
        for combination in all_combinations:
            new_pattern = pattern
            for i in combination:
                new_pattern = new_pattern[0:i] + '#' + new_pattern[i+1:]
            new_pattern = new_pattern.replace('?', '.')
            new_pattern = [i for i in  new_pattern.split('.') if len(i) != 0]
            successful = True
            if len(new_pattern) == len(numbers):
                for i in range(len(new_pattern)):
                    if len(new_pattern[i]) != numbers[i]:
                        successful = False
            else:
                successful = False
            if successful:
                arrangements += 1
    output.append(arrangements)
print(sum(output))