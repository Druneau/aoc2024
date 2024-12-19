import day19

example_towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]


def test_can_make_design():
    assert day19.make_design("brwrr", example_towels)
    assert day19.make_design("bggr", example_towels)
    assert day19.make_design("gbbr", example_towels)
    assert day19.make_design("rrbgbr", example_towels)
    assert not day19.make_design("ubwu", example_towels)
    assert day19.make_design("bwurgg", example_towels)
    assert day19.make_design("brgr", example_towels)
    assert not day19.make_design("bbrgwb", example_towels)


def test_part1():
    assert day19.part1("day19/input_example.txt") == 6
    assert day19.part1("day19/input.txt") == 6
