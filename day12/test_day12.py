from tools.file import read_file_as_chars
import day12

INPUT_EXAMPLE = read_file_as_chars("day12/input_example.txt")
INPUT_SIMPLE = read_file_as_chars("day12/input_simple.txt")
INPUT = read_file_as_chars("day12/input.txt")


def test_get_valid_touching():
    assert day12.get_valid_touching(INPUT_EXAMPLE, (0, 0)) == [(1, 0), (0, 1)]
    assert day12.get_valid_touching(INPUT_EXAMPLE, (9, 9)) == [(8, 9), (9, 8)]
    assert day12.get_valid_touching(INPUT_EXAMPLE, (6, 5)) == [(5, 5)]


def test_get_plots():
    assert day12.get_plots(INPUT_SIMPLE) == {
        "O": {
            (0, 0): [(0, 1)],
            (0, 1): [(1, 1), (0, 0), (0, 2)],
            (0, 2): [(0, 1)],
            (1, 1): [(0, 1), (2, 1)],
            (2, 0): [(2, 1)],
            (2, 1): [(1, 1), (2, 0), (2, 2)],
            (2, 2): [(2, 1)],
        },
        "X": {(1, 0): [], (1, 2): []},
    }


def test_get_regions():
    assert day12.get_regions(INPUT_SIMPLE) == {
        "O.0": {
            (0, 0): [(0, 1)],
            (0, 1): [(1, 1), (0, 0), (0, 2)],
            (0, 2): [(0, 1)],
            (1, 1): [(0, 1), (2, 1)],
            (2, 1): [(1, 1), (2, 0), (2, 2)],
            (2, 2): [(2, 1)],
            (2, 0): [(2, 1)],
        },
        "X.0": {(1, 0): []},
        "X.1": {(1, 2): []},
    }


def test_part1():
    assert day12.part1("day12/input_example.txt") == 1930
    assert day12.part1("day12/input.txt") == 1370100


def test_get_fence():
    assert day12.get_fence_map({(1, 1): []}, "O") == [
        [".", "*", "."],
        ["*", "O", "*"],
        [".", "*", "."],
    ]


def test_perimeter_scan():
    fence_map = day12.get_fence_map({(1, 1): []}, "O")
    assert day12.perimeter_scan(fence_map) == 4


def test_part2():
    assert day12.part2("day12/input_example.txt") == 1206
    # assert day12.part2("day12/input.txt") > 817337
