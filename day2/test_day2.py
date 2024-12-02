import pytest
import day2
import numpy as np

INPUT_EXAMPLE = "day2/input_example.txt"
INPUT = "day2/input.txt"


def test_part1():
    assert day2.part1(INPUT_EXAMPLE) == 2
    assert day2.part1(INPUT) == 516


def test_part2():
    assert day2.part2(INPUT_EXAMPLE) == 4
    assert day2.part2(INPUT) == 561


@pytest.mark.parametrize(
    "report, expected",
    [
        ([1, 3, 7, 10], [2, 4, 3]),
    ],
)
def test_report_diff(report, expected):
    result = day2.report_diff(report)
    assert np.array_equal(
        result, np.array(expected)
    ), f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "report, expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_report_is_safe_part1(report, expected):
    assert day2.report_is_safe(report) == expected


@pytest.mark.parametrize(
    "report, allow_dampen, expected",
    [
        ([7, 6, 4, 2, 1], False, True),
        ([1, 2, 7, 8, 9], False, False),
        ([9, 7, 6, 2, 1], False, False),
        ([1, 3, 2, 4, 5], False, False),
        ([8, 6, 4, 4, 1], False, False),
        ([1, 3, 6, 7, 9], False, True),
        ([7, 6, 4, 2, 1], True, True),
        ([1, 2, 7, 8, 9], True, False),
        ([9, 7, 6, 2, 1], True, False),
        ([8, 6, 4, 4, 1], True, True),
        ([1, 3, 2, 4, 5], True, True),
        ([1, 3, 6, 7, 9], True, True),
    ],
)
def test_report_is_safe_part2(report, allow_dampen, expected):
    assert day2.report_is_safe(report, allow_dampen) == expected


def test_generate_dampened_lists():
    assert day2.generate_dampened_lists([1, 2, 3, 4]) == [
        [2, 3, 4],
        [1, 3, 4],
        [1, 2, 4],
        [1, 2, 3],
    ]
