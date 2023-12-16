import numpy as np
from tqdm import tqdm


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def find_reflection(pattern):
    reflection_point = None
    for i in range(1, len(pattern)):
        if i * 2 <= len(pattern):
            top = pattern[:i]
            bottom = pattern[i:i*2]
        else:
            top = pattern[(2*i-len(pattern)):i]
            bottom = pattern[i:]
        mirror = top[::-1] + (-1) * bottom
        zero_sum = 0
        other_sum = 0
        for j in np.nditer(mirror):
            if j == 0:
                zero_sum += 1
            else:
                other_sum += 1
        if other_sum == 1:
            reflection_point = i
            break
    return reflection_point


patterns = []
one_pattern = []
for i in range(len(lines)):
    if lines[i] == '':
        patterns.append(np.array(one_pattern))
        one_pattern = []
    else:
        line_rafactor = [1 if i == '.' else 2 for i in lines[i]]
        one_pattern.append(line_rafactor)
patterns.append(np.array(one_pattern))


answer = 0
for pattern in tqdm(patterns):
    reflection = find_reflection(pattern)
    if reflection == None:
        reflection = find_reflection(pattern.T)
    else:
        reflection = reflection * 100
    answer += reflection
print(answer)