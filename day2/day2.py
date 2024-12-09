import numpy as np
from tools.file import read_file_as_lists


def report_diff(report):
    arr = np.asarray(report)
    return np.diff(arr)


def generate_dampened_lists(report):
    return [report[:i] + report[i + 1 :] for i in range(len(report))]


def report_is_safe(report, allow_dampen=False):
    diff = report_diff(report)

    min = np.min(diff)
    max = np.max(diff)

    if np.all(diff > 0):
        if min > 0 and max < 4:
            return True
    elif np.all(diff < 0):
        if max < 0 and min > -4:
            return True

    if allow_dampen:
        return any(
            report_is_safe(dampened_report, allow_dampen=False)
            for dampened_report in generate_dampened_lists(report)
        )

    return False


def analyze_data(filepath, allow_dampen=False):
    reports = read_file_as_lists(filepath)
    return sum(1 for r in reports if report_is_safe(r, allow_dampen))


def part1(filepath):
    return analyze_data(filepath)


def part2(filepath):
    return analyze_data(filepath, allow_dampen=True)
