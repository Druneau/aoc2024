from tools.file import read_file_as_tuples
import day1


def test_sum_distance():
    assert day1.sum_distance_tuples([(3, 1), (4, 6)]) == (2 + 2)
    example = read_file_as_tuples("day1/input_example.txt")
    sorted_example = day1.sort_tuple_halves(example)
    assert day1.sum_distance_tuples(sorted_example) == 11


def test_sort_tuple_halves():
    assert day1.sort_tuple_halves([(4, 6), (3, 1)]) == [(3, 1), (4, 6)]


def test_part1():
    assert day1.part1(input="day1/input_example.txt") == 11
    assert day1.part1(input="day1/input.txt") == 3246517


def test_part2():
    assert day1.part2(input="day1/input_example.txt") == 31
    assert day1.part2(input="day1/input.txt") == 29379307


def test_calc_similarity():
    assert day1.calc_similarity(3, [3, 1, 2]) == 3
    assert day1.calc_similarity(4, [1, 2, 3, 6]) == 0
    assert day1.calc_similarity(1, [0]) == 0
