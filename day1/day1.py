from tools.file import read_file_as_tuples


def sort_tuple_halves(tuples_array):

    left_half = sorted(t[0] for t in tuples_array)
    right_half = sorted(t[1] for t in tuples_array)

    return list(zip(left_half, right_half))


def sum_distance_tuples(sorted_tuples):
    return sum(abs(t[0] - t[1]) for t in sorted_tuples)


def part1(input):
    tuples = read_file_as_tuples(input)
    return sum_distance_tuples(sort_tuple_halves(tuples))


def part2(input):
    tuples = read_file_as_tuples(input)
    left_half, right_half = zip(*tuples)

    return sum(calc_similarity(left_id, right_half) for left_id in left_half)


def calc_similarity(id, elements):
    return id * elements.count(id)
