from tools.file import read_file_as_lists


def blink(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid_str = len(stone_str) // 2
        return [int(stone_str[:mid_str]), int(stone_str[mid_str:])]

    return [stone * 2024]


def recursive_blink_count(stone, blinks_left):
    if blinks_left == 0:
        return 1

    count = 0
    new_stones = blink(stone)
    for new_stone in new_stones:
        count += recursive_blink_count(new_stone, blinks_left - 1)

    return count


def blink_as_dict(stones: dict) -> dict:
    stones_tally = {}

    for value, count in stones.items():
        new_stones = blink(value)

        for new_stone in new_stones:
            stones_tally[new_stone] = stones_tally.get(new_stone, 0) + count
    return stones_tally


def part1(filepath):
    stones = read_file_as_lists(filepath)[0]
    total_count = 0
    for stone in stones:
        total_count += recursive_blink_count(stone, blinks_left=25)

    return total_count


def part2(filepath, blinks):
    stones = read_file_as_lists(filepath)[0]

    stones_tally = {}
    for stone in stones:
        stones_tally[stone] = 1

    for _ in range(blinks):
        stones_tally = blink_as_dict(stones_tally)

    return sum(stones_tally.values())
