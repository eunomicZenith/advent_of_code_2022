import numpy

with open(r'inputs\day9.txt') as input_file:
    raw_input = input_file.readlines()
instructions = [line.rstrip('\n') for line in raw_input]


def coordify(steps):
    coord = 0
    coords_list = [0]
    ways_dict = {'U': 1j, 'D': -1j, 'R': 1, 'L': -1}
    for step in steps:
        step_pieces = step.split()
        way, times = step_pieces[0], int(step_pieces[1])
        for _ in range(times):
            coord += ways_dict[way]
            coords_list.append(coord)
    return coords_list


def follow_tail(head_coords_list):
    tail_coord = 0
    visited_coords = [0]
    for head_coord in head_coords_list:
        real_diff = head_coord.real - tail_coord.real
        imag_diff = head_coord.imag - tail_coord.imag
        if abs(real_diff) > 1 or abs(imag_diff) > 1:
            tail_coord += numpy.sign(real_diff)
            tail_coord += complex(0, numpy.sign(imag_diff))
        visited_coords.append(tail_coord)
    return visited_coords


rope_length = 9
head_coords = coordify(instructions)

for _ in range(rope_length):
    tail_coords = follow_tail(head_coords)
    head_coords = tail_coords

print(len(set(head_coords)))
