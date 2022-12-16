with open(r'inputs\day14.txt') as input_file:
    raw_input = input_file.readlines()
numbers_with_commas = [line.rstrip('\n').split(' -> ') for line in raw_input]
rock_paths = [[[int(piece) for piece in element.split(',')] for element in line] for line in numbers_with_commas]


def make_cave(paths, part=1):
    # find the size of the cave
    width, height = 0, 0
    for path in paths:
        for coords in path:
            width = max(width, coords[0])
            height = max(height, coords[1])

    if part == 2:
        height += 2
        width += 500

    # generate the blank cave
    row = [' ' for n in range(width + 1)]
    cave = [row.copy() for n in range(height + 1)]

    # make the actual rock paths
    for path in paths:
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            sorted_x = sorted([start[0], end[0]])
            sorted_y = sorted([start[1], end[1]])
            for x in range(sorted_x[0], sorted_x[1] + 1):
                cave[start[1]][x] = '#'
            for y in range(sorted_y[0], sorted_y[1] + 1):
                cave[y][start[0]] = '#'

    # make the bottom if part 2
    if part == 2:
        cave[-1] = ['#' for _ in range(width + 1)]

    return cave


def count_sand(cave):
    sand_count = 0
    x, y = 500, 0
    try:
        while True:
            # try moving down, then left-down, then right-down
            if cave[y + 1][x] == ' ':
                y += 1
                continue
            elif cave[y + 1][x - 1] == ' ':
                x -= 1
                y += 1
                continue
            elif cave[y + 1][x + 1] == ' ':
                x += 1
                y += 1
                continue
            else:
                cave[y][x] = 'o'
                sand_count += 1

                # stop condition for part 2
                if x == 500 and y == 0:
                    for row in cave:
                        print(''.join(row))
                    return sand_count

                # start back at the top
                x, y = 500, 0

    # stop condition for part 1
    except IndexError:
        for row in cave:
            print(''.join(row))
        return sand_count


print(count_sand(make_cave(rock_paths)))
print(count_sand(make_cave(rock_paths, 2)))
