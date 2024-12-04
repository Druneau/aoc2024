import day4
from tools.file import read_file_as_strings

PATH_INPUT_SIMPLE = "day4/input_simple.txt"
PATH_INPUT_EXAMPLE = "day4/input_example.txt"
PATH_INPUT = "day4/input.txt"

INPUT_SIMPLE = read_file_as_strings(PATH_INPUT_SIMPLE)


def test_word_search():
    assert day4.word_search("XMAS", day4.PART1_MATCHES) == 1
    assert day4.word_search("SAMXMAS", day4.PART1_MATCHES) == 2


def test_decompose():
    assert day4.get_verticals(INPUT_SIMPLE) == [
        "XXXX",
        "MMMM",
        "AAAA",
        "SSSS",
    ]


def test_get_diagonals():
    assert day4.get_diagonals_skew(INPUT_SIMPLE) == [
        "X",
        "XM",
        "XMA",
        "XMAS",
        "MAS",
        "AS",
        "S",
        "X",
        "MX",
        "AMX",
        "SAMX",
        "SAM",
        "SA",
        "S",
    ]


def test_blocks():
    assert day4.get_blocks(INPUT_SIMPLE) == [
        ["XMA", "XMA", "XMA"],
        ["MAS", "MAS", "MAS"],
        ["XMA", "XMA", "XMA"],
        ["MAS", "MAS", "MAS"],
    ]


def test_part1():
    assert day4.part1(PATH_INPUT_EXAMPLE) == 18
    assert day4.part1(PATH_INPUT) == 2557


def test_part2():
    assert day4.part2(PATH_INPUT_SIMPLE) == 2
    assert day4.part2(PATH_INPUT_EXAMPLE) == 9
    assert day4.part2(PATH_INPUT) == 1854


def test_skew():
    assert day4.skew(["X", "M"], True, 2, 4) == ["", "", "X", "M"]
    assert day4.skew(["X", "M"], True, 1, 4) == ["", "X", "M", ""]
    assert day4.skew(["X", "M"], True, 0, 4) == ["X", "M", "", ""]
    assert day4.skew(["X", "M"], False, 0, 4) == ["", "", "X", "M"]
    assert day4.skew(["X", "M"], False, 1, 4) == ["", "X", "M", ""]
    assert day4.skew(["X", "M"], False, 2, 4) == ["X", "M", "", ""]
