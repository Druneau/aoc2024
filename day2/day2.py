import numpy as np
from tools.file import read_file_as_lists


def report_diff(report):
    arr = np.array(report)
    diff = np.diff(arr)
    return diff


def report_is_safe(report, dampen=False):
    diff = report_diff(report)
    positive = np.all(diff > 0)
    negative = np.all(diff < 0)
    min = np.min(diff)
    max = np.max(diff)

    if positive:
        if min > 0 and max < 4:
            return True
    elif negative:
        if max < 0 and min > -4:
            return True
    elif dampen:
        print(f"{diff}")
        print(f"p:{positive}, n:{negative}, min:{min}, max{max}")
        zero_count = np.sum(diff == 0)
        negative_count = np.sum(diff < 0)
        positive_count = np.sum(diff > 0)
        print(f"z:{zero_count}, n:{negative_count}, p:{positive_count}")

    return False


def part1(filename):
    reports = read_file_as_lists(filename)

    safe_count = 0

    for r in reports:
        if report_is_safe(r):
            safe_count += 1

    return safe_count


def part2(filename):
    reports = read_file_as_lists(filename)

    safe_count = 0

    for r in reports:
        if report_is_safe(r, dampen=True):
            safe_count += 1
    return 0
