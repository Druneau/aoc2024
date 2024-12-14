from collections import OrderedDict
from tools.file import read_file_as_strings
import re

import os
from tools.print import print_array

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


def clear_screen():
    os.system("clear")


def print_map(locations, map_size, seconds):
    unique_locations = set(locations)
    size_x, size_y = map_size

    # we're gonna try to find straight lines with lots of robots...
    # should probably find a more direct way.. but this worked!

    max_robots_in_row = 0

    this_map = []

    for y in range(size_y):
        row = []
        robots_in_row = 0
        for x in range(size_x):
            if (x, y) in unique_locations:
                row.append("O")
                robots_in_row += 1
            else:
                row.append(".")
        max_robots_in_row = max(max_robots_in_row, robots_in_row)
        this_map.append(row)

    if max_robots_in_row == 32:
        print_array(this_map)
        print(f"{seconds} elapsed")
        input("Press enter for next map")
        clear_screen()


def part2(filepath, map_size):
    robots = parse_input(filepath)

    robot_positions = [calculate_positions(robot, map_size) for robot in robots]

    distinct_maps = zip(*robot_positions)

    for seconds, robot_map in enumerate(distinct_maps):
        print_map(robot_map, map_size, seconds)

    return 0


if __name__ == "__main__":
    part2("day14/input.txt", (101, 103))
