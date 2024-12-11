from tools.file import read_file_as_lists


def blink(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid_str = len(stone_str) // 2
        return [int(stone_str[:mid_str]), int(stone_str[mid_str:])]

    return [stone * 2024]


def blink_all(stones, blink_count=1):
    for i in range(blink_count):
        if i == 0:
            after_blink = []
        else:
            stones = after_blink
            after_blink = []

        for stone in stones:
            after_blink.extend(blink(stone))

    return after_blink


def part1(filepath):
    stones = read_file_as_lists(filepath)[0]
    print(f"stones:{stones}")
    return len(blink_all(stones, 25))
