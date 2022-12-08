with open(r'inputs\day3.txt') as input_file:
    raw_input = input_file.readlines()
rucksacks = [line.rstrip('\n') for line in raw_input]


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


priorities = '*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total_prio = 0
total_badge_prio = 0

for pack in rucksacks:
    half = len(pack) // 2
    part1 = pack[:half]
    part2 = pack[half:]
    shared_set = set(part1).intersection(set(part2))
    shared_str = str(shared_set)[2]
    total_prio += priorities.index(shared_str)

# part 2

for pack1, pack2, pack3 in chunker(rucksacks, 3):
    shared_set = set(pack1).intersection(set(pack2), set(pack3))
    shared_str = str(shared_set)[2]
    total_badge_prio += priorities.index(shared_str)

print(total_prio)
print(total_badge_prio)
