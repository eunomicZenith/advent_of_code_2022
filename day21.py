import re
import dataclasses
from typing import List, Dict, Optional

with open(r'inputs\day21.txt') as input_file:
    raw_input = input_file.readlines()
monkeys_input = [line.rstrip('\n') for line in raw_input]

MonkeyName = str
MonkeyValue = Optional[int]
MonkeyChildren = List[MonkeyName]
MonkeyOperation = Optional[str]
MonkeyParent = Optional[MonkeyName]
MonkeysDict = Dict[MonkeyName, 'Monkey']


@dataclasses.dataclass
class Monkey:
    name: MonkeyName
    value: MonkeyValue
    operation: MonkeyOperation
    children: MonkeyChildren
    parent: MonkeyParent = None

    def assign_parent(self, monkeys_dict: MonkeysDict):
        if self.children:
            for child_name in self.children:
                child = monkeys_dict[child_name]
                child.parent = self.name


def make_monkeys(document) -> MonkeysDict:
    monkeys_dict: MonkeysDict = {}
    for line in document:
        name, definition = re.fullmatch(r'(\w{4}): (.+)', line).groups()
        if definition.isnumeric():
            value = int(definition)
            operation = None
            children = []
        else:
            value = None
            child1, operation, child2 = re.fullmatch(r'(\w{4}) (.) (\w{4})', definition).groups()
            children = [child1, child2]
        this_monkey = Monkey(name, value, operation, children)
        monkeys_dict[name] = this_monkey
    return monkeys_dict


all_monkeys = make_monkeys(monkeys_input)

for monk in all_monkeys.values():
    monk.assign_parent(all_monkeys)


def recursive_calc_value(monkeys_dict: MonkeysDict, starting_name: MonkeyName = 'root') -> MonkeyValue:
    s_monkey: Monkey = monkeys_dict[starting_name]
    children_values = []
    if s_monkey.value is not None:
        return s_monkey.value
    else:
        for child_name in s_monkey.children:
            child_value: MonkeyValue = recursive_calc_value(monkeys_dict, child_name)
            children_values.append(child_value)
        if s_monkey.operation == '+':
            s_monkey.value = children_values[0] + children_values[1]
        elif s_monkey.operation == '-':
            s_monkey.value = children_values[0] - children_values[1]
        elif s_monkey.operation == '*':
            s_monkey.value = children_values[0] * children_values[1]
        elif s_monkey.operation == '/':
            s_monkey.value = children_values[0] // children_values[1]
        return s_monkey.value


def find_humn_side(monkeys_dict: MonkeysDict, target: MonkeyName) -> MonkeyName:
    parent_name = None
    child_name: MonkeyName = 'humn'
    while parent_name != target:
        monke: Monkey = monkeys_dict[child_name]
        parent_name = monke.parent
        child_name = parent_name
    return monke.name


def reverse_engineer(monkeys_dict: MonkeysDict, start_name: MonkeyName = 'root'):
    s_monkey: Monkey = monkeys_dict[start_name]
    humn_side: MonkeyName = find_humn_side(monkeys_dict, start_name)
    children = s_monkey.children.copy()
    children.remove(humn_side)
    other_side: MonkeyName = children[0]
    humn_child: Monkey = monkeys_dict[humn_side]
    other_child: Monkey = monkeys_dict[other_side]
    # computing the human child's value
    if start_name == 'root':
        humn_child.value = other_child.value
    elif s_monkey.operation == '+':
        humn_child.value = s_monkey.value - other_child.value
    elif s_monkey.operation == '*':
        humn_child.value = s_monkey.value // other_child.value
    elif humn_side == s_monkey.children[0]:
        if s_monkey.operation == '-':
            humn_child.value = s_monkey.value + other_child.value
        elif s_monkey.operation == '/':
            humn_child.value = s_monkey.value * other_child.value
    elif humn_side == s_monkey.children[1]:
        if s_monkey.operation == '-':
            humn_child.value = other_child.value - s_monkey.value
        elif s_monkey.operation == '/':
            humn_child.value = other_child.value // s_monkey.value
    # going deeper if need be, printing out humn's value if we've reached it
    if humn_side == 'humn':
        print(f'Needed value for humn: {humn_child.value}')
    else:
        reverse_engineer(monkeys_dict, humn_side)


print('Initial value for root monkey:', recursive_calc_value(all_monkeys))
reverse_engineer(all_monkeys)
