import copy

with open(r'inputs\day18.txt') as input_file:
    raw_input = input_file.readlines()
droplet = [[int(x) for x in line.rstrip('\n').split(',')] for line in raw_input]


def find_area(cubes):
    total_area = 0
    for cube in cubes:
        other_cubes = cubes.copy()
        other_cubes.remove(cube)
        cube_area = 6
        for dim_i in range(3):
            for offset in [-1, 1]:
                cube[dim_i] += offset
                if cube in other_cubes:
                    cube_area -= 1
                cube[dim_i] -= offset
        total_area += cube_area
    return total_area


def fill_water(model):
    # find the size of the model
    depth = len(model) - 1
    height = len(model[0]) - 1
    width = len(model[0][0]) - 1
    measures = [width, height, depth]
    # start at a corner, and fill it with water just to make sure
    searching_set = {(0, 0, 0)}
    model[0][0][0] = '.'
    # flooding with water until we run out of adjacent spaces to fill
    while searching_set:
        searching_next = set()
        for point in searching_set:
            point = list(point)
            for dim_i in range(3):
                for offset in [-1, 1]:
                    point[dim_i] += offset
                    if 0 <= point[dim_i] <= measures[dim_i]:
                        x, y, z = point
                        if model[z][y][x] == ' ':
                            model[z][y][x] = '.'
                            searching_next.add((x, y, z))
                    point[dim_i] -= offset
        searching_set = searching_next


def scan_surface(cubes, visualize=False):
    # finding out the size of the droplet
    maximums = [0, 0, 0]
    for cube in cubes:
        for dim_i in range(3):
            maximums[dim_i] = max(maximums[dim_i], cube[dim_i])
    # making the empty 3D model
    total_surface_area = 0
    empty_row = [' ' for _ in range(maximums[0] + 1)]
    plane = [empty_row.copy() for _ in range(maximums[1] + 1)]
    model = [copy.deepcopy(plane) for _ in range(maximums[2] + 1)]
    # putting the lava voxels in it
    for cube in cubes:
        x, y, z = cube
        model[z][y][x] = '#'
    # filling it with water
    fill_water(model)
    # finding out how many adjacent spaces are filled with water, for every cube
    for cube in cubes:
        cube_area = 6
        for dim_i in range(3):
            for offset in [-1, 1]:
                cube[dim_i] += offset
                x, y, z = cube
                if all(0 <= cube[dim_i] <= maximums[dim_i] for dim_i in range(3)) \
                        and model[z][y][x] != '.':
                    cube_area -= 1
                cube[dim_i] -= offset
        total_surface_area += cube_area
    # printing out a layer-by-layer scan if you want
    if visualize is True:
        for plane in model:
            for row in plane:
                print(''.join(row))
            print('+' * (maximums[0] + 1))
    return total_surface_area


print('Surface area of the lava droplet:', find_area(droplet))
print('Contact area between the lava droplet and water:', scan_surface(droplet, visualize=False))
