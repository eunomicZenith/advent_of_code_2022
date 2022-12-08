def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


with open(r'inputs\day4.txt') as input_file:
    raw_input = input_file.read()
nums_strings = raw_input.translate(raw_input.maketrans('\n,-', '   ')).split()
nums = [int(num) for num in nums_strings]

full_contains = 0

for a, b, x, y in chunker(nums, 4):
    ab = set(range(a, b + 1))
    xy = set(range(x, y + 1))
    if ab.issubset(xy) or xy.issubset(ab):
        full_contains += 1

print(full_contains)

# part 2

overlaps = 0

for a, b, x, y in chunker(nums, 4):
    ab = set(range(a, b + 1))
    xy = set(range(x, y + 1))
    if not ab.isdisjoint(xy):
        overlaps += 1

print(overlaps)
