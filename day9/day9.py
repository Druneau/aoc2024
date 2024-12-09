from collections import deque
from tools.file import read_file_as_string
from itertools import chain
import time

FREE_SPACE_CHAR = "."


def to_blocks(disk_map: list[int]) -> list[int | str]:
    blocks = []
    file_count = 0

    for index, block_count in enumerate(disk_map):
        block_count = int(block_count)
        if index % 2 == 0:
            blocks.extend([file_count] * block_count)
            file_count += 1
        else:
            blocks.extend([FREE_SPACE_CHAR] * block_count)

    return blocks


def per_block_compact(blocks):
    compacted_blocks = []
    free_space_count = 0

    blocks = deque(blocks)

    while blocks:
        left_block = blocks.popleft()

        if left_block == FREE_SPACE_CHAR:
            free_space_count += 1
            while blocks and blocks[-1] == FREE_SPACE_CHAR:
                blocks.pop()
                free_space_count += 1
                if not blocks:
                    break
            if blocks:
                compacted_blocks.append(blocks.pop())
        else:
            compacted_blocks.append(left_block)

    return compacted_blocks


def blocks_to_files(blocks):
    files = []

    file_data = None
    file_length = 0
    file_start_index = 0

    for index, block in enumerate(blocks):
        if file_data is None:
            file_start_index = index
            file_length = 1
            file_data = block
        elif block == file_data:
            file_length += 1
        else:
            files.append((file_start_index, file_length, file_data))
            file_data = block
            file_start_index = index
            file_length = 1

    files.append((file_start_index, file_length, file_data))

    return files


def files_to_blocks(files):
    blocks = []

    for _, length, data in files:
        blocks.extend([data] * length)
    return blocks


def insert_file(file, free_space):
    file_id, length, data = file
    free_id, free_length, free_data = free_space

    if length <= free_length:
        free = [
            (free_id + length, free_length - length, free_data),
            (file_id, length, free_data),
        ]
        file = (free_id, length, data)
    else:
        free = [free_space]

    return file, free


def per_file_compact(files):
    files = sorted(files, key=lambda f: f[0], reverse=True)
    compacted_set = set()

    while files:
        file = files.pop(0)
        _, length, data = file

        if data == FREE_SPACE_CHAR:
            compacted_set.add(file)
        else:
            space = find_space(length, files)
            if space:
                files.remove(space)
                file, space_fragments = insert_file(file, space)

                space_left, space_used = space_fragments
                compacted_set.add(file)
                compacted_set.add(space_used)
                files.append(space_left)
                files.sort(key=lambda f: f[0], reverse=True)
            else:
                compacted_set.add(file)

    compacted_files = sorted(compacted_set, key=lambda f: f[0])
    blocks = files_to_blocks(compacted_files)
    return blocks


def find_space(space_length, files):
    available_spaces = [
        f for f in files if f[1] >= space_length and f[2] == FREE_SPACE_CHAR
    ]

    if available_spaces:
        return min(available_spaces, key=lambda f: f[0])
    else:
        return None


def checksum(compacted_blocks: list[int | str]) -> int:
    return sum(
        index * block
        for index, block in enumerate(compacted_blocks)
        if isinstance(block, int)
    )


def chain_functions(*functions):
    def chained(data):
        for func in functions:
            data = func(data)
        return data

    return chained


def process_disk(filepath, compact_function):
    disk_map = read_file_as_string(filepath)
    blocks = compact_function(disk_map)
    return checksum(blocks)


def part1(filepath):
    return process_disk(filepath, chain_functions(to_blocks, per_block_compact))


def part2(filepath):
    return process_disk(
        filepath, chain_functions(to_blocks, blocks_to_files, per_file_compact)
    )
