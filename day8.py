with open(r'inputs\day8.txt') as input_file:
    raw_input = input_file.readlines()
input_woods = [list(line.rstrip('\n')) for line in raw_input]


def is_covered(tree, list_of_trees):
    for item in list_of_trees:
        if item >= tree:
            return True
    return False


def count_visible_trees(canopy):
    size = len(canopy)
    zipped_canopy = list(zip(*canopy))
    visible_trees_count = (size * 4) - 4
    for x in range(1, size - 1):
        for y in range(1, size - 1):
            tree = canopy[x][y]
            right_trees = canopy[y][x + 1:]
            left_trees = canopy[y][:x]
            up_trees = zipped_canopy[x][:y]
            down_trees = zipped_canopy[x][y + 1:]
            if (not is_covered(tree, right_trees) or not is_covered(tree, left_trees)
                    or not is_covered(tree, up_trees) or not is_covered(tree, down_trees)):
                visible_trees_count += 1
    return visible_trees_count


print(count_visible_trees(input_woods))
