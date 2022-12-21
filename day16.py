import re
from itertools import combinations

with open(r'inputs\day16.txt') as input_file:
    raw_input = input_file.readlines()
template = re.compile(r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)\n?")


class Valve:
    def __init__(self, name, flow, nearbys_str):
        self.name = name
        self.flow = int(flow)
        self.nearbys = nearbys_str.split(', ')
        self.distances = {}  # just to get rid of an annoying warning

    def find_nearbys(self, valves_dict):
        real_nearbys = []
        for neighbor in self.nearbys:
            real_nearbys.append(valves_dict[neighbor])
        self.nearbys = real_nearbys

    def __str__(self):
        return self.name

    def superconnect(self, valves_dict):
        distances = {self.name: 0}
        valves_total = len(valves_dict.values())
        searching_list = [self]
        d = 0
        while len(distances) != valves_total:
            d += 1
            next_to_search = []
            for valve_to_search in searching_list:
                for surrounding_valve in valve_to_search.nearbys:
                    if surrounding_valve.name not in distances:
                        distances[surrounding_valve.name] = d
                        next_to_search.append(surrounding_valve)
            searching_list = next_to_search
        self.distances = distances


def make_valves(document):
    valves_dict = {}
    for line in document:
        name, flow, nearbys_str = re.fullmatch(template, line).groups()
        this_valve = Valve(name, flow, nearbys_str)
        valves_dict[name] = this_valve
    return valves_dict


def assign_nearbys(valves_dict):
    for valve in valves_dict.values():
        valve.find_nearbys(valves_dict)
    return valves_dict


all_valves = assign_nearbys(make_valves(raw_input))

# figure out the shortest distance from any valve to all others using BFS
for v in all_valves.values():
    v.superconnect(all_valves)

# finding the valves that have nonzero flow and are thus actually useful
my_valves = [v for v in all_valves.values() if v.flow > 0]


def dfs(valves_list, time=30, last_valve=all_valves['AA']):
    best_pressure = 0
    # this avoids errors in case we've run out of valves
    if not valves_list:
        return 0
    for next_valve in valves_list:
        # calculate how much time there'd be left if you took that valve
        new_time = time - last_valve.distances[next_valve.name] - 1
        # only proceed if there'd be time left
        if new_time > 0:
            pressure = next_valve.flow * new_time
            # make the list of remaining valves, and feed it to dfs recursively
            next_valves = valves_list.copy()
            next_valves.remove(next_valve)
            next_layer_pressure = dfs(next_valves, new_time, next_valve)
            pressure += next_layer_pressure
            # check if the new pressure beats the record
            best_pressure = max(pressure, best_pressure)
    return best_pressure


def split_search(valves_list):
    valves_set = set(valves_list)
    time = 26
    best_pressure = 0
    attempts = 0
    # First we split 1/14, then 2/13, etc. until we reach 7/8. Anything past that is redundant
    for size in range(1, len(valves_list) // 2 + 1):
        for part1 in combinations(valves_set, size):
            # part1 and part2 are the set of valves split in two
            part1 = set(part1)
            part2 = valves_set.difference(part1)
            # calculate pressures for each of those
            part_1_pressure = dfs(list(part1), time)
            part_2_pressure = dfs(list(part2), time)
            tot_pressure = part_1_pressure + part_2_pressure
            # check if their combined pressure beats the record
            best_pressure = max(best_pressure, tot_pressure)
            attempts += 1
        print(f'Finished size {size}, best pressure so far: {best_pressure}')
    print(f'{attempts} ways of dividing labor were considered.')
    return best_pressure


print(f'Best possible pressure alone: {dfs(my_valves)}')
print(f'Best possible pressure with an elephant friend: {split_search(my_valves)}')
