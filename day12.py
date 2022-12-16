import copy

with open(r'inputs\day12.txt') as input_file:
    raw_input = input_file.readlines()
mountain = [list(line.strip('\n ')) for line in raw_input if line != '\n']


def find_start(table):
    for y in range(len(table)):
        for x in range(len(table[0])):
            if table[y][x] == 'S':
                table[y][x] = 'a'
                return x, y


def find_end(table):
    for y in range(len(table)):
        for x in range(len(table[0])):
            if table[y][x] == 'E':
                table[y][x] = 'z'
                return x, y


def find_options(coord, table, tracking_table, alphabet):
    x, y = coord[0], coord[1]
    height, width = len(table), len(table[0])
    options = []
    if (x != 0 and tracking_table[y][x - 1] is True
            and alphabet.index(table[y][x]) + 1 >= alphabet.index(table[y][x - 1])):
        options.append((x - 1, y))
        tracking_table[y][x - 1] = False
    if (x != width - 1 and tracking_table[y][x + 1] is True
            and alphabet.index(table[y][x]) + 1 >= alphabet.index(table[y][x + 1])):
        options.append((x + 1, y))
        tracking_table[y][x + 1] = False
    if (y != 0 and tracking_table[y - 1][x] is True
            and alphabet.index(table[y][x]) + 1 >= alphabet.index(table[y - 1][x])):
        options.append((x, y - 1))
        tracking_table[y - 1][x] = False
    if (y != height - 1 and tracking_table[y + 1][x] is True
            and alphabet.index(table[y][x]) + 1 >= alphabet.index(table[y + 1][x])):
        options.append((x, y + 1))
        tracking_table[y + 1][x] = False
    return options


def find_path(table, start=None):
    # initial setup
    hill = copy.deepcopy(table)
    steps_count = 0
    if start is None:
        start = find_start(hill)
    searching_list = [start]
    goal = find_end(hill)
    tracking_row = [True for _ in range(len(hill[0]))]
    tracking_table = [tracking_row.copy() for _ in range(len(hill))]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    next_searching_list = []
    while True:
        steps_count += 1
        if not searching_list:
            return False
        for i in range(len(searching_list)):
            tile = searching_list.pop()
            if tile == goal:
                return steps_count - 1
            next_searching_list.extend(find_options(tile, hill, tracking_table, alphabet))
        searching_list, next_searching_list = next_searching_list, []


def find_best_path(table):
    path_lenghts = []
    hill = copy.deepcopy(table)
    find_start(hill)
    for y in range(len(hill)):
        for x in range(len(hill[0])):
            if hill[y][x] == 'a':
                length = find_path(hill, (x, y))
                if length:
                    path_lenghts.append(length)
    best_path_length = min(path_lenghts)
    return best_path_length


print(f'Shortest path starting from S: {find_path(mountain)}')
print(f'Shortest path starting from any lowest point: {find_best_path(mountain)}')
