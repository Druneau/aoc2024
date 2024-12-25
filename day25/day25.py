from tools.file import read_file_as_string

from itertools import product


def parse_blocks(input_data):
    blocks = input_data.strip().split("\n\n")
    locks = []
    keys = []

    for block in blocks:
        lines = block.splitlines()
        cols = len(lines[0])

        # start negative to remove line of #'s that defines if it's a lock or key
        counts = [-1] * cols

        for line in lines:
            for i, char in enumerate(line):
                if char == "#":
                    counts[i] += 1

        if all(char == "#" for char in lines[0]):
            locks.append(counts)
        if all(char == "#" for char in lines[-1]):
            keys.append(counts)

    return locks, keys


def part1(filepath):
    blocks = read_file_as_string(filepath)

    locks, keys = parse_blocks(blocks)

    return sum(
        all(a + b < 6 for a, b in zip(lock, key)) for lock, key in product(locks, keys)
    )
