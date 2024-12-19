from tools.file import read_file_as_strings


def parse_input(filepath):
    lines = read_file_as_strings(filepath)

    towels = lines[0].split(", ")
    designs = lines[2:]

    return designs, towels


def count_arrangements(design, towels):
    subdesign_cache = {}

    def backtrack(index):
        if index == len(design):
            return 1

        if index in subdesign_cache:
            return subdesign_cache[index]

        count = 0
        for towel in towels:
            if design.startswith(towel, index):
                count += backtrack(index + len(towel))

        subdesign_cache[index] = count
        return count

    return backtrack(0)


def total_arrangements(towels, designs):
    return sum(count_arrangements(design, towels) for design in designs)


def count_possible_designs(towels, designs):
    return sum(1 for design in designs if count_arrangements(design, towels) > 0)


def part1(filepath):
    designs, towels = parse_input(filepath)
    return count_possible_designs(towels, designs)


def part2(filepath):
    designs, towels = parse_input(filepath)
    return total_arrangements(towels, designs)
