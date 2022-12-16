import ast

with open(r'inputs\day13.txt') as input_file:
    raw_input = input_file.readlines()
evald_input = [ast.literal_eval(line.strip('\n')) for line in raw_input if line != '\n']


def sum_correct_pair_indexes(items_list):
    c_pairs_sum = 0
    for i in range(len(items_list) // 2):
        left = items_list[i * 2]
        right = items_list[i * 2 + 1]
        if comp_pair(left, right):
            c_pairs_sum += i + 1
    return c_pairs_sum


def comp_pair(left, right):
    # if they're both ints:
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        else:
            return left < right

    # if they're mismatched, list the int:
    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]

    # they're both lists:
    if type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            result = comp_pair(left[i], right[i])
            if result is None:
                continue
            else:
                return result
        if len(left) == len(right):
            return None
        return len(left) < len(right)


print(f'Sum of the indexes of correct pairs: {sum_correct_pair_indexes(evald_input)}')

# part 2


def insertion_sort(items_list):
    sorted_list = []
    while len(items_list) != 0:
        smallest_item = items_list[0]
        for item in items_list[1:]:
            if not comp_pair(smallest_item, item):
                smallest_item = item
        items_list.remove(smallest_item)
        sorted_list.append(smallest_item)
    return sorted_list


def calc_key(items_list):
    items_list.extend([[[2]], [[6]]])
    items_list = insertion_sort(items_list)
    key_2 = items_list.index([[2]]) + 1
    key_6 = items_list.index([[6]]) + 1
    signal_key = key_2 * key_6
    return signal_key


print(f'Signal key: {calc_key(evald_input)}')
