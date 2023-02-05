with open(r'inputs\day20.txt') as input_file:
    raw_input = input_file.readlines()
numbers_input = [int(n.rstrip('\n')) for n in raw_input]


def calc_coords_sum(nums, key=1, iters=1):
    # every number is paired up with its position
    pairs_orig = [[i, n * key] for i, n in enumerate(nums)]
    pairs_copy = pairs_orig.copy()
    nums_len = len(nums)
    # rearranging the list
    for _ in range(iters):
        for pair in pairs_orig:
            displacement = pair[1]
            start_i = pairs_copy.index(pair)
            target_i = (start_i + displacement) % (nums_len - 1)
            pairs_copy.insert(target_i, pairs_copy.pop(start_i))
    # finding the zero
    new_nums = [n[1] for n in pairs_copy]
    zero_i = new_nums.index(0)
    # reordering the list based on the zero's position, then calculating the answer
    reord_nums = new_nums[zero_i:] + new_nums[:zero_i]
    answer = sum([reord_nums[(x + 1) * 1000 % nums_len] for x in range(3)])
    return answer


print(calc_coords_sum(numbers_input))
print(calc_coords_sum(numbers_input, 811589153, 10))
