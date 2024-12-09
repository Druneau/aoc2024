from collections import deque
from tools.file import read_file_as_string


def to_blocks(disk_map):
    blocks = []

    file_count = 0

    for id, block in enumerate(disk_map):
        block = int(block)
        if id % 2 == 0:
            blocks.extend(block * [file_count])
            file_count += 1
        else:
            blocks.extend(block * ["."])

    return blocks


def compact(blocks):
    compacted_blocks = []
    free_space_count = 0

    blocks = deque(blocks)

    while len(blocks) > 0:
        left_block = blocks.popleft()

        if left_block == ".":
            free_space_count += 1
            if not blocks:
                break
            while blocks[-1] == ".":
                blocks.pop()
                free_space_count += 1
                if not blocks:
                    break
            if blocks:
                compacted_blocks.append(blocks.pop())
        else:
            compacted_blocks.append(left_block)

    # compacted_blocks.extend((free_space_count) * ".")

    return compacted_blocks


def checksum(compacted_blocks):
    checksum = 0

    for index, id in enumerate(compacted_blocks):
        checksum += index * id

    return checksum


def part1(filepath):
    disk_map = read_file_as_string(filepath)
    blocks = to_blocks(disk_map)
    compacted_blocks = compact(blocks)
    return checksum(compacted_blocks)
