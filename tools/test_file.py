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
