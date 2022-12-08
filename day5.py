import copy

with open(r'inputs\day5.txt') as input_file:
    raw_input = input_file.readlines()
raw_stack_rows = [line.rstrip('\n') for line in raw_input if '[' in line]
manual = [list(filter(lambda x: x.isnumeric(), line.rstrip('\n').split())) for line in raw_input if 'move' in line]

num_of_stacks = len(raw_stack_rows[0]) // 4
stack_rows = [[raw_row[i * 4 + 1] for i in range(num_of_stacks + 1)] for raw_row in raw_stack_rows]

stack_cols = list(zip(*stack_rows))
stacks = []

for column in stack_cols:
    stack = [item for item in column if item != ' ']
    r_stack = list(reversed(stack))
    stacks.append(r_stack)

stacks_p2 = copy.deepcopy(stacks)

for line in manual:
    times = int(line[0])
    stack1 = int(line[1]) - 1
    stack2 = int(line[2]) - 1
    for i in range(times):
        moved_item = stacks[stack1].pop()
        stacks[stack2].append(moved_item)

last_items = []
for stack in stacks:
    last_items.append(stack[-1])

print(''.join(last_items))

# part 2

for line in manual:
    depth = int(line[0])
    stack1 = int(line[1]) - 1
    stack2 = int(line[2]) - 1
    moved_items = list(stacks_p2[stack1][-depth:])
    stacks_p2[stack1] = stacks_p2[stack1][:-depth]
    stacks_p2[stack2].extend(moved_items)

last_items = []
for stack in stacks_p2:
    last_items.append(stack[-1])

print(''.join(last_items))
