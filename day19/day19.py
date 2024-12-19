import time

from tools.file import read_file_as_strings


def can_be_made(design, towels):
    return make_design_recursive(design, towels)


def make_design_all(design, towels) -> bool:
    for combination in generate_combinations(design, len(towels)):
        if all(towel in towels for towel in combination):
            return True

    return False


def generate_combinations(chars, max_length):
    def helper(remaining, max_length):
        if not remaining:
            yield []
            return

        for i in range(1, min(len(remaining) + 1, max_length + 1)):
            prefix = remaining[:i]
            for suffix_combo in helper(remaining[i:], max_length):
                yield [prefix] + suffix_combo

    return helper(chars, max_length)


def make_design_recursive(design, towels):
    def backtrack(index):
        if index == len(design):  # Successfully matched entire design
            return True

        for towel in towels:
            if design.startswith(towel, index):  # Towel matches substring
                if backtrack(index + len(towel)):  # Recur with the next segment
                    return True

        return False  # No towel fits, backtrack

    return backtrack(0)


def reduce_towels(towels):
    reduced = []

    for i, towel in enumerate(towels):
        other_towels = towels[:i] + towels[i + 1 :]  # Exclude current towel
        if not can_be_made(towel, other_towels):  # Keep if it cannot be made
            reduced.append(towel)

    print(f"{len(towels)} towels reduced to {len(reduced)}")
    return reduced


def parse_input(filepath):
    lines = read_file_as_strings(filepath)

    # first line
    towels = lines[0].split(", ")

    # rest of the file is designs wanted
    designs = lines[2:]

    return designs, towels


def part1(filepath):
    designs, towels = parse_input(filepath)

    tried = 0
    passed = 0
    total = len(designs)

    towels = reduce_towels(towels)

    start_time = time.time()

    for design in designs:
        tried += 1
        if can_be_made(design, towels):
            passed += 1

        elapsed_time = time.time() - start_time
        remaining = total - tried
        estimated_finish = elapsed_time / tried * remaining if tried > 0 else 0

        print(
            f"Tried: {tried}/{total}, Passed: {passed}, Elapsed: {elapsed_time:.2f}s, ETA: {estimated_finish:.2f}s",
            end="\r",
            flush=True,
        )

    print()  # Ensure the progress line is cleared
    return passed
