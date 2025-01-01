import day17


def test_part1():
    assert day17.part1("day17/input_example.txt") == "4,6,3,5,6,3,5,2,1,0"
    assert day17.part1("day17/input.txt") == "6,7,5,2,1,3,5,1,7"
    assert day17.part1("day17/input_copy.txt") == "2,4,1,3,7,5,1,5,0,3,4,1,5,5,3,0"


def test_part2():
    assert day17.part2("day17/input_example_2.txt") == 117440
    assert day17.part2("day17/input.txt") == 216549846240877


def test_calculate_register_a_from_bits():
    assert day17.calculate_register_a_from_bits([0]) == 0
    assert day17.calculate_register_a_from_bits([7]) == 7
    assert day17.calculate_register_a_from_bits([7, 1]) == 7 + 1 * 2**3
    assert day17.calculate_register_a_from_bits([7, 7]) == 7 + 7 * 2**3
    assert (
        day17.calculate_register_a_from_bits([7, 7, 0, 0, 0, 1])
        == 7 + 7 * 2**3 + 0 * 2**6 + 0 * 2**9 + 0 * 2**12 + 1 * 2**15
    )
