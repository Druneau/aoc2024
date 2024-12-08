from itertools import combinations
from tools.file import read_file_as_dict, read_file_grid_size


def antenna_pairs(antennas):
    return list(combinations(antennas, 2))


def in_map(map_size, location):
    x, y = location
    max_x, max_y = map_size
    return 0 <= x < max_x and 0 <= y < max_y


def calculate_harmonic_range(dx, dy, map_size, harmonics):
    if not harmonics:
        return range(1, 2)

    width, height = map_size
    max_harmonic_order = max(width // dx, height // dy)
    return range(0, max_harmonic_order + 1)


def antinodes(antenna_pair, map_size, harmonics=False):
    (x1, y1), (x2, y2) = antenna_pair
    dx, dy = x2 - x1, y2 - y1

    harmonic_range = calculate_harmonic_range(dx, dy, map_size, harmonics)

    antinodes = []
    for harmonic_order in harmonic_range:
        for anchor, multiplier in [((x1, y1), -1), ((x2, y2), 1)]:
            x, y = anchor
            antinode = (
                x + dx * harmonic_order * multiplier,
                y + dy * harmonic_order * multiplier,
            )
            if in_map(map_size, antinode):
                antinodes.append(antinode)

    return antinodes


def calculate_antinodes(filepath, harmonics):
    antennas = read_file_as_dict(filepath, ignore_char=".")
    map_size = read_file_grid_size(filepath)

    valid_antinodes = set()
    for _, locations in antennas.items():
        for pair in antenna_pairs(locations):
            valid_antinodes.update(antinodes(pair, map_size, harmonics=harmonics))

    return len(valid_antinodes)


def part1(filepath):
    return calculate_antinodes(filepath, harmonics=False)


def part2(filepath):
    return calculate_antinodes(filepath, harmonics=True)
