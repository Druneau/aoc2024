import day11


def test_blink():
    assert day11.blink(stone=0) == [1]
    assert day11.blink(1) == [2024]
    assert day11.blink(11) == [1, 1]
    assert day11.blink(10) == [1, 0]
    assert day11.blink(1000) == [10, 0]
    assert day11.blink(99) == [9, 9]
    assert day11.blink(999) == [999 * 2024]


def test_part1():
    assert day11.part1("day11/input_example.txt") == 55312
    assert day11.part1("day11/input.txt") == 204022


def test_part2():
    assert day11.part2("day11/input_example.txt", 6) == 22
    assert day11.part2("day11/input_example.txt", 25) == 55312
    assert day11.part2("day11/input.txt", 25) == 204022
    assert day11.part2("day11/input.txt", 75) == 241651071960597
