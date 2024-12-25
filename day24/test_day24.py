import day24


def test_and():
    assert not day24._and(False, False)
    assert not day24._and(True, False)
    assert not day24._and(False, True)
    assert day24._and(True, True)


def test_or():
    assert not day24._or(False, False)
    assert day24._or(True, False)
    assert day24._or(False, True)
    assert day24._or(True, True)


def test_xor():
    assert not day24._xor(False, False)
    assert day24._xor(True, False)
    assert day24._xor(False, True)
    assert not day24._xor(True, True)


def test_parse_equation():
    assert day24.parse_equation("x00 AND y00 -> z00") == (
        "z00",
        ["x00", day24._and, "y00"],
    )

    assert day24.parse_equation("x01 XOR y01 -> z01") == (
        "z01",
        ["x01", day24._xor, "y01"],
    )

    assert day24.parse_equation("x00: 1") == (
        "x00",
        True,
    )

    assert day24.parse_equation("y01: 0") == (
        "y01",
        False,
    )


def test_part1():
    assert day24.part1("day24/input_example.txt") == 4
    assert day24.part1("day24/input_example_larger.txt") == 2024
    assert day24.part1("day24/input.txt") == 55544677167336


def test_number_to_bits():
    assert day24.number_to_bits(5, num_bits=4) == [False, True, False, True]


def test_bits_to_number():
    assert day24.bits_to_number([False, False, False, True, False, True]) == 5


def test_part2():
    assert day24.part2("day24/input_example_part2.txt") == "z00,z01,z02,z05"
