from collections import deque
from tools.file import read_file_as_string


def to_blocks(disk_map: list[int]) -> list[int | str]:
    blocks = []
    file_count = 0

    for index, block_count in enumerate(disk_map):
        block_count = int(block_count)
        if index % 2 == 0:
            blocks.extend([file_count] * block_count)
            file_count += 1
        else:
            blocks.extend(["."] * block_count)

    return blocks


def compact(blocks):
    compacted_blocks = []
    free_space_count = 0

    blocks = deque(blocks)

    while blocks:
        left_block = blocks.popleft()

        if left_block == ".":
            free_space_count += 1
            while blocks and blocks[-1] == ".":
                blocks.pop()
                free_space_count += 1
                if not blocks:
                    break
            if blocks:
                compacted_blocks.append(blocks.pop())
        else:
            compacted_blocks.append(left_block)

    return compacted_blocks


def checksum(compacted_blocks: list[int]) -> int:
    return sum(index * block for index, block in enumerate(compacted_blocks))


def part1(filepath):
    disk_map = read_file_as_string(filepath)
    blocks = to_blocks(disk_map)
    compacted_blocks = compact(blocks)
    return checksum(compacted_blocks)
