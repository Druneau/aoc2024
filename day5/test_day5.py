import day5

PATH_EXAMPLE = "day5/input_example.txt"
PATH_INPUT = "day5/input.txt"


def test_parse_rules():
    assert day5.parse_rules(PATH_EXAMPLE) == [
        (47, 53),
        (97, 13),
        (97, 61),
        (97, 47),
        (75, 29),
        (61, 13),
        (75, 53),
        (29, 13),
        (97, 29),
        (53, 29),
        (61, 53),
        (97, 53),
        (61, 29),
        (47, 13),
        (75, 47),
        (97, 75),
        (47, 61),
        (75, 61),
        (47, 29),
        (75, 13),
        (53, 13),
    ]


def test_matching_rules():
    rules = day5.parse_rules(PATH_EXAMPLE)
    assert day5.matching_rules(rules, pages=[75, 29, 13]) == [
        (75, 29),
        (29, 13),
        (75, 13),
    ]


def test_parse_updates():
    assert day5.parse_updates(PATH_EXAMPLE) == [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]


def test_part1():
    assert day5.part1(PATH_EXAMPLE) == 143
    assert day5.part1(PATH_INPUT) == 6242


def test_part2():
    assert day5.part2(PATH_EXAMPLE) == 123
    assert day5.part2(PATH_INPUT) == 5169
