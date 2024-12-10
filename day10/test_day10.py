import day10


def test_part1():
    assert day10.part1("day10/input_example.txt") == 36
    assert day10.part1("day10/input.txt") == 782


def test_part2():
    assert day10.part2("day10/input_rating_simple.txt") == 3
    assert day10.part2("day10/input_rating_complex.txt") == 227
    assert day10.part2("day10/input_example.txt") == 81
    assert day10.part2("day10/input.txt") == 1694
