from itertools import combinations

from numpy import empty

from tools.file import read_file_as_dict, read_file_grid_size


def antenna_pairs(antennas):
    return list(combinations(antennas, 2))


def in_map(map_size, location):
    x, y = location
    max_x, max_y = map_size
    return -1 < x < max_x and -1 < y < max_y


def antinodes(antenna_pair, map_size):

    (x1, y1), (x2, y2) = antenna_pair

    dx = x2 - x1
    dy = y2 - y1

    antinodes = []

    an1 = (x1 - dx, y1 - dy)
    if in_map(map_size, an1):
        antinodes.append(an1)

    an2 = (x2 + dx, y2 + dy)
    if in_map(map_size, an2):
        antinodes.append(an2)

    return antinodes


def part1(filepath):

    antennas = read_file_as_dict(filepath, ignore_char=".")
    map_size = read_file_grid_size(filepath)

    valid_antinodes = []
    for _, (frequency, locations) in enumerate(antennas.items()):
        pairs = antenna_pairs(locations)

        for pair in pairs:
            nodes = antinodes(pair, map_size)
            valid_antinodes += nodes
    return len(set(valid_antinodes))
