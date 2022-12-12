with open(r'inputs\day11.txt') as input_file:
    raw_input = input_file.readlines()
monkeys_templates = [line.strip('\n ') for line in raw_input if line != '\n']
monkeys_list = []
part = 2


class Monkey:
    def __init__(self, items, operation, divisor, true_target, false_target):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.true_target = true_target
        self.false_target = false_target
        self.score = 0

    def throw_item(self):
        item = self.items.pop()
        if 'old + ' in self.operation:
            item = item + int(self.operation.split(' + ')[1])
        elif 'old * old' in self.operation:
            item = item * item
        elif 'old * ' in self.operation:
            item = item * int(self.operation.split(' * ')[1])
        if part == 1:
            item //= 3
        elif part == 2:
            item %= mcm
        if item % self.divisor == 0:
            monkeys_list[self.true_target].items.append(item)
        else:
            monkeys_list[self.false_target].items.append(item)
        self.score += 1


# Making the monkeys from the input
for line in monkeys_templates:
    line_pieces = line.split()
    if line_pieces[0] == 'Starting':
        monkey_items = [int(piece.rstrip(',')) for piece in line_pieces[2:]]
    if line_pieces[0] == 'Operation:':
        monkey_operation = line
    if line_pieces[0] == 'Test:':
        monkey_divisor = int(line_pieces[-1])
    if line_pieces[1] == 'true:':
        monkey_true_target = int(line_pieces[-1])
    if line_pieces[1] == 'false:':
        monkey_false_target = int(line_pieces[-1])
        new_monkey = Monkey(monkey_items, monkey_operation, monkey_divisor, monkey_true_target, monkey_false_target)
        monkeys_list.append(new_monkey)

# Calculating the minimum common multiple for part 2.
divisors = []
mcm = 1
for monkey in monkeys_list:
    divisors.append(monkey.divisor)
for m_divisor in divisors:
    mcm *= m_divisor

# Computing the answers; switch answers by editing whether part is 1 or 2.
times = 20 if part == 1 else 10_000

for _ in range(times):
    for monkey in monkeys_list:
        for n in range(len(monkey.items)):
            monkey.throw_item()

monkey_scores = []
for monkey in monkeys_list:
    monkey_scores.append(monkey.score)

monkey_scores.sort()
monkey_business = monkey_scores[-1] * monkey_scores[-2]
print(f'Part {part}: Monkey business is {monkey_business}')
