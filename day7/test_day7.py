import day7

input_example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def test_parse_calibrations():
    assert day7.parse_calibrations("190: 10 19") == [(190, [10, 19])]
    assert day7.parse_calibrations(input_example) == [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]


def test_evaluate_equation():
    assert day7.evaluate_equation(190, [10, 19])
    assert day7.evaluate_equation(3267, [81, 40, 27])
    assert not day7.evaluate_equation(83, [17, 5])
    assert not day7.evaluate_equation(192, [17, 8, 14])


def test_single_value():
    assert day7.evaluate_equation(5, [5])
    assert not day7.evaluate_equation(10, [5])


def test_deep_tree():
    assert day7.evaluate_equation(10, 10 * [1])
    assert day7.evaluate_equation(100, 8 * [2])


def test_complex_cases():
    assert not day7.evaluate_equation(4068635, [3, 3, 43, 703, 22, 632])
    assert not day7.evaluate_equation(48771072, [4, 114, 2, 1, 6, 9, 1, 2, 441, 1, 8])


def test_part1():
    assert day7.part1("day7/input_example.txt") == 3749
    assert day7.part1("day7/input.txt") == 6392012777720


def test_part2():
    assert day7.part2("day7/input_example.txt") == 11387
    assert day7.part2("day7/input.txt") == 61561126043536
