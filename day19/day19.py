from tools.file import read_file_as_strings


def make_design(design, towels) -> bool:
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


def parse_input(filepath):
    lines = read_file_as_strings(filepath)

    # first line
    towels = lines.pop(0).split(", ")

    # seperator line
    _ = lines.pop(0)

    # rest of the file is designs wanted
    designs = lines

    return designs, towels


def part1(filepath):
    designs, towels = parse_input(filepath)

    return sum(1 for design in designs if make_design(design, towels))
