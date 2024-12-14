from collections import OrderedDict
from tools.file import read_file_as_strings
import re

INPUT_PATTERN = r"([-]*\d+)"


def parse_input(filepath):
    lines = read_file_as_strings(filepath)
    robots = []
    for line in lines:
        x, y, dx, dy = re.findall(INPUT_PATTERN, line)
        robot = [(int(x), int(y)), (int(dx), int(dy))]
        robots.append(robot)

    return robots


def calculate_positions(robot, map_size):
    positions = OrderedDict()
    current_position, velocity = robot

    while current_position not in positions:
        positions[current_position] = None
        current_position = step(current_position, velocity, map_size)

    return list(positions)


def step(location, direction, map_size):
    x, y = location
    dx, dy = direction
    bx, by = map_size
    new_x = (x + dx) % bx
    new_y = (y + dy) % by

    return (new_x, new_y)


def pos_after_seconds(positions, seconds):
    pos_count = len(positions)

    return positions[seconds % pos_count]


def calculate_safety_factor(positions, map_size):
    mid_x, mid_y = map_size[0] // 2, map_size[1] // 2

    """
    q1|q2
    -----
    q3|q4
    """

    quad1, quad2, quad3, quad4 = 0, 0, 0, 0

    for pos in positions:
        x, y = pos
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x:
            if y < mid_y:
                quad1 += 1
            else:
                quad3 += 1
        else:
            if y < mid_y:
                quad2 += 1
            else:
                quad4 += 1

    return quad1 * quad2 * quad3 * quad4


def part1(filepath, map_size):
    robots = parse_input(filepath)
    seconds = 100

    final_positions = []

    for robot in robots:
        positions = calculate_positions(robot, map_size)
        final_pos = pos_after_seconds(positions, seconds)
        final_positions.append(final_pos)

    return calculate_safety_factor(final_positions, map_size)
