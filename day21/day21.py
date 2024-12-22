from itertools import permutations

from tools.file import read_file_as_strings

NUMERIC_KEYS = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

DIRECTION_KEYS = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

DELTA_KEYS = {
    (-1, 0): "^",
    (0, 1): ">",
    (1, 0): "v",
    (0, -1): "<",
}


def calc_delta(key_from, key_to):
    f_row, f_col = key_from
    t_row, t_col = key_to

    return (t_row - f_row, t_col - f_col)


def build_deltas(locations):
    keys = locations.keys()
    moves = list(permutations(keys, 2))

    deltas = {}
    for move in moves:
        key_from = locations[move[0]]
        key_to = locations[move[1]]
        deltas[move] = calc_delta(key_from, key_to)

    return deltas


def transform(sequence):
    is_numeric_keypad = False
    if isinstance(sequence, str):
        # we load a string from file, so must be keycode
        locations = NUMERIC_KEYS
        sequence = list(sequence)
        is_numeric_keypad = True
    else:
        locations = DIRECTION_KEYS

    sequence.insert(0, "A")
    from_to_pairs = list(zip(sequence, sequence[1:]))
    key_presses = []
    for from_key, to_key in from_to_pairs:
        from_loc = locations[from_key]
        to_loc = locations[to_key]

        # we have locations, find a delta and convert to direction key presses
        dr, dc = calc_delta(from_loc, to_loc)

        vector_row = dr / abs(dr) if dr != 0 else 0
        vector_col = dc / abs(dc) if dc != 0 else 0

        char_row = DELTA_KEYS[vector_row, 0] if vector_row != 0 else ""
        char_col = DELTA_KEYS[0, vector_col] if vector_col != 0 else ""

        dr = abs(dr)
        dc = abs(dc)
        to_press = ""
        # any risk hitting empty spot?
        if is_numeric_keypad:
            if from_key in {"7, 4, 1"}:
                to_press = dc * char_col + dr * char_row + "A"
            else:
                to_press = dr * char_row + dc * char_col + "A"
        else:
            if from_key == "<":
                to_press = dc * char_col + dr * char_row + "A"
            else:
                to_press = dr * char_row + dc * char_col + "A"

        key_presses.extend(to_press)
        # print(f"{from_key} to {to_key} = {to_press}")

    return key_presses


def finger_to_robot_to_robot_to_robot(sequence):
    robotcommand1 = transform(sequence[:])
    robotcommand2 = transform(robotcommand1[:])
    fingercommand = transform(robotcommand2[:])

    print("----")
    print("".join(fingercommand))
    print("".join(robotcommand2))
    print("".join(robotcommand1))
    print(sequence)
    print("----")

    return fingercommand


def complexity(code):
    sequence = finger_to_robot_to_robot_to_robot(code)
    sequence_length = len(sequence)
    numeric_part = int(code[:-1])
    return sequence_length * numeric_part


def part1(filepath):
    print()
    codes = read_file_as_strings(filepath)

    total_complexity = 0

    for code in codes:
        total_complexity += complexity(code)

    return total_complexity
