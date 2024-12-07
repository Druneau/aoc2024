from tools.file import read_file_as_string


def parse_calibrations(lines):
    return [
        (int(key), list(map(int, values.split())))
        for key, values in (line.split(":") for line in lines.strip().split("\n"))
    ]


def evaluate_equation(answer, numbers, concat=False):
    tree = build_tree(
        numbers[0], numbers, len(numbers) - 1, len(numbers), concat, answer, [False]
    )
    # print(f"a:{answer}")
    # pretty_print_tree(tree)
    return check_leaf_nodes(tree, answer)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None


def check_leaf_nodes(node, value):
    if node is None:
        return False

    if node.left is None and node.middle is None and node.right is None:
        # print(f"a:{value} v:{node.value}")
        return node.value == value

    return (
        check_leaf_nodes(node.left, value)
        or check_leaf_nodes(node.middle, value)
        or check_leaf_nodes(node.right, value)
    )


def build_tree(value, values, current_depth, total_depth, concat, answer, found_flag):

    if found_flag[0]:
        return None

    if current_depth == 0:
        if value == answer:
            found_flag[0] = True
        return Node(value)

    root = Node(value)

    child_value = values[total_depth - current_depth]

    root.left = build_tree(
        value + child_value,
        values,
        current_depth - 1,
        total_depth,
        concat,
        answer,
        found_flag,
    )
    if concat:
        root.middle = build_tree(
            int(str(value) + str(child_value)),
            values,
            current_depth - 1,
            total_depth,
            concat,
            answer,
            found_flag,
        )
    root.right = build_tree(
        value * child_value,
        values,
        current_depth - 1,
        total_depth,
        concat,
        answer,
        found_flag,
    )
    return root


def pretty_print_tree(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("├── " if is_left else "└── ") + str(node.value))
        if node.left or node.middle or node.right:  # Print children only if they exist
            pretty_print_tree(node.left, prefix + ("│   " if is_left else "    "), True)
            pretty_print_tree(
                node.middle, prefix + ("│   " if is_left else "    "), False
            )
            pretty_print_tree(
                node.right, prefix + ("│   " if is_left else "    "), False
            )


def part1(filepath):
    data = read_file_as_string(filepath)
    calibrations = parse_calibrations(data)

    sum_valid_calibrations = 0
    count_valid = 0

    for answer, numbers in calibrations:
        if evaluate_equation(answer, numbers):
            sum_valid_calibrations += answer
            count_valid += 1

    return sum_valid_calibrations


def part2(filepath):
    data = read_file_as_string(filepath)
    calibrations = parse_calibrations(data)

    sum_valid_calibrations = 0
    count_valid = 0

    for answer, numbers in calibrations:
        if evaluate_equation(answer, numbers, concat=True):
            sum_valid_calibrations += answer
            count_valid += 1

    return sum_valid_calibrations
