import day1


def test_distance():
    assert day1.distance(1, 3) == 2
    assert day1.distance(2, 3) == 1
    assert day1.distance(3, 3) == 0
    assert day1.distance(3, 4) == 1
    assert day1.distance(4, 9) == 5


def test_sum_distance():
    assert day1.sum_distance_tuples([(3, 1), (4, 6)]) == (2 + 2)
    example = day1.read_file_as_tuples("input_example.txt")
    sorted_example = day1.sort_tuple_halves(example)
    assert day1.sum_distance_tuples(sorted_example) == 11


def test_read_file_as_tuples():
    assert day1.read_file_as_tuples("input_example.txt") == [
        (3, 4),
        (4, 3),
        (2, 5),
        (1, 3),
        (3, 9),
        (3, 3),
    ]


def test_sort_tuple_halves():
    assert day1.sort_tuple_halves([(4, 6), (3, 1)]) == [(3, 1), (4, 6)]


def test_part1():
    assert day1.part1(input="input_example.txt") == 11
    assert day1.part1(input="input.txt") == 3246517


def test_part2():
    assert day1.part2(input="input_example.txt") == 31
    assert day1.part2(input="input.txt") == 29379307


def test_calc_similarity():
    assert day1.calc_similarity(3, [3, 1, 2]) == 3
    assert day1.calc_similarity(4, [1, 2, 3, 6]) == 0
    assert day1.calc_similarity(1, [0]) == 0


def test_get_count():
    assert day1.get_count(3, [1, 2, 3, 4, 5, 6]) == 1
    assert day1.get_count(7, [1, 2, 3, 4, 5, 6]) == 0
