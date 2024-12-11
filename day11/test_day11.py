import day11


def test_blink():
    assert day11.blink(stone=0) == [1]
    assert day11.blink(1) == [2024]
    assert day11.blink(11) == [1, 1]
    assert day11.blink(10) == [1, 0]
    assert day11.blink(1000) == [10, 0]
    assert day11.blink(99) == [9, 9]
    assert day11.blink(999) == [999 * 2024]


def test_blink_all():
    assert day11.blink_all([125, 17]) == [253000, 1, 7]
    assert day11.blink_all([125, 17], blink_count=2) == [253, 0, 2024, 14168]
    assert day11.blink_all([125, 17], blink_count=6) == [
        2097446912,
        14168,
        4048,
        2,
        0,
        2,
        4,
        40,
        48,
        2024,
        40,
        48,
        80,
        96,
        2,
        8,
        6,
        7,
        6,
        0,
        3,
        2,
    ]


def test_part1():
    assert day11.part1("day11/input_example.txt") == 55312
    assert day11.part1("day11/input.txt") == 204022
