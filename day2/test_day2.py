import day2
import pytest
import numpy as np


def test_part1():
    assert day2.part1("day2/input_example.txt") == 2
    assert day2.part1("day2/input.txt") == 516


def test_part2():
    assert day2.part2("day2/input_example.txt") == 0


def test_report_diff():
    expected = np.array([2, 4, 3])
    result = day2.report_diff([1, 3, 7, 10])
    assert np.array_equal(result, expected), f"Expected {expected}"


def test_report_is_safe():
    assert day2.report_is_safe([7, 6, 4, 2, 1]) == True
    assert day2.report_is_safe([1, 2, 7, 8, 9]) == False
    assert day2.report_is_safe([9, 7, 6, 2, 1]) == False
    assert day2.report_is_safe([1, 3, 2, 4, 5]) == False
    assert day2.report_is_safe([8, 6, 4, 4, 1]) == False
    assert day2.report_is_safe([1, 3, 6, 7, 9]) == True

    # dampen
    assert day2.report_is_safe([7, 6, 4, 2, 1], True) == True
    assert day2.report_is_safe([1, 2, 7, 8, 9], True) == False
    assert day2.report_is_safe([9, 7, 6, 2, 1], True) == False
    assert day2.report_is_safe([1, 3, 2, 4, 5], True) == True
    assert day2.report_is_safe([8, 6, 4, 4, 1], True) == True
    assert day2.report_is_safe([1, 3, 6, 7, 9], True) == True
