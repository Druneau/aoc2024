from tools.file import read_file_as_strings

PART1_MATCHES = ["XMAS", "SAMX"]
PART2_MATCHES = ["MAS", "SAM"]


def word_search(line, substrings):
    matches = sum(line.count(substring) for substring in substrings)
    return matches


def get_verticals(lines):
    return ["".join(chars) for chars in zip(*lines)]


def get_diagonals_skew(lines):
    skewed_right = []
    skewed_left = []
    columns = len(lines[0])
    final_size = columns * 2 - 1
    shift_count = columns - 1

    for line in lines:
        line = list(line)
        skewed_right.append(skew(line, True, shift_count, final_size))
        skewed_left.append(skew(line, False, shift_count, final_size))
        shift_count -= 1

    return get_verticals(skewed_right) + get_verticals(skewed_left)


def skew(line, shift_right, shift_count, final_size):
    pad_count = final_size - len(line) - shift_count

    if shift_right:
        left_padding = shift_count
        right_padding = pad_count
    else:
        left_padding = pad_count
        right_padding = shift_count

    return [""] * left_padding + line + [""] * right_padding


def part1(filename):
    lines = read_file_as_strings(filename)
    lines = lines + get_verticals(lines) + get_diagonals_skew(lines)
    return sum(word_search(line, PART1_MATCHES) for line in lines)


def get_blocks(lines):
    blocks = []
    num_rows = len(lines)
    num_cols = len(lines[0]) if lines else 0

    for row_start in range(num_rows - 2):
        for col_start in range(num_cols - 2):
            blocks.append(
                [
                    lines[row][col_start : col_start + 3]
                    for row in range(row_start, row_start + 3)
                ]
            )

    return blocks


def part2(filename):
    lines = read_file_as_strings(filename)

    blocks = get_blocks(lines)

    total_cross_mas = 0
    for block in blocks:
        diagonals = get_diagonals_skew(block)
        search = word_search(diagonals, PART2_MATCHES)
        if search == 2:
            total_cross_mas += 1

    return total_cross_mas
