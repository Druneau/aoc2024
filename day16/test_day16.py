import day16


def test_part1():
    assert day16.part1("day16/input_example.txt") == 7036
    assert day16.part1("day16/input_example_2.txt") == 11048
    assert day16.part1("day16/input.txt") == 134588


def test_part2():
    assert day16.part2("day16/input_example.txt") == 45
    assert day16.part2("day16/input_example_2.txt") == 64
    # assert day16.part2("day16/input.txt") == 0
