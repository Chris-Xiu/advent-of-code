from tqdm import tqdm


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
MAP = [[c for c in i] for i in lines]


def get_next_state(beam, energized):
    potential_beams = []
    row, col, up_down, left_right = beam
    energized.add((row, col))
    object = MAP[row][col]
    if object == '.':
        potential_beams.append((row+up_down, col+left_right, up_down, left_right))
    elif object == '|':
        if up_down != 0:
            potential_beams.append((row+up_down, col+left_right, up_down, left_right))
        else:
            potential_beams.append((row-1, col, -1, 0))
            potential_beams.append((row+1, col, 1, 0))
    elif object == '-':
        if left_right != 0:
            potential_beams.append((row+up_down, col+left_right, up_down, left_right))
        else:
            potential_beams.append((row, col-1, 0, -1))
            potential_beams.append((row, col+1, 0, 1))
    elif object == '/':
        potential_beams.append((row-left_right, col-up_down, -left_right, -up_down))
    else:
        potential_beams.append((row+left_right, col+up_down, left_right, up_down))
    output_beams = []
    for beam in potential_beams:
        if beam[0] >= 0 and beam[0] < len(MAP) and beam[1] >= 0 and beam[1] < len(MAP[0]):
            output_beams.append(beam)
    return (output_beams, energized)


configurations = []
for row in range(len(MAP)):
    configurations.append((row, 0, 0, 1))
    configurations.append((row, len(MAP[0])-1, 0, -1))
for col in range(len(MAP[0])):
    configurations.append((0, col, 1, 0))
    configurations.append((len(MAP)-1, col, -1, 0))


all_length = []
for config in tqdm(configurations):
    current_beams = [config]
    energized = set()
    seen_state = set()
    while len(current_beams) != 0:
        next_beams = []
        for beam in current_beams:
            seen_state.add(beam)
            new_beams, energized = get_next_state(beam, energized)
            next_beams += new_beams
        current_beams = [i for i in next_beams if i not in seen_state]
    all_length.append(len(energized))
print(max(all_length))