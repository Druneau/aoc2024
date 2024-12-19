import day19

example_towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]


def test_total_arrangements():
    assert day19.total_arrangements(example_towels, ["brwrr"]) == 2
    assert day19.total_arrangements(example_towels, ["bggr"]) == 1
    assert day19.total_arrangements(example_towels, ["gbbr"]) == 4
    assert day19.total_arrangements(example_towels, ["rrbgbr"]) == 6
    assert day19.total_arrangements(example_towels, ["brgr"]) == 2
    assert day19.total_arrangements(example_towels, ["bwurrg"]) == 1
    assert day19.total_arrangements(example_towels, ["ubwu"]) == 0
    assert day19.total_arrangements(example_towels, ["bbrgwb"]) == 0


def test_part1():
    assert day19.part1("day19/input_example.txt") == 6
    assert day19.part1("day19/input.txt") == 283


def test_part2():
    assert day19.part2("day19/input_example.txt") == 16
    assert day19.part2("day19/input.txt") == 615388132411142
