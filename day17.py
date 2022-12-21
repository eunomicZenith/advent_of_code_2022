import time

with open(r'inputs\day17.txt') as input_file:
    jets_input = input_file.read().rstrip('\n')

with open(r'inputs\day17_rocks.txt') as input_file:
    rocks_input = [line.rstrip('\n') for line in input_file.readlines()]


def make_rocks(rocks_doc):
    current_rock = []
    rocks_list = []
    for line in rocks_doc:
        if line == '':
            rocks_list.append(current_rock)
            current_rock = []
        else:
            current_rock.append(list(line))
    return rocks_list


def avoids_collision(board, rock, rock_top, rock_left):
    acceptable_values = ' .'
    for x in range(len(rock[0])):
        for y in range(len(rock)):
            if board[y + rock_top][x + rock_left] not in acceptable_values and rock[y][x] not in acceptable_values:
                return False
    return True


def drop_rock(board, rock, rock_top, rock_left):
    for x in range(len(rock[0])):
        for y in range(len(rock)):
            if rock[y][x] != '.':
                board[y + rock_top][x + rock_left] = rock[y][x]


def tetris_tower(rocks, shifts_str, goal, visualize=False):
    empty_line = ['.' for _ in range(7)]
    board = [empty_line.copy() for _ in range(5_000)]
    shifts = list(shifts_str)
    r_count = 0
    tower_height = 0
    traces = {}
    offset = 0
    while r_count != goal:
        # defining the rock's data and starting position
        rock = rocks.pop(0)
        rocks.append(rock)
        rock_height = len(rock)
        rock_width = len(rock[0])
        rock_top = tower_height + 3
        rock_left = 2
        rock_done = False
        while not rock_done:
            # sideways movement
            direction = shifts.pop(0)
            shifts.append(direction)
            if direction == '<':
                x_shift = -1
            else:
                x_shift = 1
            attempted_rock_left = rock_left + x_shift
            if 7 - rock_width >= attempted_rock_left >= 0:
                if avoids_collision(board, rock, rock_top, attempted_rock_left):
                    rock_left = attempted_rock_left
            # vertical movement
            attempted_rock_top = rock_top - 1
            if attempted_rock_top >= 0 and avoids_collision(board, rock, attempted_rock_top, rock_left):
                rock_top = attempted_rock_top
            else:
                # the rock has come to rest
                drop_rock(board, rock, rock_top, rock_left)
                r_count += 1
                tower_height = max(rock_top + rock_height, tower_height)
                rock_done = True
                if goal > 10_000:
                    # trace-checking
                    board_top = board[tower_height - 100: tower_height]
                    trace_hash = hash(str(board_top) + str(shifts) + str(rock))
                    if trace_hash in traces and offset == 0:
                        # means we've found a loop!
                        last_r_count, last_tower_height = traces[trace_hash]
                        rocks_elapsed = r_count - last_r_count
                        height_jump = tower_height - last_tower_height
                        loops_to_go = (goal - r_count) // rocks_elapsed
                        r_count += loops_to_go * rocks_elapsed
                        offset = height_jump * loops_to_go
                    else:
                        traces[trace_hash] = (r_count, tower_height)
    if visualize is True:
        for row in board[::-1]:
            if row != empty_line:
                print(''.join(row))
    return tower_height + offset


pieces = make_rocks(rocks_input)
jets = jets_input

print('Part 1: ', tetris_tower(pieces, jets, 2022))
print('Part 2: ', tetris_tower(pieces, jets, 1_000_000_000_000))
