import day8


def test_antenna_pairs():
    assert day8.antenna_pairs([(1, 1), (2, 2), (3, 3)]) == [
        ((1, 1), (2, 2)),
        ((1, 1), (3, 3)),
        ((2, 2), (3, 3)),
    ]


def test_antinodes():
    assert day8.antinodes(((1, 1), (2, 2)), map_size=(3, 3)) == [(0, 0)]
    assert day8.antinodes(((2, 2), (1, 1)), map_size=(3, 3)) == [(0, 0)]
    assert day8.antinodes(((1, 10), (2, 20)), map_size=(3, 30)) == [(0, 0)]
    assert day8.antinodes(((10, 1), (20, 2)), map_size=(30, 3)) == [(0, 0)]


def test_in_bounds():
    assert day8.in_map((3, 3), (0, 0))
    assert day8.in_map((3, 3), (2, 2))
    assert not day8.in_map((3, 3), (-1, 0))
    assert not day8.in_map((3, 3), (0, -1))
    assert not day8.in_map((3, 3), (-100, 0))


def test_part1():
    assert day8.part1("day8/input_example.txt") == 14
    assert day8.part1("day8/input.txt") == 323


def test_part2():
    assert day8.part2("day8/input_example.txt") == 34
    assert day8.part2("day8/input.txt") == 1077
