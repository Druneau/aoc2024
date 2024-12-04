from tools.file import read_file_as_strings

PART1_MATCHES = ["XMAS", "SAMX"]
PART2_MATCHES = ["MAS", "SAM"]


def word_search(line, substrings):
    matches = sum(line.count(substring) for substring in substrings)
    return matches


def get_verticals(lines):
    return ["".join(chars) for chars in zip(*lines)]


def get_diagonals(lines):
    num_rows = len(lines)
    num_cols = len(lines[0])
    diagonals = []

    # Top-left to bottom-right diagonals
    for col_start in range(num_cols):
        diagonal = [
            lines[row][col_start + row]
            for row in range(min(num_rows, num_cols - col_start))
        ]
        diagonals.append("".join(diagonal))
    for row_start in range(1, num_rows):
        diagonal = [
            lines[row_start + col][col]
            for col in range(min(num_cols, num_rows - row_start))
        ]
        diagonals.append("".join(diagonal))

    # Top-right to bottom-left diagonals
    for col_start in range(num_cols):
        diagonal = [
            lines[row][col_start - row] for row in range(min(num_rows, col_start + 1))
        ]
        diagonals.append("".join(diagonal))
    for row_start in range(1, num_rows):
        diagonal = [
            lines[row_start + col][num_cols - col - 1]
            for col in range(min(num_cols, num_rows - row_start))
        ]
        diagonals.append("".join(diagonal))

    return diagonals


def part1(filename):
    lines = read_file_as_strings(filename)
    lines = lines + get_verticals(lines) + get_diagonals(lines)
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
        diagonals = get_diagonals(block)
        search = word_search(diagonals, PART2_MATCHES)
        if search == 2:
            total_cross_mas += 1

    return total_cross_mas
