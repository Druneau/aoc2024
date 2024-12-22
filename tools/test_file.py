import tools.file


def test_read_file_as_tuples():
    assert tools.file.read_file_as_tuples("day1/input_example.txt") == [
        (3, 4),
        (4, 3),
        (2, 5),
        (1, 3),
        (3, 9),
        (3, 3),
    ]


def test_read_file_as_lists():
    assert tools.file.read_file_as_lists("day2/input_example.txt") == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_read_file_as_strings():
    assert tools.file.read_file_as_strings("day3/input_example.txt") == [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ]


def test_read_file_as_chars():
    assert tools.file.read_file_as_chars("day4/input_simple.txt") == [
        ["X", "M", "A", "S"],
        ["X", "M", "A", "S"],
        ["X", "M", "A", "S"],
        ["X", "M", "A", "S"],
    ]


def test_read_file_as_dict():
    assert tools.file.read_file_as_dict("day8/input_example.txt", ignore_char=".") == {
        "0": [(8, 1), (5, 2), (7, 3), (4, 4)],
        "A": [(6, 5), (8, 8), (9, 9)],
    }


def test_read_file_as_ints():
    assert tools.file.read_file_as_ints("day22/input_example.txt") == [1, 10, 100, 2024]
