import day17


def test_part1():
    assert day17.part1("day17/input_example.txt") == "4,6,3,5,6,3,5,2,1,0"
    assert day17.part1("day17/input.txt") == "6,7,5,2,1,3,5,1,7"


def test_part2():
    assert day17.part2("day17/input_example_2.txt") == 117440
    # assert day17.part2("day17/input.txt") == 117440
