import day20


def test_part1():
    assert day20.part1("day20/input_example.txt", 0) == 44
    assert day20.part1("day20/input.txt", 100) == 1445


def test_part2():
    assert day20.part2("day20/input_example.txt", 50, cheat_picoseconds_limit=20) == 285
    assert day20.part2("day20/input.txt", 100, cheat_picoseconds_limit=20) == 1008040
