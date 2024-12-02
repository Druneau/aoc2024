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
