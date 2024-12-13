import day13


def test_solve_a_b():
    assert day13.solve_a_b(94, 34, 22, 67, 8400, 5400) == (80, 40)
    assert day13.solve_a_b(17, 86, 84, 37, 7870, 6450) == (38, 86)


def test_part1():
    assert day13.part1("day13/input_example.txt") == 480
    assert day13.part1("day13/input.txt") == 29877


def test_part2():
    assert day13.part2("day13/input.txt") == 99423413811305
