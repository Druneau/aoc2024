def distance(leftID, rightID):
    return abs(leftID - rightID)


def read_file_as_tuples(filename):
    result = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    result.append((int(parts[0]), int(parts[1])))
                else:
                    raise ValueError(f"Invalid line format: {line.strip()}")
    except Exception as e:
        print(f"An error occured: {e}")
    return result


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
