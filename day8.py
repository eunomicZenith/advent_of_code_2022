with open(r'inputs\day8.txt') as input_file:
    raw_input = input_file.readlines()
input_woods = [list(line.rstrip('\n')) for line in raw_input]


def is_visible(tree, list_of_trees):
    for item in list_of_trees:
        if item >= tree:
            return False
    return True


def viewing_dist(tree, list_of_trees):
    streak = 0
    for item in list_of_trees:
        streak += 1
        if item >= tree:
            return streak
    return streak


def find_best_treehouse(canopy):
    size = len(canopy)
    zipped_canopy = list(zip(*canopy))
    visible_trees_count = size * 4 - 4
    highest_scenic_score = 0
    for x in range(1, size - 1):
        for y in range(1, size - 1):
            tree = canopy[y][x]
            up_trees = zipped_canopy[x][y - 1::-1]
            down_trees = zipped_canopy[x][y + 1:]
            left_trees = canopy[y][x - 1::-1]
            right_trees = canopy[y][x + 1:]
            directions = [up_trees, down_trees, left_trees, right_trees]
            if any(is_visible(tree, direction) for direction in directions):
                visible_trees_count += 1
            tree_scenic_score = 1
            for direction in directions:
                tree_scenic_score *= viewing_dist(tree, direction)
            if tree_scenic_score > highest_scenic_score:
                highest_scenic_score = tree_scenic_score
    return visible_trees_count, highest_scenic_score


visible_trees, best_view = find_best_treehouse(input_woods)
print(f'Visible trees: {visible_trees}')
print(f'Best scenic score: {best_view}')
