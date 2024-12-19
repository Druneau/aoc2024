import day19

example_towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]


def test_can_make_design_all():
    assert day19.make_design_all("brwrr", example_towels)
    assert day19.make_design_all("bggr", example_towels)
    assert day19.make_design_all("gbbr", example_towels)
    assert day19.make_design_all("rrbgbr", example_towels)
    assert not day19.make_design_all("ubwu", example_towels)
    assert day19.make_design_all("bwurgg", example_towels)
    assert day19.make_design_all("brgr", example_towels)
    assert not day19.make_design_all("bbrgwb", example_towels)


def test_make_design_recursive():
    assert day19.make_design_recursive("brwrr", example_towels)
    assert day19.make_design_recursive("bggr", example_towels)
    assert day19.make_design_recursive("gbbr", example_towels)
    assert day19.make_design_recursive("rrbgbr", example_towels)
    assert not day19.make_design_recursive("ubwu", example_towels)
    assert day19.make_design_recursive("bwurgg", example_towels)
    assert day19.make_design_recursive("brgr", example_towels)
    assert not day19.make_design_recursive("bbrgwb", example_towels)


def test_part1():
    assert day19.part1("day19/input_example.txt") == 6
    assert day19.part1("day19/input.txt") == 283
