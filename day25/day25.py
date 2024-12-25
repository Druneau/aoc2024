from tools.file import read_file_as_string
from itertools import product


def parse_blocks(input_data):
    blocks = input_data.strip().split("\n\n")
    locks = []
    keys = []

    for block in blocks:
        lines = block.splitlines()

        # start negative to remove line of #'s
        # that defines if it's a lock or key
        pin_heights = [-1] * 5

        for line in lines:
            for i, char in enumerate(line):
                if char == "#":
                    pin_heights[i] += 1

        is_lock = lines[0][0] == "#"

        if is_lock:
            locks.append(pin_heights)
        else:
            keys.append(pin_heights)

    return locks, keys


def part1(filepath):
    blocks = read_file_as_string(filepath)

    locks, keys = parse_blocks(blocks)

    return sum(
        all(a + b < 6 for a, b in zip(lock, key)) for lock, key in product(locks, keys)
    )
