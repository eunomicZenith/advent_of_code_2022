import re
import numpy as np
from sympy import Point, Line

with open(r'inputs\day15.txt') as input_file:
    raw_input = input_file.readlines()
template = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
line_nums = [[int(x) for x in re.fullmatch(template, line.rstrip('\n')).groups()] for line in raw_input]
part = 1
is_trial = False
target_row = 10 if is_trial else 2_000_000


class Sensor:
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.beacon = (bx, by)
        self.dist = abs(bx - x) + abs(by - y)

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, dist = {self.dist}'  # purely for my own convenience


sensors = [Sensor(line[0], line[1], line[2], line[3]) for line in line_nums]


def list_edges(l_sensors, row):
    edges = []
    for s in l_sensors:
        interdist = abs(row - s.y)
        if s.dist > interdist:
            left_edge = s.x - (s.dist - interdist)
            right_edge = s.x + (s.dist - interdist)
            edges.append((left_edge, 'Left'))
            edges.append((right_edge, 'Right'))
    return edges


sens_edges = list_edges(sensors, target_row)
sens_edges.sort()
excluded_points = 0
left_count, right_count = 0, 0

for edge in sens_edges:
    if left_count == right_count and edge[1] == 'Left':
        current_start = edge[0]
    if edge[1] == 'Left':
        left_count += 1
    elif edge[1] == 'Right':
        right_count += 1
    if left_count == right_count and edge[1] == 'Right':
        current_end = edge[0]
        excluded_points += current_end - current_start + 1

set_of_annoying_beacons = set()
for sen in sensors:
    if sen.beacon[1] == target_row:
        set_of_annoying_beacons.add(sen.beacon)
excluded_points -= len(set_of_annoying_beacons)

print(excluded_points)

# part 2

g = 0
corner_sensors = []
for i in sensors:
    for j in sensors:
        if i != j and abs(i.x - j.x) + abs(i.y - j.y) == i.dist + j.dist + 2:
            if g < 2 and i not in corner_sensors and j not in corner_sensors:
                corner_sensors.append(i)
                corner_sensors.append(j)
                g += 1

diag_lines = []
for n in range(2):
    corn1 = corner_sensors[n * 2]
    corn2 = corner_sensors[n * 2 + 1]
    dir_x = np.sign(corn2.x - corn1.x)
    dir_y = np.sign(corn2.y - corn1.y)
    x_point = Point(corn1.x + (dir_x * corn1.dist + dir_x), corn1.y)
    y_point = Point(corn1.x, corn1.y + (dir_y * corn1.dist + dir_y))
    d_line = Line(x_point, y_point)
    diag_lines.append(d_line)

hidden_sensor = diag_lines[0].intersection(diag_lines[1])

hidden_coords = hidden_sensor[0].coordinates

frequency = 4_000_000
frequency *= hidden_coords[0]
frequency += hidden_coords[1]
print(frequency)
