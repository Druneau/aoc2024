import day21

SIMPLE_KEYS = {
    "A": (0, 0),
    "B": (1, 1),
    "C": (2, 2),
}


def test_calc_delta():
    assert day21.calc_delta((0, 0), (1, 1)) == (1, 1)
    assert day21.calc_delta((1, 1), (0, 0)) == (-1, -1)
    assert day21.calc_delta((0, 1), (1, 1)) == (1, 0)
    assert day21.calc_delta((0, 1), (0, 1)) == (0, 0)


def test_build_deltas():
    assert day21.build_deltas(SIMPLE_KEYS) == {
        ("A", "B"): (1, 1),
        ("A", "C"): (2, 2),
        ("B", "A"): (-1, -1),
        ("B", "C"): (1, 1),
        ("C", "A"): (-2, -2),
        ("C", "B"): (-1, -1),
    }


def test_transform():
    assert day21.transform("029A") == list("<A^A^^>AvvvA")


def test_finger_to_robot_to_robot_to_robot():
    assert len(day21.finger_to_robot_to_robot_to_robot("029A")) == 68


def test_complexity():
    assert day21.complexity("029A") == 68 * 29
    assert day21.complexity("980A") == 60 * 980
    assert day21.complexity("179A") == 68 * 179
    assert day21.complexity("456A") == 64 * 456
    assert day21.complexity("379A") == 64 * 379


def test_part1():
    assert day21.part1("day21/input_example.txt") == 126384
