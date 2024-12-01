from tools.file import read_file_as_tuples


def distance(leftID, rightID):
    return abs(leftID - rightID)


def sort_tuple_halves(tuples_array):
    if not tuples_array:
        return []

    left_half = [t[0] for t in tuples_array]
    right_half = [t[1] for t in tuples_array]

    left_half.sort()
    right_half.sort()

    sorted_tuples = list(zip(left_half, right_half))

    return sorted_tuples


def sum_distance_tuples(sorted_tuples):
    sum = 0
    for t in sorted_tuples:
        sum += distance(t[0], t[1])
    return sum


def part1(input="./day1/input.txt"):
    tuples = read_file_as_tuples(input)
    sorted_tuples = sort_tuple_halves(tuples)
    return sum_distance_tuples(sorted_tuples)


def part2(input="./day1/input.txt"):

    tuples = read_file_as_tuples(input)
    similarity_sum = 0

    left_half = [t[0] for t in tuples]

    right_half = [t[1] for t in tuples]

    for id in left_half:
        similarity_sum += calc_similarity(id, right_half)

    return similarity_sum


def calc_similarity(id, list):
    count = get_count(id, list)
    return id * count


def get_count(id, list):
    return list.count(id)
