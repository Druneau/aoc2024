import day4
from tools.file import read_file_as_strings

INPUT_SIMPLE = read_file_as_strings("day4/input_simple.txt")


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
    assert day4.get_diagonals(read_file_as_strings("day4/input_simple.txt")) == [
        "XMAS",
        "MAS",
        "AS",
        "S",
        "XMA",
        "XM",
        "X",
        "X",
        "MX",
        "AMX",
        "SAMX",
        "SAM",
        "SA",
        "S",
    ]


def test_part1():
    assert day4.part1("day4/input_example.txt") == 18
    assert day4.part1("day4/input.txt") == 2557


def test_blocks():
    assert day4.get_blocks(INPUT_SIMPLE) == [
        ["XMA", "XMA", "XMA"],
        ["MAS", "MAS", "MAS"],
        ["XMA", "XMA", "XMA"],
        ["MAS", "MAS", "MAS"],
    ]


def test_part2():
    assert day4.part2("day4/input_simple.txt") == 2
    assert day4.part2("day4/input_example.txt") == 9
    assert day4.part2("day4/input.txt") == 1854
